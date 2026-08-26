from enum import Enum

class TicketCategory(str, Enum):
    """category of tickets"""
    HARDWARE = "hardware"
    HR_SUPPORT = "hr_support"
    ACCESS = "access"
    MISCELLANEOUS = "miscellaneous"
    STORAGE = "storage"
    PURCHASE = "purchase"
    INTERNAL_PROJECT = "internal_project"
    ADMINISTRATIVE_RIGHTS = "administrative_rights"

class TicketStatus(str, Enum):
    """status of tickets"""
    ACTIVE = "active"
    FINISHED = "finished"