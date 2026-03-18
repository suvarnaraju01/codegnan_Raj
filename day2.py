'''
varaibles--> variable is basically named storage loacation that is used
data in the memory, to make it simple it is the label which points
out to a value -->storage placeholders

rules for defining variables
--> variables can store A-Z,a-z,0-9
-->varibles start with uppercase,lowercase letters even with underscore
-->but you cant start with symbols(@#$.....),even number also

better preferable way is go with general purpose--> you want to store your details name, email_id,account_number..

'''
'''
a=1
b=5
a=25
#python is dynamically typed, you need not define the datatype and also
#only the recent values to the variables with same name is pointed


print(a)
print(b)

#1a23 = 25  #syntax error

#@werf = 4.5  #syntax error

#$dsf = 12 #invalid syntax
#store your personal details

name = "raju"
location ="vishakapatnam"
age = 23
emailid = "vsuvarnaraju01@gmail.com"
email_id = "vsuvarnaraju01@gmail.com"
print(name,location,age, email_id)



# how to assign multiple value to a variables
raju,kartheek,shyam = 23,21,21
print(raju)
print(kartheek)
print(shyam)

#if u want to assign same valuesto multiple variables
X=Y=Z=21
print(X,Y,Z)
#keywords or reserved words, which has specific usage
#there are 35 keywords
#never use keywords as identifiers

#if = 23
#lambda = 'raju'
#FALSE = 0 # cant assign

#python is case sensitive
false = 22

#identifiers are  names given to variables, funtions,classes,objects....

#literals are fixed values to a identifiers
name=25

#name is identifiers,25 is literal
# single line comments --> #
#multiple line comments --> start  with   end with 3 invited coma
# numeric datatype-->int,float,complex
#int -->count,values,quatities
#float-->temperature, percentage,price
#complex-->specific conversions (real and immaginary)
#implicit as python follows dynamic type
count = 25
print(count)
print(type(count))

price = 125.5
print(price)
print(type(price))

j3 = 23
value = 2+j3
print(value)
print(type(value))

value = 2+3j
print(value)
print(type(value))

#typecasting--> converting onr type to another

#int-->float,complex

age = 25
print(type(age))

b = float(age)
print(b)
print(type(b))
c = complex(age)
print(c)
print(type(c))

#float,complex
price= 12.5
print(type(price))
d= int(price)
print(d)
print(type(d))
e=complex(price)
print(e)

f=2+5j
print(type(f))
#g = int (f) #complex to int is not possible
#print(g)
h= float (f) #complex to float is not possible
print(h)
'''

'''
#boolean datatype-->validation -->true/false
a=True
print(a)
print(type(a))

#typeconversation of bool
b=int(a)
print(b)
c=float(a)
print(c)
d=complex(float(int(False)))
print(d)
'''

'''
#input --> input ()/ outout -->print()
a= 23
print (a)
'''

'''
a=input("enter a value")
print (a)
print(type(a))

a=int(input("enter a value:"))  #only integer input
print(a)
print(type(a))

a=float(input("enter a value:"))  #only integer input
print(a)
print(type(a))
'''

#now lets work on a simple case study using above -->fee calculator

#details of the student
name = input(" enter  your name")
print("-------")
admission_fees = int(input("enter admission fees"))
tuition_fees=float(input("enter tuition fees"))
hostel_fees=float(input("enter hostel fees"))
#calculate th etotal fees
total_fees= admission_fees+ tuition_fees+ hostel_fees
print(" *********** ")
print("your name ",name)
print("admission _fees ",admission_fees)
print(" tuition _fees ",tuition_fees)
print(" hostel_fees ",hostel_fees )
print(" total fees ",total_fees)
print("****************")
