import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 1) == 3
