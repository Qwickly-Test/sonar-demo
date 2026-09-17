from datetime import date

from qwickly.attendance import AttendanceBook


def test_rate_with_no_sessions():
    assert AttendanceBook("CS101").attendance_rate("s1") == 0.0


def test_rate():
    book = AttendanceBook("CS101")
    book.mark_present(date(2026, 9, 1), "s1")
    book.mark_present(date(2026, 9, 1), "s2")
    book.mark_present(date(2026, 9, 2), "s2")
    book.mark_present(date(2026, 9, 3), "s2")
    assert book.session_count() == 3
    assert book.attendance_rate("s1") == 33.33
    assert book.attendance_rate("s2") == 100.0
