import pytest

from pythoncode.calculator import Calculator


class TestCalc:
    @pytest.mark.add
    def test_add(self):
        """
        测试相加
        """
        calc = Calculator()
        result = calc.add(1,1)
        assert 2 == result