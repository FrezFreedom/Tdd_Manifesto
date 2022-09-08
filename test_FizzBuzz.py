
from FizzBuzz import fizzBuzz

# test fizzBuzz function

def test_ShouldReturnFizz_whenNumberIsDividedByThree():
    assert fizzBuzz(18) == "Fizz"

def test_ShouldReturnBuzz_whenNumberIsDividedByFive():
    assert fizzBuzz(10) == "Buzz"

def test_ShouldReturnFizzBuzz_whenNumberIsDividedByThreeAndFive():
    assert fizzBuzz(30) == "FizzBuzz"

def test_ShouldReturnNone_whenNumberIsNotDividedByThreeOrFive():
    assert fizzBuzz(2) == None