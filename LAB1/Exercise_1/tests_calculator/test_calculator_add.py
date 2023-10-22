import pytest
from calculator import add

##ADD FUNCTION-------------------------------------------------
#-------------------------------------------------
test_cases_add_zero_int = [
    (0, 0, 0),
    (-0, -0, 0),
    (-0, 0, 0),
    (0, -0, 0),
    (6, 0, 6),
    (0, 9, 9),
    (-6, 0, -6),
    (0, -9, -9),
    (6, -0, 6),
    (-0, 9, 9),
    (-6, -0, -6),
    (-0, -9, -9)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_add_zero_int)
def test_add_zero_int(num_f, num_s, expected):
    assert add(num_f, num_s) == expected

#-------------------------------------------------
test_cases_add_int = [
    (6, 9, 15),
    (-6, -9, -15),
    (-6, 9, 3),
    (6, -9, -3)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_add_int)
def test_add_int(num_f, num_s, expected):
        assert add(num_f, num_s) == expected

#-------------------------------------------------
test_cases_add_zero_float = [
    (0.0, 0.0, 0.0),
    (-0.0, 0.0, 0.0),
    (-0.0, -0.0, 0.0),
    (0.0, -0.0, 0.0),
    (0.0, 4.5, 4.5),
    (2.5, 0.0, 2.5),
    (0.0, -4.5, -4.5),
    (-2.5, 0.0, -2.5),
    (-0.0, 4.5, 4.5),
    (2.5, -0.0, 2.5),
    (-0.0, -4.5, -4.5),
    (-2.5, -0.0, -2.5)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_add_zero_float)
def test_add_zero_float(num_f, num_s, expected):
        assert add(num_f, num_s) == expected

#-------------------------------------------------
test_cases_add_float = [
    (2.5, 4.5, 7.0),
    (-2.5, -4.5, -7.0),
    (-2.5, 4.5, 2.0),
    (2.5, -4.5, -2.0)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_add_float)
def test_add_float(num_f, num_s, expected):
        assert add(num_f, num_s) == expected

#-------------------------------------------------
test_cases_add_zero_float_and_int = [
    (0.0, 0, 0.0),
    (-0.0, -0, 0.0),
    (-0, 0.0, 0.0),
    (0, -0.0, 0.0),
    (2.5, 0, 2.5),
    (-2.5, 0, -2.5),
    (2, 0.0, 2),
    (-2, 0.0, -2),
    (0, 2.5, 2.5),
    (0, -2.5, -2.5),
    (0.0, 2, 2),
    (0.0, -2, -2)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_add_zero_float_and_int)
def test_add_zero_float_and_int(num_f, num_s, expected):
        assert add(num_f, num_s) == expected

#-------------------------------------------------
test_cases_add_float_and_int = [
    (2.5, 1, 3.5),
    (-2.5, -1, -3.5),
    (-2.5, 1, -1.5),
    (1, 2.5, 3.5),
    (1, -2.5, -1.5)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_add_float_and_int)
def test_add_float_and_int(num_f, num_s, expected):
        assert add(num_f, num_s) == expected

#-------------------------------------------------
test_cases_add_negativ = [
    ("1", "2", pytest.raises(TypeError)),
    ([1], [2], pytest.raises(TypeError)),
    (1, "2", pytest.raises(TypeError)),
    (1, [2], pytest.raises(TypeError)),
    ("1", 2, pytest.raises(TypeError)),
    ([1], 2, pytest.raises(TypeError)) 
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_add_negativ)
def test_add_negativ(num_f, num_s, expected):
        with expected:
            add(num_f, num_s)

#-------------------------------------------------
test_cases_add_input_types = [
   (6, 9),
   (6.5, 2.5),
   (6.5, 9)  
]

@pytest.mark.parametrize("num_f, num_s", test_cases_add_input_types)
def test_add_input_types(num_f, num_s):
        assert isinstance(add(num_f, num_s), (int, float))
#-------------------------------------------------