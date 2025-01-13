# Create a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Orange"]

# Access elements using indexing
print("Accessing elements using indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

# Modify elements in the list
fruits[1] = "Kiwies"
print("\nModified list after changing second fruit:")
print(fruits)

# Add elements to the list
fruits.append("Watermelon")
print("\nModified list after adding 'Watermelon':")
print(fruits)

# Remove elements from the list
fruits.remove("Watermelon")
print("\nModified list after removing 'Watermelon':")
print(fruits)

# Find the length of the list
length = len(fruits)
print("\nLength of the list:", length)

# Sort the list in ascending order
fruits.sort()
print("\nSorted fruits list (ascending):")
print(fruits)

# Sort the list in descending order
fruits.sort(reverse=True)
print("\nSorted fruits list (descending):")
print(fruits)
