'''
recursive function -A function that calls itself again andagain until a condition is met.
A recursive function is a function that solves a problem by breaking it into smaller parts and
calling itself. '''

def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("enter 4 digit pin: ")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("welcome to the ATM")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f" invalid pin .attempts left:{self.ramaining_attempts}")
            else:
                print("card blocked.please contact customer care")
                return False


#prime number
prime_num = 7
count = 0
def prime_check(prime_num,k):
    for j in range(1,prime_num+1):
        if prime_num % j == 0 :
            k += 1
    if k== 2:
        print("prime")
    else:
        print("not prime")
prime_check(prime_num,count)
           
#palindrome
palindrome = input("enter word:   ")
def is_palindrome(s):
    if palindrome == palindrome[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
is_palindrome(palindrome)



#even number
even= int(input("enter num:   "))
def is_even(s):
    if even %2==0:
        print("even number")
    else:
        print("not even number")
is_even(even)



def vowels_consonents(raj,vowels_list,consonents_list ):
    for j in raj :
        if j in "AEIOUaeiou":
            vowels_list.append(j)
        else:
            consonents_list.append(j)
    print(f"{vowels_list} these are all vowels in the string,{consonents_list} these are consonents in the string")
vowels_consonents(raj =input("enter data"),consonents_list = [ ], vowels_list = [ ])


