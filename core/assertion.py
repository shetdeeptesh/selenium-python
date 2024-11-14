import logging


_logger = logging.getLogger("CustomLogger")


_assert_data = {
    "pass_count":0,
    "fail_count":0,
    "test_cases":[]
}

def get_data():
    return _assert_data

def _add_count(status):
    if status == "Pass":
        _assert_data["pass_count"] += 1
    else: 
        _assert_data["fail_count"] += 1

def _add_data(actual, expected, title, status, remark=None):
    _add_count(status)
    _assert_data['test_cases'].append({"actual": actual, "expected": expected, "title": title, "status": status,  "remark":  remark })



def assert_equal(expected, actual, title):
    if expected == actual:
        _logger.info(f"{title} -> Pass")
        _add_data(actual, expected, title, "Pass")
    else:
        _logger.info(f"{title} -> Fail")
        _add_data(actual, expected, title, "Fail" )


def assert_greater_than(expected, actual, title):
    if actual > expected:
        _logger.info(f"{title} -> Pass")
        _add_data(actual, f"greater then {expected}", title, "Pass" )
    else:
        _logger.info(f"{title} -> Fail")
        _add_data(actual, expected, title, "Fail" )
        
