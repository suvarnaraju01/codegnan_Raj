'''
#program for prime number:
prime_no = int(input("enter a number"))
count = 0
for j in range(1,prime_no + 1):
    if prime_no % j == 0 :
        count += 1
        print(count)
if count == 2:
    print(f"{prime_no} is a prime number")
else:
    print(f"{prime_no}is not prime number")
'''
for an in range(2,100):
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count += 1
    if count == 2:
        print(f" {an} is a prime")
    else:
        print(f"{an} is not prime  ")          
