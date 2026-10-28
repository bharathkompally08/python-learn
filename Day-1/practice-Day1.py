# Exercise 1: Hello, Python
    # Create hello.py.

    # Create three variables: one for your name, one for your age, and one for your city.
    # Print a single sentence using an f-string that includes all three variables.

name = "Bharath"
age = 24
city = "Hyderabad"
# print(f"My name is {name} and my age is {age} and I'm from {city}")

# Exercise 2: Type Explorer
    # Create types.py.

    # Create one variable for each of the five types: int, float, str, bool, NoneType.
    # Print each variable alongside its type using type().
    # Then print the results of True + True, True + False, and False + False. Write your prediction as a comment before each line, then run the code and check.
a = 22
b = 2.22
c= "india"
d= True
e = None
# print(a, type(a)) ## 22, <class 'int'>
# print(b, type(b)) ## 2.22, <class 'float'>
# print(c, type(c)) ## india, <class 'str'>
# print(d, type(d)) ## True, <class 'bool'>
# print(e, type(e)) ## None, <class 'NoneType'>
# print(True + True)  ## 2
# print(True + False) ## 1
# print(False + False) ## 0

# Exercise 3: Age Calculator
    # Create age_calc.py.
    # Ask the user for their birth year using input().
    # Calculate their approximate age by subtracting their birth year from 2025.
    # Print the result using an f-string.
# birth_year = int(input("What is your birth year : "))
# year = 2025
# age = year - birth_year
# print(f"Your age is : {age}") ## Your age is : 24

# Exercise 4: Operator Predictions
    # Create operators.py. Before running the code, write a comment above each print line with your predicted output. Then run the file and compare.

# Exercise 5: Debug This Code
    # Create debug.py. The following code has three bugs. Find and fix all three. Add a comment above each fix explaining what was wrong and why your fix works.

    # name = input("What is your name? ")
    # age = input("What is your age? ")
    # birth_year = 2025 - age
    # print(f"Hello {name}! You were born in {birth_year}.")
    # is_adult = age >= 18
    # print(f"Adult status: {is_adult}")

# name = input("What is your name? ")
# age = int(input("What is your age? ")) ## input default takes string format need to convert to int - Fix type convert to int
# birth_year = 2025 - age 
# print(f"Hello {name}! You were born in {birth_year}.")
# is_adult = age >= 18
# print(f"Adult status: {is_adult}")


# F. Mini-Project: CLI Unit Converter
    # Problem Statement
    # Build a command-line tool that converts between common units of measurement. The program should display a menu, perform the selected conversion, and loop until the user chooses to quit.
    # Menu Options
    # Celsius → Fahrenheit
    # Fahrenheit → Celsius
    # Kilometers → Miles
    # Miles → Kilometers
    # Kilograms → Pounds
    # Pounds → Kilograms
    # Quit
    # Requirements
    # Display the menu with numbered options.
    # Ask the user to select an option by typing a number.
    # Ask for the value to convert.
    # Display the result rounded to 2 decimal places, including the unit.
    # After each conversion, loop back to the menu.
    # Exit cleanly when the user selects option 7.
    # Formulas
    # Fahrenheit = Celsius × 9/5 + 32
    # Celsius = (Fahrenheit − 32) × 5/9
    # 1 kilometer ≈ 0.621371 miles
    # 1 mile ≈ 1.60934 kilometers
    # 1 kilogram ≈ 2.20462 pounds
    # 1 pound ≈ 0.453592 kilograms
    # Constraints
    # Use only Python built-in features. No imports.
    # Use while, if/elif/else, input(), print(), and f-strings.
    # Handle invalid menu choices (e.g., user types 9) by printing an error message and re-displaying the menu.
    # Acceptance Criteria
    #  The program runs without errors.
    #  All six conversions produce mathematically correct results.
    #  The menu loops until the user selects Quit.
    #  The output is formatted clearly with units and 2 decimal places.
    #  Invalid menu choices are handled gracefully.
    # Stretch Goal (Optional)
    # Handle non-numeric input for the value to convert without crashing. Hint: This requires try/except, which we cover on Day 2. If you do not know it yet, skip this stretch goal.

input_list = """
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Kilometers → Miles
4. Miles → Kilometers
5. Kilograms → Pounds
6. Pounds → Kilograms
7. Quit
"""

### FORMULAS
# Fahrenheit = Celsius × 9/5 + 32
# Celsius = (Fahrenheit − 32) × 5/9
# 1 kilometer ≈ 0.621371 miles
# 1 mile ≈ 1.60934 kilometers
# 1 kilogram ≈ 2.20462 pounds
# 1 pound ≈ 0.453592 kilograms
###
print(input_list)

while True:
    user_input = int(input("Select any one from the list: "))

    if(user_input == 7) :
        print("exiting code!!")
        break
    if user_input < 1 or user_input > 7:
        print("Invalid choice. Please select 1 to 7.")
        continue

    user_value = float(input("Provide value to convert: "))

    if(user_input == 1):
        fahrenheit = (user_value) * 9/5 + 32
        print(f"{user_value}°C = {fahrenheit:.2f}°F")
    elif (user_input == 2):
        celsius = (user_value - 32) * 5/9
        print(f"{user_value}°F = {celsius:.2f}°C")
    elif (user_input == 3):
        kilometer = 0.621371 * user_value
        print(f"{user_value} km = {kilometer:.2f} miles")
    elif (user_input == 4):
        mile = 1.60934 * user_value
        print(f"{user_value} miles = {mile:.2f} km")
    elif (user_input == 5):
        kilogram = 2.20462 * user_value
        print(f"{user_value} kg = {kilogram:.2f} pounds")
    elif (user_input == 6):
        pound = 0.453592 * user_value
        print(f"{user_value} pounds = {pound:.2f} kg")


