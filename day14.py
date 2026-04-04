#Fibonacci - Fibonacci series lo next number = previous two numbers sum
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    
#Armstrong - 3 digits unnayi kabatti each digit power 3

n = 153
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit**3
    n = n // 10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")

#Factorial Using Loop
    n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print(fact)

#Perfect Number
n = 6
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect number")
else:
    print("Not perfect")
