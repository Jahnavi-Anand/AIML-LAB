# Create a string variable
text = "Hello, welcome to the world of Python programming!"

# Find the length of the string
length_of_string = len(text)
print(f"Length of the string: {length_of_string}")

# Convert the string to uppercase
uppercase_string = text.upper()
print(f"Uppercase version: {uppercase_string}")

# Convert the string to lowercase
lowercase_string = text.lower()
print(f"Lowercase version: {lowercase_string}")

# Check if a substring exists in the string
substring = "Python"
is_substring_present = substring in text
print(f"Is '{substring}' present in the string? {is_substring_present}")

# Split the string into a list of words
words_list = text.split()
print(f"List of words: {words_list}")
