'''
Lambda Funtion:
-----------------------
        Also called anonymous function.
        it can take  n number of arguments but have only one expression
syntax:
         lambda (keyword) arguments : expression


any = lambda so : so +12
print(any(12))

any = lambda a , b, c:a+b+c
print(any(int(input("enter first number ")),int(input("enter first number ")),int(input("enter first number "))))


List Comprehension:
---------------------------
    This offers the shorter syntax when you want to create a new list from existing list.
    Syntax:
             variable_name = [expression loop and condition]
'''
raj=[1,2,3,4,5]
ansh=[j for j in raj if j%2==0]
print(ansh)
    
