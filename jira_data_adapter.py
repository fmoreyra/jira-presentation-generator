from atlassian import Jira
from jira_api import Sprint, Ticket


class JiraDataAdapter:
    def __init__(self, jira_url, jira_username, jira_password) -> None:
        assert isinstance(jira_url, str)
        assert isinstance(jira_username, str)
        assert isinstance(jira_password, str)
        self._jira = Jira(url=jira_url, username=jira_username, password=jira_password, cloud=True)
        self._jwt_query = 'Project = "W3D" AND sprint in openSprints() ORDER BY parent ASC'


    def adapt(self) -> Sprint:
        current_sprint_dict = self._jira.jql(self._jwt_query)
        sprint = Sprint(number=123)
        for issue in current_sprint_dict['issues']:
            jira_id = issue['key']
            summary = issue['fields']['summary']
            status = issue['fields']['status']['name']
            try:
                epic_name = issue['fields']['parent']['fields']['summary']
            except KeyError:
                epic_name = "Otros"
            
            try:
                person_in_charge = issue['fields']['assignee']['displayName']
            except (KeyError, TypeError):
                person_in_charge = "TEAM"

            sprint.add_ticket(Ticket(jira_id, epic_name, summary, status, person_in_charge))
        return sprint

