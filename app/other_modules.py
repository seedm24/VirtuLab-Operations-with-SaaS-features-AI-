
# app/other_modules.py

from datetime import datetime
from typing import Any, Dict

def format_timestamp(timestamp: datetime) -> str:
    """
    Convert a datetime object to a formatted string.
    """
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

class ResponseFormatter:
    """
    A helper class to format API responses consistently.
    """

    @staticmethod
    def success(data: Any, message: str = "Operation successful") -> Dict[str, Any]:
        return {
            "status": "success",
            "message": message,
            "data": data,
        }

    @staticmethod
    def error(error_message: str, data: Any = None) -> Dict[str, Any]:
        return {
            "status": "error",
            "message": error_message,
            "data": data,
        }
