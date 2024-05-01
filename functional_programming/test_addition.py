import addition

import pytest

def test_add():
    assert addition.add(4,6) == 10

def test_sub():
    assert addition.sub(4,6) == -2 