import pytest
import main


@pytest.mark.parametrize('x, y, res', [(5,7, 12), (1, 1, 2)])
@pytest.mark.math
def test_add(x, y, res):
    calc = main.Calc(x, y)
    assert calc.add() == res
    assert calc.add(x, y) == res


@pytest.mark.math
def test_mult():
    assert main.Calc.mult(6, 6) == 36

def test_average():
    calc = main.Calc()
    assert calc.average([1, 2, 4]) == 2.33

def test_calc_add():
    calc = main.Calc()
    assert calc + 1 == 1