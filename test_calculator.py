import calculator


class TestCalculator:

    def test_addition(self):
        assert calculator.add(2, 2) == 4

    def test_subtraction(self):
        assert calculator.subtract(4, 2) == 2

    def test_multiplication(self):
        assert calculator.multiply(10, 10) == 100

    def test_division(self):
        assert calculator.divide(25, 5) == 5
