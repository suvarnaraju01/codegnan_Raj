# we can store data  in  above format ---- "key":"value"
# keys are unique,immutable data types has to be used.
# represented by curly braces
#values we use all datatype elements
#methods
a={"raj":"ansh",
      "raj":"ansh" , #if  we have 2 same vlaues or duplicate values  it return single values in out put
   "Raj":"ansh",
   (4,7):0}
print(a)
print(a.keys( ))#keys( ) - used to get all the used keys in dict
print(a.values( ))#values - used to get all values of keys used in dict.
print(a.clear( ))#clear - used to clear data from dict
a.clear( )
print(a)



#sets - it is a unordered collection and it never allows duplicates
#methods - 1. union - for adding with out duplicates
a={1,2,3,4,2}
so = {4,5,6}
print(a.union(so))
#2. intersection - find the common  element from 2 sets
print(a.intersection(so))
#3.difference - common ga leni elements ni print cheztundhi
print(a.difference(so))
#4.remove - remove element from dataset
a.remove(3)
print(a)
#5. pop -

userdetails ={"name":"raj","pin":"2001"}
user_detail= input("enter your pin") 
if user_detail in userdetails["pin"]:
    print("valid")
else:
    print("ckeck your pin")
