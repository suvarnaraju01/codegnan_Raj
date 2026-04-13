'''
Generator :
---------------
-->This is a special type of  function that return an ITERATOR which iterate one  at a time
'''
'''
def  raj_generator(  ) :
    yield 1
    yield 2
    yield 3
ansh = raj_generator(  )
print(next(ansh))
print(next(ansh))
print(next(ansh))


def square_gen(n):
    for i in range(n):
        yield i*i

for val in square_gen(5):
    print(val)
 '''      
'''
yeild :
-------
---it will take a pause again and again ,this is not a normal keword can not be used in the  nrml funtion.
---this is used to produce a value and pause execution.
'''
'''
def square_gen(n):
    for i in range(n):
        yield i**i ,i-i,i+i
 
for val in square_gen(5):
    print(val)
'''        
'''
next :
-------
----This is used to get next value from a generator
----when the value is finished ,it will stop the iterator
'''
'''
def  raj_generator(  ) :
    yield 1
    yield 2
    yield 3
ansh = raj_generator(  )
print(next(ansh))
print(next(ansh))
print(next(ansh))
'''
def square_gen(n):
    for i in range(n):
        yield i

for val in square_gen(100):
    print(val)
