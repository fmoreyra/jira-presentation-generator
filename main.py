from jira_data_adapter import JiraDataAdapter
import os

from pptx import Presentation
from pptx.dml.color import RGBColor


from dotenv import load_dotenv
load_dotenv()

sprint = JiraDataAdapter(
    jira_url=os.environ['JIRA_URL'],
    jira_username=os.environ['JIRA_USERNAME'],
    jira_password=os.environ['JIRA_API_KEY']
).adapt()

sprint.print_tickets()


prs = Presentation('template_demo.pptx')
title_slide_layout = prs.slide_layouts[0]
epic_slide_layout = prs.slide_layouts[8]
ticket_slide_layout = prs.slide_layouts[1]

slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title

title.text = "Demo - Sprint XXXX"

epics = []
for ticket in sprint.tickets:
    if ticket.epic_name not in epics:
        epic_slide = prs.slides.add_slide(epic_slide_layout)
        epic_slide.shapes[0].text = f"Épica: {ticket.epic_name}"
        epics.append(ticket.epic_name)
    ticket_slide = prs.slides.add_slide(prs.slide_layouts[2])
    ticket_slide.shapes[0].text = ticket.summary
    ticket_slide.shapes[1].text = f"Épica: {ticket.epic_name}"
    ticket_slide.shapes[2].text = ticket.jira_id
    ticket_slide.shapes[3].text = f"Responsable: {ticket.person_in_charge}"
    ticket_slide.shapes[4].text = f"Status: {ticket.status}"
    ticket_slide.shapes[4].fill.solid()
    ticket_slide.shapes[4].fill.fore_color.rgb = RGBColor(*ticket.status_color_rgb)

prs.save('test.pptx')
