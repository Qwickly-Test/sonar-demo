"""Attendance tracking per course session."""

from collections import defaultdict
from datetime import date


class AttendanceBook:
    """Records which students were present at each session of a course."""

    def __init__(self, course_code: str) -> None:
        self.course_code = course_code
        self._sessions: dict[date, set[str]] = defaultdict(set)

    def mark_present(self, session_day: date, student_id: str) -> None:
        self._sessions[session_day].add(student_id)

    def session_count(self) -> int:
        return len(self._sessions)

    def sessions_attended(self, student_id: str) -> int:
        return sum(1 for present in self._sessions.values() if student_id in present)

    def attendance_rate(self, student_id: str) -> float:
        """Return the student's attendance as a percentage (0-100)."""
        total = self.session_count()
        if total == 0:
            return 0.0
        return round(self.sessions_attended(student_id) / total * 100, 2)
