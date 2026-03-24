''' strings-- this is a sequence of charecters /collection of charecters , which represented by double quotes(" ") or single('  ') quotes
and  we can acess using indexing '''
'''
any="python programming"
print(any[2]) #TypeError: string indices must be integers, not 'tuple'-[2,3,4]
#slicing-
print(any[7:12])
print(any[0:14])
print(any[3:17])
print(any[4:9])


print(any.replace("python","java"))
print(any[-5])
#so=any.repalce("python","java")
#print(so) - i couldnt able to modify on that paticular variable.... becoz its immutable
print(any[29]) #string can allow neg indexing, cant access out of range
'''

'''
day_5 = "I'm Raj from Akp , completed PG in NIST college "
print(f"my name is {day_5[4:8]}")
print(f"my name is {day_5[-9:-8]}")
print(f"{day_5[::-1]}")
print(len(day_5))#len-len() method is used to  get char present in the string or find the length of the string
some="234"#Note:-we can convert a strings into integer , if  it contain only integer values.....
# some="234p" invalid literal for int() with base 10: '234p'
num=int(some)
print(type(num))
'''

#methods of strings:
#1.split() - remove space / separate  words using single quote
#ex:['python', 'is', 'a', 'programming', 'language']
#syntax : variable_name.split method ("substring")
some="python is a programming language"
print(some.split("  "))
print(some.split(  ))
print(some.split("programming "))
print(some.split("python"))

 #2.lower() - it convert  into lower case/ small letters
#syntax : variable_name.lower method ("substring")
some="python is a programming language"
print(some.lower(  ))

#3.upper() - it convert into upper case/capital letters
#syntax : variable_name.upper method ("substring")
print(some.upper(  ))

#4.replace() -used to replace old string with new string.
#syntax :  variable_name.replace method ("old string","new string")
some="python is a programming language"
print(some.replace("pragramming","normal"  ))


some="python is a programming language"
if "python"in some:
    print("yes")
else:
    print("no")
