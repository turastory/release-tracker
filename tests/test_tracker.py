from tracker import tracker


def test_filter_regex():
    strings = ["Android10", "iOS", "3.141592"]
    assert tracker.filter_regex(
            strings, "[a-zA-Z]+") == ["Android10", "iOS"]
    assert tracker.filter_regex(
            strings, "\\d+") == ["3.141592"]
    assert tracker.filter_regex(
            strings, "[A-Z]+|\\d") == ["Android10", "3.141592"]
