
from utils import get_first_number, get_second_number, get_operation, validate_operation_symbol, validate_number

def do_the_math_for_me():
	first_number = get_first_number()
	second_number = get_second_number()
	operand = get_operation()

	validate_number(first_number, position="First")
	validate_number(second_number, position="Second")
	validate_operation_symbol(operand)


	if(operand == "+" and first_number.isdigit() and second_number.isdigit()):
		print(int(first_number) + int(second_number))

	if(operand == "-" and first_number.isdigit() and second_number.isdigit()):
		print(int(first_number) - int(second_number))

	if(operand == "*" and first_number.isdigit() and second_number.isdigit()):
		print(int(first_number) * int(second_number))

	if(operand == "/" and first_number.isdigit() and second_number.isdigit()):
		print(int(first_number) / int(second_number))

