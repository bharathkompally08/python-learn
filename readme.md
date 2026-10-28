### LEARNING PYTHON (DAY-WISE)
## DAY 1
BASICS:
print, input& output, variables, operators, data types, type conversions, conditional statements, loops
EXCERICES: 
Exercise 1: Hello Python
    Create hello.py.
    Store your name, your current language (JavaScript), and your target language (Python) in variables.
    Print a single formatted sentence using an f-string.
    Expected output:
    My name is ___, I currently write JavaScript, and I am learning Python.
Exercise 2: Type Explorer
    Create types.py.
    Create one variable for each type: int, float, str, bool, NoneType.
    Print each variable and its type.
    Print the results of True + True and True + False. Predict the output before running.
Exercise 3: Age Calculator
    Create age_calc.py.
    Ask the user for their birth year using input().
    Calculate their approximate age.
    Print the result with an f-string.
    Hint: input() returns a string. What happens if you subtract a string from an integer?
    Expected interaction:
    Enter your birth year: 1995
    You are approximately 30 years old.
Exercise 4: Operator Predictions
    Create operators.py. Predict each output as a comment BEFORE running. Then run and check.
    print(10 / 3)
    print(10 // 3)
    print(10 % 3)
    print(2 ** 10)
    print(2 ^ 10)
    print(1 == True)
    print(1 == "1")
    print(0 == False)
    print(not True)
    print(True and False)
    print(True or False)
    For any wrong prediction, write a one-sentence explanation of why.
Exercise 5: Debug This
    Create debug.py. This code has three bugs. Find and fix them. Comment each fix.
    name = input("What is your name? ")
    age = input("What is your age? ")
    birth_year = 2025 - age
    print(f"Hello {name}! You were born in {birth_year}.")
    is_adult = age >= 18
    print(f"Adult status: {is_adult}")
    Expected after fix:
    What is your name? Alice
    What is your age? 30
    Hello Alice! You were born in 1995.
    Adult status: True
Mini-Project: CLI Unit Converter
    Problem
    Build a command-line tool that converts between units. It runs in a loop until the user quits.
    Menu Options
    Celsius → Fahrenheit
    Fahrenheit → Celsius
    Kilometers → Miles
    Miles → Kilometers
    Kilograms → Pounds
    Pounds → Kilograms
    Quit
    Requirements
    Display the menu, ask for a choice by number.
    Ask for the value to convert.
    Print the result rounded to 2 decimal places.
    Loop back to the menu after each conversion.
    Exit cleanly on "Quit."
    Use only built-in Python (no imports).
    Use while, if/elif/else, input(), print(), f-strings.
    Acceptance Criteria
    Runs without errors
    All conversions are mathematically correct
    Menu loops until quit
    Output includes units and is formatted clearly
    Formulas (look these up if you don't know them)
    °F = °C × 9/5 + 32
    1 km ≈ 0.621371 miles
    1 kg ≈ 2.20462 pounds
    Handle invalid input (non-numeric values) without crashing. Hint: You may need try/except, which we cover on Day 2. If you don't know it yet, skip this.