#CONCATINATION - act as addition  for the integers
#case-2 for other data types ( we have to use same data types)then this + symbol
# act as concatination operator
#notice -  coudnt able to concatinate 2 diff datatypes like string and integer.
#can only concatinate str to str , int to int .


print(9+8)
print("python "+"programming"+ "language")
print([1,2]+[3,4])

print([3,4]+9) # TypeError: can only concatenate list (not "int") to list

print(9+"programming"+ "language") # TypeError: unsupported operand type(s) for +: 'int' and 'str'


#TUPLE - mixture of diff datatypes and it is represented by ( ) , separated by ,
thing = (1,"teja",[12.4],(6,7))
thing = (12,18,"python",(23,"raju",[67,"python is a programming language",(7,8)],[8,"python",[34,9]]))
print(thing)
# print space between is and a?
3*+



num=2
num2=4
print(f"before swapping num={num} and num2={num2}")
num,num2=num2,num
print(f"after swapping num={num} and num2={num2}")
'''
leap_year = int(input("enter number:"))
if(leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0: 
  print(f" yes ,  {leap_year} is a leap year ")
else:
  print(f"no , {leap_year} is not leap year")
