def get_number(position):
    number = input(f"Enter the {position} number: ")
    return number

def get_first_number():
    return get_number("first")

def get_second_number():
    return get_number("second")

def get_operation():
    operation = input("Choose the operation (+, -, /, *): ")
    return operation

def validate_number(number, position):
    if(number.isdigit()):
       pass
    
    else:
        print(f"The {position} Number entered is not a digit, all numbers must be digits")
        return

def validate_operation_symbol(operand):
    if(operand == "+" or operand == "-" or operand == "*" or operand == "/"):
        pass
    else:
        print("You must enter an operand")
        return

