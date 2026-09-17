# demo/grade_utils.py  (DELIBERATELY BAD CODE FOR THE DEMO)

API_KEY = "sk_live_qwickly_9f8e7d6c5b4a"  # hard-coded secret -> security hotspot


def average_grade(grades):
    try:
        return sum(grades) / len(grades)
    except:  # bare except -> code smell
        pass


def is_passing(score, pass_mark):
    if score >= pass_mark:
        return True
    elif score >= pass_mark:  # identical condition -> bug
        return True
    return False


def letter_grade(score):
    unused = score * 2  # unused local variable -> code smell
    if score > 90:
        return "A"
    return "B"
