#perfect number
num = int(input("Enter number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect")

#check anagram
s1 = input("Enter string1: ")
s2 = input("Enter string2: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#multiplication table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
