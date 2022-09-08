

def fizzBuzz(number: int) -> str:

    divisibleByThree: bool = (number % 3 == 0)
    divisibleByFive: bool = (number % 5 == 0)
    divisibleByThreeAndFive: bool = divisibleByThree and divisibleByFive

    if divisibleByThreeAndFive:
        return "FizzBuzz"
    elif divisibleByThree:
        return "Fizz"
    elif divisibleByFive:
        return "Buzz"
    return str(number)