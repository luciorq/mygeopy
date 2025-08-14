from mygeopy.triangle import hypot
import pytest

def test_hypot_calculation():
    """Test the basic calculation of the hypotenuse."""
    assert hypot(3, 4) == 5.0
    assert hypot(5, 12) == 13.0
    assert hypot(8, 15) == 17.0
    assert hypot(7, 24) == 25.0

def test_hypot_with_zero():
    """Test the hypotenuse calculation with zero values."""
    assert hypot(0, 0) == 0.0
    assert hypot(0, 5) == 5.0
    assert hypot(5, 0) == 5.0

def test_hypot_with_floats():
    """Test the hypotenuse calculation with floating-point numbers."""
    assert hypot(2.5, 6.0) == 6.5
    assert hypot(1.2, 3.5) == pytest.approx(3.7)

def test_hypot_invalid_input_type():
    """Test that hypot raises TypeError for non-numeric input."""
    with pytest.raises(TypeError):
        hypot("a", "b")
    with pytest.raises(TypeError):
        hypot(None, 5)

def test_hypot_negative_input():
    """Test that hypot raises ValueError for negative input."""
    with pytest.raises(ValueError):
        hypot(-3, 4)
    with pytest.raises(ValueError):
        hypot(3, -4)
    with pytest.raises(ValueError):
        hypot(-3, -4)
