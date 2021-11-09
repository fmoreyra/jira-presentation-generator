from dataclasses import dataclass, field
from typing import List


@dataclass
class Ticket:
    jira_id: str
    summary: str
    status: str
    person_in_charge: str


@dataclass
class Epic:
    title: str
    tickets: List[Ticket] = field(default_factory=list)


@dataclass
class Sprint:
    number: int
    epics: List[Epic] = field(default_factory=list)
