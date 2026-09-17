"""Student records."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    student_id: str
    first_name: str
    last_name: str
    email: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class StudentRegistry:
    """In-memory store of students, keyed by student ID."""

    def __init__(self) -> None:
        self._students: dict[str, Student] = {}

    def add(self, student: Student) -> None:
        if student.student_id in self._students:
            raise ValueError(f"Student {student.student_id} already exists")
        self._students[student.student_id] = student

    def get(self, student_id: str) -> Student:
        try:
            return self._students[student_id]
        except KeyError as exc:
            raise LookupError(f"Student {student_id} not found") from exc

    def all(self) -> list[Student]:
        return sorted(self._students.values(), key=lambda s: s.last_name)
