# Display a menu with 7 options: Add, Subtract, Multiply, Divide, Floor Divide, Modulo, Power, and Exit
# Ask the user to choose an operation by number
# Ask the user for two numbers (handle the case where they type text instead of numbers — print an error and ask again)
# Perform the calculation and display the result using an f-string
# Store every calculation in a list called history as a formatted string (e.g., "5 + 3 = 8")
# Add an option to view the history — print all previous calculations
# The program keeps running until the user chooses Exit
# Handle division by zero — print a clear error message instead of crashing

menu_options = '''
Select any options from menu,
1. +
2. -
3. X
4. /
5. //
6. %
7. ^
8. View History
9. Exit
'''
history = []
while(True):
    try:
        user_option = int(input(f"{menu_options} : ",))
        if(user_option == 9):
            break
        if(user_option == 8):
            if history:
                print("\n--- Calculation History ---")
                for item in history:
                    print(item)
            else:
                print("No calculation history available.")
            continue
        if(user_option > 9 or user_option < 1) :
            print("Select from the options")
            continue
        input1 = int(input(f"Select number 1 : "))
        input2 = int(input(f"Select number 2 : "))
        
        match user_option:
            case 1:
                res =  input1 + input2
                history.append(f"{input1} + {input2} = {res}")
                print(res)
            case 2:
                res =  input1 - input2
                history.append(f"{input1} - {input2} = {res}")
                print(res)
            case 3:
                res =  input1 * input2
                history.append(f"{input1} * {input2} = {res}")
                print(res)
            case 4:
                res =  input1 / input2
                history.append(f"{input1} / {input2} = {res}")
                print(res)
            case 5:
                res =  input1 // input2
                history.append(f"{input1} // {input2} = {res}")
                print(res)
            case 6:
                res =  input1 % input2
                history.append(f"{input1} % {input2} = {res}")
                print(res)
            case 7:
                res =  input1 ** input2
                history.append(f"{input1} ^ {input2} = {res}")
                print(res)
    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")   

    except Exception as e:
        print(e)
    