from django_extensions.management.jobs import BaseJob, DailyJob


class Job(DailyJob):
    help = "My sample job."

    def execute(self):
        # executing empty sample job
        pass
