import pytest

from qwickly.students import Student, StudentRegistry


def make_student(student_id="s1", last_name="Lovelace"):
    return Student(student_id, "Ada", last_name, f"{student_id}@example.com")


def test_full_name():
    assert make_student().full_name == "Ada Lovelace"


def test_add_and_get():
    registry = StudentRegistry()
    student = make_student()
    registry.add(student)
    assert registry.get("s1") == student


def test_duplicate_rejected():
    registry = StudentRegistry()
    registry.add(make_student())
    with pytest.raises(ValueError):
        registry.add(make_student())


def test_missing_student():
    with pytest.raises(LookupError):
        StudentRegistry().get("nope")


def test_all_sorted_by_last_name():
    registry = StudentRegistry()
    registry.add(make_student("s1", "Turing"))
    registry.add(make_student("s2", "Hopper"))
    assert [s.last_name for s in registry.all()] == ["Hopper", "Turing"]
