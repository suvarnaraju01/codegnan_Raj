#practice questions
print("Hello, World!")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)
#example questions
l = float(input("Enter length: "))
w = float(input("Enter width: "))
area = l * w
print("Area:", area)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name + "! You are", age, "years old.")


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum:", max(nums))
print("Minimum:", min(nums))



s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
ci = p * (1 + r/100) ** t
print("Compound Interest:", ci)


days = int(input("Enter number of days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7
print("Years:", years)
print("Weeks:", weeks)
print("Days:", remaining_days)



nums = list(map(int, input("Enter numbers: ").split()))
sum_pos = sum(x for x in nums if x > 0)
print("Sum of positive numbers:", sum_pos)



sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count:", len(words))


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
