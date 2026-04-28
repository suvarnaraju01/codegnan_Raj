'''
Regular Expression(RsgEx) :

7.? - This is  meta charecter will form a searching pattern as it
         will take any zero or one charecter for(?)
syntax - re.finadall(".?".variable_name)

import re
any = "This function is used to find all the  sequence of charecters in the string "
so = re.findall("Th.?",any) #?metacharecter
an = re.search("T.?",any) 
print(so,an)

8. { } -  This is meta charecter will form a searching pattern as we mention the size in the { }
syntax - re.search(".{size}",variable)

import re
any = "This function is used to find all the  sequence of charecters in the string"
an = re.findall(".{22}", any)
print(an)

9.  | - this meta charecter will form a searching pattern as it consider right and left
         any string is present or not for(|)

import re
any = "This function is used to find all the  sequence of charecters in the string"
an = re.findall("that|This", any)
print(an)
--------------------------------------------------------------------------------------------------------------------

Special Sequence - A special sequence is a \ followed by one of the charecter in the list below ,
and has a
special meaning:
1.\A - Returns a match  if the specified charecter are at the beginning of the string
Eg: "\AThe

import re
txt = "The rain in spain"
#check if the string  start with "The":
x = re.findall("\AThe",txt)
print(x)
if x:
    print("yes, there is a match !")
else:
    print("no match")

2. \b - return  a match  where  the  specified charecter are at the biginning  or
at the  end of the word.
Ex: r"\bain" 

import re
txt = " The rain Spain"
#Check if " is present at the beginning of a word:
x = re.findall("\bSpain",txt)
print(x)
if x:
    print("yes, there is at least one match !")
else:
    print("no match")

3. \d - returns a match  where the string contains digits (number from0-9)
Eg: "\d" 

import re
txt = " The rain  in 56 Spain"
#Check if  the string contains any digits (number from 0-9):
x = re.findall("\d",txt)
print(x)
if x:
    print("yes, there is at least one match !")
else:
    print("no match")

4.D - return a match where  the string does not contain  digits
Eg: "\D" 
import re
txt = "The rain  in 67 Spain"
#Check if  the string contains any digits (number from 0-9):
x = re.findall("\D",txt)
print(x)
if x:
    print("yes, there is at least one match !")
else:
    print("no match")
5.\s - return a match where  the string contain  a white space charecter
Eg: "\s" 
import re
txt = "The rain  in Spain"
#Check if  the string contains any digits (number from 0-9):
x = re.findall("\s",txt)
print(x)
if x:
    print("yes, there is at least one match !")
else:
    print("no match")

    
6. \S - return a match where  the string  DOES NOT  contain a white space charecter
Eg: "\S" 
import re
txt = "The rain  in Spain"
#Return a match at every NON white-space charecter:
x = re.findall("\S",txt)
print(x)
if x:
    print("yes, there is at least one match !")
else:
    print("no match")
==========================================================================
Time and Date :
---------------------
%d - day
%m - month
%Y -  year 
%H - hour
%M - min
%S - sec
%p - am/pm
%A  -day name
%B - month name

import datetime
today = datetime.datetime.today( )
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%H-%M-%S,%p"))
print(today.strftime("%A"))
print(today.strftime("%B"))'''

import re

# Input
name = input("Enter your name: ")

# Phone number validation
while True:
    phno = input("Enter phone number: ")
    if re.fullmatch(r"\d{10}", phno):
        break
    else:
        print("Invalid phone number! Must be exactly 10 digits.")

# Email validation
while True:
    email = input("Enter email id: ")
    if re.fullmatch(r"[a-zA-Z0-9._%+-]+@gmail\.com", email):
        break
    else:
        print("Invalid email! Must end with @gmail.com")

# Password validation
password = input("Set password: ")
confirm_password = input("Confirm password: ")

while password != confirm_password:
    print("Passwords do not match! Try again.")
    password = input("Set password: ")
    confirm_password = input("Confirm password: ")

# Final Output
print("\n--- User Details ---")
print("Name:", name)
print("Phone:", phno)
print("Email:", email)
print("Password set successfully!")



