#program for printing table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
print("---------------------------------")
#string methods
text = "Python Learning"

print(text.upper())        # Converts to uppercase
print(text.lower())        # Converts to lowercase
print(text.title())        # First letter capital
print(text.capitalize())   # First letter capital of sentence
print(text.swapcase())     # Changes upper to lower and lower to upper
print(text.replace("Python", "Java"))   # Replace word
print(text.find("Learn"))  # Find position
print(text.count("n"))     # Count characters
print(text.startswith("Py"))  # Check starting
print(text.endswith("ing"))   # Check ending
