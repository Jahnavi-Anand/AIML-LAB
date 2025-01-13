# Assign values to variables of different data types
integer = 10
floating = 50.0
string = "Hello"
boolean = True

# Perform arithmetic operations on numeric data types
addition = integer + floating
subtraction = integer - floating
multiplication = integer * floating
division = integer / floating if floating != 0 else "undefined (division by zero)"
modulus = integer % floating if floating != 0 else "undefined (modulus by zero)"

# Print arithmetic operation results
print(f"Addition: {integer} + {floating} = {addition}")
print(f"Subtraction: {integer} - {floating} = {subtraction}")
print(f"Multiplication: {integer} * {floating} = {multiplication}")
print(f"Division: {integer} / {floating} = {division}")
print(f"Modulus: {integer} % {floating} = {modulus}")

# Concatenate strings using the + operator
concatenated_string = string + " World !!"
print(f"Concatenated String: {concatenated_string}")

# Use logical operators to evaluate boolean expressions
and_op = boolean and False
or_op = boolean or False
not_op = not boolean

# Print logical operation results
print(f"Logical AND (True and False): {and_op}")
print(f"Logical OR (True or False): {or_op}")
print(f"Logical NOT (not True): {not_op}")
