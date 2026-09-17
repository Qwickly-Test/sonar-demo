"""Courses and enrolment."""

from dataclasses import dataclass, field


@dataclass
class Course:
    code: str
    title: str
    capacity: int
    enrolled: set[str] = field(default_factory=set)

    @property
    def seats_left(self) -> int:
        return self.capacity - len(self.enrolled)

    def enroll(self, student_id: str) -> None:
        if student_id in self.enrolled:
            raise ValueError(f"{student_id} is already enrolled in {self.code}")
        if self.seats_left <= 0:
            raise ValueError(f"{self.code} is full")
        self.enrolled.add(student_id)

    def drop(self, student_id: str) -> None:
        self.enrolled.discard(student_id)
