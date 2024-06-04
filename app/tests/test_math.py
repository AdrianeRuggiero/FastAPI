from app.controllers.math import inc, minus

def test_inc():
    assert inc(3) == 4

def test_minus():
    assert minus(3) == 2