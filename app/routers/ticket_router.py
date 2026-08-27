from starlette import status

from fastapi import APIRouter, Depends

from app.models.ticket import Ticket, TicketCreate
from app.repositories.ticket_repository import TicketRepository
from app.dependencies import get_ticket_repository

router = APIRouter(prefix="/ticket", tags=["ticket"])

@router.post("/", response_model=Ticket, status_code=status.HTTP_201_CREATED)
def create_ticket(data: TicketCreate, repository: TicketRepository = Depends(get_ticket_repository)):
    """endpoint to create a new ticket"""
    ticket: Ticket = Ticket(**data.dict())
    return repository.create(ticket)