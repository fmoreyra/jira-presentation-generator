from dataclasses import dataclass, field
from typing import List


@dataclass
class Ticket:
    jira_id: str
    epic_name: str
    summary: str
    status: str
    person_in_charge: str

    def __post_init__(self):
        assert isinstance(self.jira_id, str)
        assert isinstance(self.epic_name, str)
        assert isinstance(self.summary, str)
        assert isinstance(self.status, str)
        assert isinstance(self.person_in_charge, str)


@dataclass
class Sprint:
    number: int
    tickets: List[Ticket] = field(default_factory=list)

    def add_ticket(self, ticket):
        assert isinstance(ticket, Ticket)
        self.tickets.append(ticket)

    def print_tickets(self):
        print(f"Amount of issues in sprint: {len(self.tickets)}")
        for ticket in self.tickets:
            print("----------------------------------------------------------")
            print(f"Issue Key: {ticket.jira_id}")
            print(f"Issue Summary: {ticket.summary}")
            print(f"Status: {ticket.status}")
            print(f"Epic: {ticket.epic_name}")
            print(f"Person in charge: {ticket.person_in_charge}")
            print("----------------------------------------------------------")

