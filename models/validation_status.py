# Enum for validation status
from enum import Enum


class ValidationStatus(Enum):
    """
        Enum for defining different validation statuses for document validation.
        """
    VALID = 'VALID'
    INVALID = 'INVALID'
    ERROR = 'ERROR'
    NOT_FOUND = 'NOT_FOUND'
    NOT_PROCESSED = 'NOT_PROCESSED'