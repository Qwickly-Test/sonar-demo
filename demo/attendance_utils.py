# demo/attendance_utils.py  (DELIBERATELY BAD CODE FOR THE DEMO)

DB_PASSWORD = "admin123"  # hard-coded credential -> security hotspot


def attendance_percentage(present, total):
    try:
        return present / total * 100
    except:  # bare except -> code smell
        pass


def is_same_session(session_a, session_b):
    return session_a == session_a  # compares a value with itself -> bug


def unused_helper(student_id):
    result = student_id  # unused local variable -> code smell
    return None
