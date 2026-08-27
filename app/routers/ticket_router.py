from starlette import status

from fastapi import APIRouter, Depends

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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="something went wrong")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket_id(id: int, repository: TicketRepository = Depends(get_ticket_repository)):
    """endpoint to delete a ticket"""
    repository.delete_by_id(id)

@router.get("/{id}", response_model=Ticket | None, status_code=status.HTTP_200_OK)
def get_ticket(id: int, repository: TicketRepository = Depends(get_ticket_repository)):
    """endpoint to get a ticket"""
    return repository.get_by_id(id)

@router.get("/", response_model=list[Ticket], status_code=status.HTTP_200_OK)
def get_tickets(repository: TicketRepository = Depends(get_ticket_repository)):
    """endpoint to get all tickets"""
    return repository.list_all()