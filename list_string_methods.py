'''# Original list with different data types
my_list = [10, "hello", 3.5, True, [1, 2], (5, 6)]
print("Original List:", my_list)

# Taking a new list (copy)
new_list = my_list.copy()
print("Copied List:", new_list)

# 1. append()
new_list.append("new_item")
print("\nAfter append:", new_list)

# 2. extend()
new_list.extend([100, 200])
print("After extend:", new_list)

# 3. insert()
new_list.insert(2, "inserted")
print("After insert:", new_list)

# 4. remove()
new_list.remove("hello")
print("After remove:", new_list)

# 5. pop()
removed_item = new_list.pop()
print("After pop:", new_list)
print("Popped item:", removed_item)

# 6. index()
print("Index of 10:", new_list.index(10))

# 7. count()
print("Count of True:", new_list.count(True))

# 8. reverse()
new_list.reverse()
print("After reverse:", new_list)

# 9. copy()
another_list = new_list.copy()
print("Another copied list:", another_list)

# 10. clear()
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear:", temp_list)

# 11. sort() (works only with same data types)
num_list = [5, 2, 9, 1]
num_list.sort()
print("Sorted list:", num_list)
'''
#strings
# Original string with mixed content
my_string = "Hello Python 123"
print("Original String:", my_string)

# 1. upper()
print("\nUpper:", my_string.upper())

# 2. lower()
print("Lower:", my_string.lower())

# 3. title()
print("Title:", my_string.title())

# 4. capitalize()
print("Capitalize:", my_string.capitalize())

# 5. swapcase()
print("Swapcase:", my_string.swapcase())

# 6. find()
print("Find 'Python':", my_string.find("Python"))

# 7. index()
print("Index 'Hello':", my_string.index("Hello"))

# 8. replace()
print("Replace:", my_string.replace("Python", "Java"))

# 9. split()
print("Split:", my_string.split())

# 10. join()
words = ["I", "love", "Python"]
print("Join:", " ".join(words))

# 11. startswith()
print("Starts with 'Hello':", my_string.startswith("Hello"))

# 12. endswith()
print("Ends with '123':", my_string.endswith("123"))

# 13. count()
print("Count of 'o':", my_string.count("o"))

# 14. strip()
str_with_spaces = "  hi  "
print("Strip:", str_with_spaces.strip())

# 15. lstrip()
print("Lstrip:", str_with_spaces.lstrip())

# 16. rstrip()
print("Rstrip:", str_with_spaces.rstrip())

# 17. isalpha()
print("Isalpha:", "Hello".isalpha())

# 18. isdigit()
print("Isdigit:", "123".isdigit())

# 19. isalnum()
print("Isalnum:", "Hello123".isalnum())

# 20. isspace()
print("Isspace:", "   ".isspace())
