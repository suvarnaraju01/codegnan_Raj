'''
num = 5
for j in range (num) :
    for i in range(j):
        print("* ",end = " ")
    print( )    

num = 6
for j in range (num) :
    for i in range(j):
        print(j,end = " ")
    print( )

num = 7
for j in range (num) :
    for i in range(j):
        print(i,end = " ")
    print( )
    

num = 8
for j in range (num) :
    for i in range(num-j):
        print("*",end = " ")
    print( )


#pyramid 
num = int (input ("enter limit: "))
for j in range (num) :
    print(" " * (num - j) , end = " ")
    for j in range(j+1):
        print(" i ",end = "  ")
    print(  )
'''


    String--- [String is Immutable-can't be modified]
    String is a Sequences of charcaters that are encloseed in quotes ['',"",''' ''']
  Methods:
  Count ()   ,    capitalize ()
  Join  ()   ,    casefold ()
  strip ()   ,    isalnum ()
  replace () ,    isalpha()
  spilt () ,      isdigit()


SBI_RAJ = {"Name" : "RAJ",
                      "ATM PIN" : "2391",
                      "Balance":5000}
user_pin = input (" Enter Pin: ")
if len(user_pin) == 4:
    if user_pin in SBI_RAJ["ATM PIN"]:
        user_choice = int(input("enter\n1.withdraw: "))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw"))
            if money_w <= SBI_RAJ["Balance"]:
                SBI_RAJ["Balance"] -= money_w
                print ( SBI_RAJ["Balance"])
            else:
                print("Insufficient balance")
    else:
            print("You have enetered invalid pin")
else:
    print("Pls enter 4 digit pin")




    
    






  
