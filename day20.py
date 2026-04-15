'''
Module :
-----------
  A module in Python is simply a file that contains Python code (functions, variables, classes)
  which can be reused in other programs.
  
🔹 Definition:
A module is a .py file that helps organize code and allows you to reuse functionality by
importing it into other Python programs.

🔹 Example:
Suppose you create a file named math_utils.py:

🔹 Key Points :
A module = Python file (.py)
Helps in code reuse
Improves code organization
Can be imported using import- keyword before the module.

🔹 Types of Modules
 ---------------------------
Built-in modules→A built-in module is a pre-defined module provided by Python
mthat can be used directly by importing it.
 ----------------------
🔹 Built-in Modules List :
 -------------------------------
math → Mathematical operations
random → Generate random numbers
datetime → Work with date and time
sys → System-related functions
os → Operating system interaction
time → Time-related functions
re → Regular expressions
json → JSON data handling
collections → Specialized data structures
itertools → Iteration tools
functools → Functional programming tools
string → String constants and utilities
heapq → Heap queue (priority queue)
bisect → Array bisection algorithms
copy → Copy objects
threading → Multithreading
multiprocessing → Parallel processing
subprocess → Run system commands
pickle → Object serialization
logging → Logging system

User-defined modules → created by you
 ----------------------------
syntax: keyword filename
              import ansh
            print(file name.functionality)
            print(ansh.add,sub etc)
Third-party modules → installed using pip (e.g., numpy)
 --------------------------
'''
'''
import Raj_ansh
print(Raj_ansh.add(2,4))
print(Raj_ansh.sub(2,4))
print(Raj_ansh.mul(2,4))
print(Raj_ansh.div(2,4))
'''

-'''
import day3
print(day3.ansh/2)
print(day3.ansh-2)
print(day3.ansh*2)
print(day3.ansh+2)
'''
'''
import math
print(math.sqrt(16))
'''
import random
num=random.randint(1,5)
i=0
while i<=3:
    g=int(input("guess:"))
    if g == num:
        print("correct")
        break
    else:
        print("try again")
    i+=1
print("number was:",num)
