import numbers

def hypot(a: float, b: float) -> float:
    """
    Compute the hypotenuse of a right triangle given sides `a` and `b`.

    Args:
        a (float): The length of one side next to the right angle
        b (float): The length of the second side next to the right angle

    Returns:
        float: The length of the hypotenuse

    Examples:
        >>> hypot(3, 4)
        5.0
    """

    if not (isinstance(a, numbers.Real) and isinstance(b, numbers.Real)):
        raise TypeError("`a` and `b` must be real numbers")

    if a < 0 or b < 0:
        raise ValueError("`a` and `b` must be a non-negative real numbers")

    return (a ** 2 + b ** 2) ** 0.5
