from sqlmodel import Session, select
from app.models.ticket import Ticket
from sqlalchemy.exc import IntegrityError

class TicketRepository:
    """access to the ticket table"""

    def __init__(self, session: Session):
        self.session = session

    def create(self, ticket: Ticket) -> Ticket | None:
        """creates a new ticket"""
        self.session.add(ticket)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            return None
        self.session.refresh(ticket)
        return ticket

    def get_by_id(self, ticket_id: int) -> Ticket | None:
        """gets a ticket by its id"""
        return self.session.get(Ticket, ticket_id)

    def list_all(self) -> list[Ticket]:
        """lists all tickets"""
        return list(self.session.exec(select(Ticket)).all())

    def delete_by_id(self, ticket_id: int) -> Ticket | None:
        """deletes a ticket by its id"""
        ticket: Ticket | None = self.get_by_id(ticket_id)
        if ticket:
            self.session.delete(ticket)
            self.session.commit()
            return ticket
        return None
