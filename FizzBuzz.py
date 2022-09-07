

def checkNumberIsDividedByThree(number: int) -> bool:
    return number % 3 == 0

def checkNumberIsDividedByFive(number: int) -> bool:
    return number % 5 == 0

def checkNumberIsDividedByThreeAndFive(number: int) -> bool:
    return checkNumberIsDividedByThree(number) and checkNumberIsDividedByFive(number)


def fizzBuzz(number: int) -> str:

    if checkNumberIsDividedByThreeAndFive(number):
        return "FizzBuzz"
    elif checkNumberIsDividedByThree(number):
        return "Fizz"
    elif checkNumberIsDividedByFive(number):
        return "Buzz"
    return None