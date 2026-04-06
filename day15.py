'''
Funtions  it is a block of code ,which is reusable .These are  2 types
 1. Built-in/In-built
 2.user define
 
 1.In-built - it they comes with the program itself,those are already defined....
 eg : print( ), sum ( ),map (  ).....
 
 2. User defined - this is created by user( developer, person using for development ).
 
 Note: start with def keyword,
           followed by func name.
           it has calling funtion

           def fun_name( a,b):  #a,b are parameters
              -------
               -----
                ----
           fun_name( ) #arguments
'''
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
