#required arguments - it should match exact same number of varibles in calling with def
'''
num = 8
num_2 = 10
def add(num,num_2):
    print(num+num_2)
    print(num)
add(num,num_2)          

my_name = "raj"
def add(my_name):
    print(my_name)
add(my_name = "vardhanapu")
add(my_name ="suvarna")
add(my_name ="raju")
#Note:calling fun use chesi enni lines turvata ayna use chesi call cheyochu 

#default argument  - it take default values  from the arguments even thou if assign values before.
#prime number
def prime_check(prime_num,count):
    for j in range(1,prime_num+1):
        if prime_num % j == 0 :
            count += 1
    if count == 2:
        print(f"{prime_num} is prime")
    else:
        print(f"{prime_num} not prime")
prime_check(prime_num = int(input("enter number")),count = 0)
prime_check(prime_num = 9,count = 0)
prime_check(prime_num = 11,count = 0)
prime_check(prime_num = 13,count = 0)#key word arguments - as like dictionary here we have key and values directly in the arguments
'''
'''#Ex - 2
def raj(b,c,a):
    print(f"a={a},b={b},c={c}" )
raj(a=2,b=3,c=4)#even thou places of arguments and parameters are diff ,values of variable are same so no problem '''

'''#count of words in sentence
def word_count(sentence ):
    words = sentence.split()
    count = len(words)
    print("Number of words:", count)
word_count(sentence = input("Enter a sentence: "))'''

'''variable length argument:
----------------------------------
addinga star (*) before the parameters name in the function ,recive a tuple of arguments and can acess items with indexs'''
P=int(input("enter principle value"))
R=float(input("enter  rate of intrest value"))
T=float(input("enter time period"))
A= " "
CI=" "
def compound_intrest(A,CI):
    A=P(1+R/100)^T
    CI=A-P
    print("compound intrest is" ,CI)
compound_intrest(A, CI )
