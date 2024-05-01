from curses.ascii import isdigit
import find_string
import pytest

def test_ispresent():
    assert find_string.ispresent("N7")


def test_nodigit():
    assert find_string.nodigit("Al")