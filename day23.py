'''
constructor(__init__)
----------------------------
-->A constructor is a special method ,that used  to initialized object data.
A constructor is a special method that is automatically called when an object is created.
__init__( )'''


'''
class student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    def display(self):
        print(self.name,self.ID)
stu_1 = student("teja",123)
stu_1.display( )
'''

'''
Access Specifiers :
------------------------
Access specifiers control visibility of variables and methods
1.public - Accessible from anywhere
2.protected - Meant for internal use (convention) ,
                      Can still be accessed outside (not strict)
3.private - More restricted using name mangling

self ---> this is a keyword is instance variable and unique for each object
----
                  Summary Table
                 ---------------------
  Type           Syntax                          Access Level
  ------        ------------                         -----------------
Public	         var                        	Anywhere
Protected       _var	                              Internal use (convention)
Private	     __var                             Restricted (name mangling)
'''
class some:
    def  __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private="private"
any = some ( )
print(any.public)
print(any.protected)
print(any.private)
        
