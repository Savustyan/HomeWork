# PASSWORD VALIDATOR
import sys # NameError: name sys is not defined if not import
# Input
password: str = input('Input password: ')
# Logic
# Size
if (8 > len(password)) or (len(password) >= 128):
    print('Change password length')
    sys.exit(0)
# Capital letter
k: int = int(0)
for i in password:
    if i.isupper():
        k += 1
if k == 0:
    print('Use capital letter')
    sys.exit(0)
# lowercase letter
k: int = int(0)
for i in password:
    if i.islower():
        k += 1
if k == 0:
    print('Use lowercase letter')
    sys.exit(0)
# digit
k: int = int(0)
for i in password:
    if i.isdigit():
        k += 1
if k == 0:
    print('Use digit')
    sys.exit(0)
else:
    print('Your password is correct')
