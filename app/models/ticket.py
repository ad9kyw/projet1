from datetime import datetime

from sqlmodel import Field, SQLModel
from app.models.enums import TicketCategory, TicketStatus

class Ticket(SQLModel, table=True):
    """represent a ticket to prioritize"""
    id: int | None = Field(default=None, primary_key=True)
    content: str
    category: TicketCategory
    status: TicketStatus = Field(default=TicketStatus.ACTIVE)
    priority: int = Field(default=5)
    created_at: datetime = Field(default_factory=datetime.now)

class TicketCreate(SQLModel):
    """represent a ticket at creation"""
    content: str
    category: TicketCategory