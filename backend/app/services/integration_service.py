from app.services.jira_service import (
    MockJiraService
)


class IntegrationService:

    @staticmethod
    def sync_jira():

        return MockJiraService.get_issues()