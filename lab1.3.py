# Prompt the user to enter their name
name = input("Enter your name here: ")

# Greet the user using their name
greet = f"Hello, {name}! Nice to meet you !!"
print(greet)

# Prompt the user to enter their year of birth
dob = int(input("Enter your year of birth: "))

# Calculate the user's age based on the current year (2024)
current_year = 2024
age = current_year - dob

# Display the user's age
print(f"Currently, your age is: {age}")
