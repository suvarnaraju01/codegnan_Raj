'''
Regular Expression(RsgEx) :
------------------------------------
This regular expression or RegEx is a sequence of charecters that forms a  searching pattern .
To use this we have to import re ,which will unlock the package.

Functions:
--------------
1.Findall - This function is used to find all the  sequence of charecters in the string.
syntax - re.findall( metachar,variable_name ).

2.Search - by using this u can find only 1st sequence in the string.
syntax - re.search ("matachar",variable_name).

import re
any = "python is  a language" 
so = re.findall( "a",any )
an = re.search("a"any)
print(so)

Metacharecters -  are used to form searching pattern.
---------------------
1.[ ] - in this we can search for [a-z],[A-Z],[0-9]
import re
any = "This function is us2ed to find al1l the  seque9nce of charecters in the string "
so = re.findall("[0-9a-z]",any) #[ ]metacharecter
an = re.search("[a-z]",any) 
print(so,an)

2.   . - This will form a searching pattern as it will take any single charecter for .   .
import re
we = "hello"
the = re.findall("h....o",we)
thing = re.search("he..o",we) #  .  metacharecter
print(the)
print(thing)

3. ^ - this is used to  find the  string is starting with the sequence or not.
syntax - re.findall("matachar",variable_name)
import re
any = "This function is used to find all the  sequence of charecters in the string "
so = re.findall("^This ",any) #^metacharecter
an = re.search("^This",any) 
print(so,an)

4.$ -  This is used to find the string is ending  with the sequence or not.
syntax - re.findall("$",variable_name)
import re
any = "This function is used to find all the  sequence of charecters in the string "
so = re.findall("string $",any) #$metacharecter
an = re.search("are $",any) 
print(so,an)

5.* -  This is used to find charecter  will form a searching pattern as it will take any zero
        or more charecter for *.
syntax - re.findall("
import re
any = "This function is used to find all the  sequence of charecters in the string "
so = re.findall("Th.*r",any) #*metacharecter
an = re.search("T.*",any) 
print(so,an)


6. + -  This is used to find charecter  will form a searching pattern as it will take any one
or more  charecter for + .
syntax - re.search(".+",variable_name)'''

import re
any = "This function is used to find all the  sequence of charecters in the string "
so = re.findall("an.+g",any) #^metacharecter
an = re.search("T.+",any) 
print(so,an)





