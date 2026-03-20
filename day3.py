'''
#operators, different type of operations , conditional statements-->if , ifelse , else ,nested if
operators= an operator is asymbol that perform an operation on one or more values (operands) and produces a result

operators are primarily used :
-->calculate values
-->compare values/ inputs
-->make decisions
-->control the program flow

 there  are main seven main categories in python
 -->arthemetic
 -->assignment
 -->comparision
 -->membership( in, not  in)
 -->identity(is , is not)
 -->bitwise
 -->logical (and, or ,not)
 '''
'''
#arthematic operators - it perform mathematical operations + addition ,- subtraction ,* multiplication , /division ,** exponent ,% modulus , // integer division
a=5
b=3
print(a+b)
print(a*b)
print(a-b)
print(a/b)#return in float values
print(a**b) #return exponential value
print(a%b)#modulus division -returns remainder
print(a//b)# flooring division / integer division-return quotient ,discards  float value

#f string notation
num1=int(input("enter the first value"))
num2= float(input("enter the second value"))
result=(num1+num2)*4
print(" the result is ",result) # standard notations
#f- string notation
print(f" the result is {result, num1, num2}")
print(f" the result is {result, num1, num2,(result* num1)}")

'''
'''
 #assignment operators --->= assign ,+= addition assignment ,-= subtract assignment ,*= , /= , %= , //= , **= .
#they are majorly used for  code repetation in application usage
a=3
b=2
a+=2# a= a+2
print(a)
b+=a
print(b)
b-=a
print(b)
b*=a
print(b)
b//=a
print(b)
b%= a
print(b)
b**= a
print(b)
'''

'''
#relational or comparision operator --> they always return the boolean values
#values(true / false)

#--  is equal to ,!= not equal to
#<less than , > greter than, <=, >=

a=int(input(" enter value"))
b=int(input(" enter another value"))
print(a==b)
print(a!=b)
print(a<b)
print(a > b)
print(a<=b)
print(a>=b)

'''

'''
# membership operator --> they are used to ckeck existance of an object  in a collection -->in, not in
a= "codegnan"
print(type(a))
print("a" in a)
print("s" in a)
print( "3" in "2344")
b=[12,3,4,5]
c=int(input("enter the value"))
print(c)
print(c in b)
print(c not in b )

# logical operators-->they are used to combine multiple conditions(and ,or, not)
age=int(input("enter the value"))
vote_right=True
print(age>=18 and vote_right) # both condition should be true
print(age>18 or  vote_right)
print(not vote_right)
'''
#identify operators--> they check the memory location and validate  we used
#(id) function it is different from == operator->  is , is not

a=[1,2,4]
b=[1,2,4]
print(a==b)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

#bitwise -->bitwise     AND  & , OR | perform bitwise  operator
#we get the result ( remember the  binary conversation)
print(5 & 3)
print(bin(5))# bin  return binary number

#Task --> Now you have all operators create a Checker Task
#git add .
#git commit -m"operators usage"
#git push -u origin main 

