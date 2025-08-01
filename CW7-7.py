# Part 1 of Excercise 7
import math


def circle_circumference(radius: float) -> float:
    """Function to calculate the circumference of a circle with radius -r-"""
    return 2 * math.pi * radius

# Part 2 of Excercise 7


def adding_numbers(number1: float, number2: float) -> float:
    """A function to calculate the sum of two numbers"""
    return number1 + number2


number1 = 5
number2 = 10
print(adding_numbers(number1, number2))

# Part 3 of Excercise 7


class GeneratingReport:
    def generate(self):
        """The reports are generated and called."""
        return "report"


class Saver:
    def save_to_file(self, report: str, filename: str):
        """Saves given reports to a file."""
        with open(filename, 'w') as f:
            f.write(report)

# Part 4 of Excercise 7


def read(file: str) -> str:
    """Reads all lines of file"""
    with open(file, "r") as f:
        return f.readlines


def clean(lines):
    """Erase lines from empty spaces"""
    for line in lines:
        return line.strip()


def
