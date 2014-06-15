import requests

from lplight import models


class RestClient(object):

    def __init__(self):
        self.default_headers = {}
        self.default_parameters = {}

    def build_headers(self, headers={}, params={}):
        actual_headers = {}
        actual_params = {}

        actual_headers.update(self.default_headers)
        actual_headers.update(headers)

        actual_params.update(self.default_parameters)
        actual_params.update(params)

        return actual_headers, actual_params

    def get(self, uri, model=None, headers={}, params={}, is_collection=False):
        actual_headers, actual_params = self.build_headers(headers, params)

        resp = requests.get(uri, headers=actual_headers, params=actual_params)
        setattr(resp, 'model', None)

        # Make sure we only attempt to deserialize if we get a valid code.
        if model and resp.status_code >= 200 and resp.status_code < 300:
            # TODO(jmv): Clean this up
            if is_collection:
                entries = []
                while uri:
                    json = resp.json()
                    uri = json.get('next_collection_link')
                    for item in json.get('entries'):
                        entries.append(model.from_json(item))

                    if uri:
                        # Parameters provided by the collection link
                        resp = requests.get(uri, headers=actual_headers)
                resp.model = entries
            else:
                resp.model = model.from_json(resp.json())

        return resp


class LaunchpadClient(object):
    BASE_URI = 'https://api.launchpad.net/1.0'

    def __init__(self):
        self._client = RestClient()

    def get_project(self, name):
        """ Retrives project information by name

        :param name: The formal project name in string form.
        """
        uri = '{base}/{project}'.format(base=self.BASE_URI, project=name)
        resp = self._client.get(uri, model=models.Project)

        return resp

    def get_bugs(self, project, status=None):
        """ Retrives a List of bugs for a given project.
        By default, this will only return activate bugs. If you wish to
        retrieve a non-active bug then specify the status through the
        status parameter.

        :param project: The formal project name.
        :param status: Allows filtering of bugs by current status.
        """
        uri = '{base}/{project}'.format(base=self.BASE_URI, project=project)
        parameters = {'ws.op': 'searchTasks'}

        if status:
            parameters['status'] = status

        resp = self._client.get(uri, model=models.Bug, is_collection=True,
                                params=parameters)

        return resp

    def get_bug_by_id(self, bug_id):
        """ Retrieves a single bug by it's Launchpad bug_id

            :param bug_id: The Launchpad id for the bug.
        """
        uri = '{base}/bugs/{bug_id}'.format(base=self.BASE_URI, bug_id=bug_id)
        resp = self._client.get(uri, model=models.Bug)

        return resp

    def get_bug_tasks(self, bug_id):
        uri = '{base}/bugs/{bug_id}/bug_tasks'.format(base=self.BASE_URI,
                                                      bug_id=bug_id)
        resp = self._client.get(uri, model=models.BugTask, is_collection=True)
        return resp
