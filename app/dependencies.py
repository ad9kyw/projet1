from fastapi import Depends
from sqlmodel import Session

from app.database import get_session
from app.repositories.ticket_repository import TicketRepository

def get_ticket_repository(session: Session = Depends(get_session)) -> TicketRepository:
    """give the ticket repository"""
    return TicketRepository(session)