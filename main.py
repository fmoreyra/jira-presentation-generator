from jira_data_adapter import JiraDataAdapter
import os
from dotenv import load_dotenv
load_dotenv()

sprint = JiraDataAdapter(jira_url=os.environ['JIRA_URL'],
                         jira_username=os.environ['JIRA_USERNAME'],
                         jira_password=os.environ['JIRA_API_KEY']).adapt()

# Do things with the sprint (Google presentation module uses this instance)

