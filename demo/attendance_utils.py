# demo/attendance_utils.py  (FIXED)
import os

DB_PASSWORD = os.environ.get("DB_PASSWORD", "")


def attendance_percentage(present: int, total: int) -> float:
    if total == 0:
        return 0.0
    return present / total * 100


def is_same_session(session_a: str, session_b: str) -> bool:
    return session_a == session_b
