import main


def test_decimal_to_binary():
    assert main.decimal_to_binary(144) == "10010000"
    assert main.decimal_to_binary(2) == "10"
    assert main.decimal_to_binary(1) == "1"


def test_factorial():
    assert main.factorial(4) == 24
    assert main.factorial(2) == 2
    assert main.factorial(1) == 1

