from starlette import status

from fastapi import APIRouter, Depends, HTTPException

from app.models.ticket import Ticket, TicketCreate
from app.repositories.ticket_repository import TicketRepository
from app.dependencies import get_ticket_repository

router = APIRouter(prefix="/ticket", tags=["ticket"])

@router.post("/", response_model=Ticket, status_code=status.HTTP_201_CREATED)
def create_ticket(data: TicketCreate, repository: TicketRepository = Depends(get_ticket_repository)):
    """endpoint to create a new ticket"""
    ticket: Ticket = Ticket(**data.model_dump())
    ticket: Ticket | None = repository.create(ticket)
    if ticket:
        return ticket
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket_id(ticket_id: int, repository: TicketRepository = Depends(get_ticket_repository)):
    """endpoint to delete a ticket"""
    ticket = repository.delete_by_id(ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/{ticket_id}", response_model=Ticket | None, status_code=status.HTTP_200_OK)
def get_ticket(ticket_id: int, repository: TicketRepository = Depends(get_ticket_repository)):
    """endpoint to get a ticket"""
    ticket: Ticket | None = repository.get_by_id(ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return ticket

@router.get("/", response_model=list[Ticket], status_code=status.HTTP_200_OK)
def get_tickets(repository: TicketRepository = Depends(get_ticket_repository)):
    """endpoint to get all tickets"""
    return repository.list_all()