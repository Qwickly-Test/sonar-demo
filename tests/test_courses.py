import pytest

from qwickly.courses import Course


def test_enroll_reduces_seats():
    course = Course("CS101", "Intro to CS", capacity=2)
    course.enroll("s1")
    assert course.seats_left == 1


def test_cannot_enroll_twice():
    course = Course("CS101", "Intro to CS", capacity=2)
    course.enroll("s1")
    with pytest.raises(ValueError):
        course.enroll("s1")


def test_full_course():
    course = Course("CS101", "Intro to CS", capacity=1)
    course.enroll("s1")
    with pytest.raises(ValueError):
        course.enroll("s2")


def test_drop():
    course = Course("CS101", "Intro to CS", capacity=1)
    course.enroll("s1")
    course.drop("s1")
    assert course.seats_left == 1
