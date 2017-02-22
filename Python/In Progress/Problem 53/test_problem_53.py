import pytest
import problem_53 as code

class test_Factorial:
    def test_zero(self):
        assert code.factorial(0) == 1

    def test_one(self):
        assert code.factorial(1) == 1

    def test_five(self):
        assert code.factorial(5) == 120

# class test_Choose:
#     def
