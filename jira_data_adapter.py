from atlassian import Jira
from jira_api import Sprint


class JiraDataAdapter:
    def __init__(self, jira_url, jira_username, jira_password) -> None:
        assert isinstance(jira_url, str)
        assert isinstance(jira_username, str)
        assert isinstance(jira_password, str)
        self._jira = Jira(url=jira_url, username=jira_username, password=jira_password, cloud=True)
        self._jwt_query = 'Project = "W3D" AND sprint in openSprints() ORDER BY parent ASC'

    def adapt(self) -> Sprint:
        current_sprint_dict = self._jira.jql(self._jwt_query)
        print(f"Amount of issues in sprint: {len(current_sprint_dict['issues'])}")
        for issue in current_sprint_dict['issues']:
            print("----------------------------------------------------------")
            print(f"Issue Key: {issue['key']}")
            print(f"Issue Summary: {issue['fields']['summary']}")
            print(f"Status: {issue['fields']['status']['name']}")
            try:
                print(f"Epic: {issue['fields']['parent']['fields']['summary']}")
            except KeyError:
                print("No related epic")
            try:
                print(f"Person in charge: {issue['fields']['assignee']['displayName']}")
            except (KeyError, TypeError):
                print("No person in charge of this ticket, generally we use TEAM here")
            print("----------------------------------------------------------")
