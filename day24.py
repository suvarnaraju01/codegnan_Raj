'''
Encapsulation:
'''
'''class BankAC:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
Acc = BankAC(15000)
Acc.deposite(7000)
print(Acc.get_balance( ))'''

'''
Inheritance : this allows child class which is also sub class that Acquire the properties(attributes,methods)
of a parent class (base class,super class ).

1.single - A class inherits from only one base class.'''
'''
class parent:
    def display(self):
        print("this is a parent method")
class child(parent):
    def display(self):
        super( ).display( )
obj = child( )
obj.display( )
'''

'''
2.miltiple - class inherits properties from more than one base class.
'''
class Father:
    def skill_1(self):
        print("Father :hard working")
class Mother:
    def skill_2(self):
        print("mother:cooking")
class child(Father,Mother):
    def All_skills(self):
        print("child:Coding")
ANY = child( )
ANY.skill_1( )
ANY.skill_2( )
ANY.All_skills( )

'''
super( ): is used to call methods or constructors of the parent class from the child class.
'''
'''
class parent:
    def display(self):
        print("this is a parent method")
class child(parent):
    def display(self):
        super( ).display( )
obj = child( )
obj.display( )
'''
