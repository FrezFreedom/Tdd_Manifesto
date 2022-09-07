
from FizzBuzz import checkNumberIsDividedByThree, checkNumberIsDividedByFive, checkNumberIsDividedByThreeAndFive, fizzBuzz

# test checkNumberIsDividedByThree function

def test_ShouldReturnTrue_whenNumberIsDividedByThree():
    assert checkNumberIsDividedByThree(36) == True

def test_ShouldReturnFalse_whenNumberIsNotDividedByThree():
    assert checkNumberIsDividedByThree(37) == False

# test checkNumberIsDividedByFive function

def test_ShouldReturnTrue_whenNumberIsDividedByFive():
    assert checkNumberIsDividedByFive(35) == True

def test_ShouldReturnFalse_whenNumberIsNotDividedByFive():
    assert checkNumberIsDividedByFive(34) == False

# test checkNumberIsDividedByThreeAndFive function

def test_ShouldReturnTrue_whenNumberIsDividedByThreeAndFive():
    assert checkNumberIsDividedByThreeAndFive(30) == True

def test_ShouldReturnFalse_whenNumberIsDividedByThreeAndFive():
    assert checkNumberIsDividedByThreeAndFive(31) == False

# test fizzBuzz function

def test_ShouldReturnFizz_whenNumberIsDividedByThree():
    assert fizzBuzz(18) == "Fizz"

def test_ShouldReturnBuzz_whenNumberIsDividedByFive():
    assert fizzBuzz(10) == "Buzz"

def test_ShouldReturnFizzBuzz_whenNumberIsDividedByThreeAndFive():
    assert fizzBuzz(30) == "FizzBuzz"

def test_ShouldReturnNone_whenNumberIsNotDividedByThreeOrFive():
    assert fizzBuzz(2) == None