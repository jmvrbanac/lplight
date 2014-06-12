import six


class SimpleModel(object):

    def _json_to_obj(self, json_dict):
        for key, val in six.iteritems(json_dict):
            if hasattr(self, key):
                setattr(self, key, val)

    @classmethod
    def from_json(cls, json_dict):
        obj = cls()
        obj._json_to_obj(json_dict)
        return obj


class Project(SimpleModel):

    def __init__(self):
        self.name = None
        self.display_name = None
        self.title = None
        self.description = None
        self.summary = None
        self.active = None
        self.date_created = None
        self.licenses = []
        self.official_bug_tags = []

        self.wiki_url = None
        self.homepage_url = None
        self.download_url = None
        self.information_type = None
        self.programming_language = None

        self.private = False
        self.private_bugs = None

        self.active_milestones_collection_link = None
        self.all_milestones_collection_link = None
        self.releases_collection_link = None
        self.series_collection_link = None
        self.bug_tracker_link = None
        self.project_group_link = None

        self.bug_supervisor_link = None
        self.driver_link = None
        self.web_link = None
        self.owner_link = None


class Bug(SimpleModel):

    def __init__(self):
        self.date_closed = None
        self.date_assigned = None
        self.title = None
        self.bug_link = None
        self.bug_watch_link = None
        self.milestone_link = None
        self.http_etag = None
        self.date_left_closed = None
        self.date_fix_committed = None
        self.date_fix_released = None
        self.date_in_progress = None
        self.resource_type_link = None
        self.status = None
        self.bug_target_name = None
        self.importance = None
        self.assignee_link = None
        self.date_triaged = None
        self.self_link = None
        self.target_link = None
        self.bug_target_display_name = None
        self.related_tasks_collection_link = None
        self.date_confirmed = None
        self.date_left_new = None
        self.web_link = None
        self.owner_link = None
        self.date_created = None
        self.date_incomplete = None
        self.is_complete = None


class BugStatus(object):
    NEW = 'New'
    INCOMPLETE = 'Incomplete'
    OPINION = 'Opinion'
    INVALID = 'Invalid'
    WONT_FIX = 'Won\'t Fix'
    EXPIRED = 'Expired'
    CONFIRMED = 'Confirmed'
    TRIAGED = 'Triaged'
    IN_PROGRESS = 'In Progress'
    FIX_COMMITTED = 'Fix Committed'
    FIX_RELEASED = 'Fix Released'
    INCOMPLETE_W_RESPONSE = 'Incomplete (with response)'
    INCOMPLETE_WO_RESPONSE = 'Incomplete (without response)'
