a=5
#print(b)#NameError: name 'b' is not defined
for j in range (1,10,2):
    print(j) #if u print b and j for b is show name error bcoz we never called b but after for j is initial variable
#range ( ) - used to  generate number
#syntax - range(start,end,step)   step is optional, actually step is used for  skip the number
#for s in range(2,30,5):
  #  print(j)
    '''
any = "abc"
print(list(any))
print(tuple(any))


so = 123
vs = (str(so))
print(str(so))
print(float(123))
      

an = 123
print(str(an))
print(tuple(an))

a=[(1,2),(2,4)]
print(dict(a)) '''
rev_str = "raju"
print(rev_str[::-1])
#program for palindrome
a = "madam"
empty=""
for j in a:
    empty = j + empty
if empty == rev_str:
    print(f"{rev_str}  is palindrome")
else:
    print(f"{rev_str}  not a palindrome")
        
#program for generating even numbers
for a in range(1,100):
    if a %2 == 0:
        print(f"{a} is even number")
    else:
        print(f"{a} id odd number")

        
