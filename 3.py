# CALCULATOR
# input
first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')
import sys # NameError: name sys is not defined if not import
# if text in value
if (not first_value.isdigit()) or (not second_value.isdigit()):
    print(f'Value is not a digit')
    sys.exit(0)
# transformation to float
first_value: float = float(first_value)
second_value: float = float(second_value)
# output
if operation == '+':
    print(first_value+second_value)
elif operation == '-':
    print(first_value-second_value)
elif operation == '*':
    print(first_value*second_value)
elif operation == '/':
    print(first_value/second_value)
elif operation == '//':
    print(first_value//second_value)
elif operation == '**':
    print(first_value**second_value)
else:
    print(f'Invalid operation {operation}')
