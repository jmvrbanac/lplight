from specter import Spec, expect

from lplight import models


class SampleModelImpl(models.SimpleModel):
    """ Dirty Implementation of a model for testing."""
    def __init__(self):
        self.field_a = None
        self.field_b = None


class SimpleModel(Spec):

    def can_deserialize(self):
        result = SampleModelImpl.from_json({
            'field_a': 'Tester',
            'field_b': True
        })

        expect(result).not_to.be_none()
        expect(result.field_a).to.equal('Tester')
        expect(result.field_b).to.be_true()


class ProjectModel(Spec):

    def can_deserialize(self):
        name = 'Test Name'
        title = 'Test Title'
        bug_tracker_link = 'Test link'

        sample_dict = {
            'name': name,
            'title': title,
            'bug_tracker_link': bug_tracker_link
        }

        project = models.Project.from_json(sample_dict)

        expect(project.name).to.equal(name)
        expect(project.title).to.equal(title)
        expect(project.bug_tracker_link).to.equal(bug_tracker_link)


class BugModel(Spec):

    def can_deserialize(self):
        sample_dict = {
            'name': 'Test Name',
            'title': 'Test Title',
            'id': 'Test id',
            'bug_tasks_collection_link': 'bug task link'
        }

        bug = models.Bug.from_json(sample_dict)

        for key, val in sample_dict.items():
            bug_attr = getattr(bug, key)
            expect(bug_attr).to.equal(sample_dict[key])


class BugTaskModel(Spec):

    def can_deserialize(self):
        sample_dict = {
            'date_assigned': 'Test assigned',
            'title': 'Test Title',
            'date_closed': 'stuff'
        }

        bug = models.BugTask.from_json(sample_dict)

        for key, val in sample_dict.items():
            bug_attr = getattr(bug, key)
            expect(bug_attr).to.equal(sample_dict[key])
