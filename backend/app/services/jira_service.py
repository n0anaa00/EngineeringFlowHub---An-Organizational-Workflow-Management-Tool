class MockJiraService:

    @staticmethod
    def get_issues():

        return [

            {
                "key": "JIRA-1001",
                "summary": "Review CAD drawings"
            },

            {
                "key": "JIRA-1002",
                "summary": "Update pump specification"
            },

            {
                "key": "JIRA-1003",
                "summary": "Pipeline validation"
            }
        ]