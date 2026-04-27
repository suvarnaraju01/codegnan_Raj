'''
File handling :
    file handler is a object is to maintain several functions of file such as creating,
    reading,writing, updating and also deleting the file.
'''
  '''  
How  to open a file:
 1.open( ) - this open function  takes 2 parameters and in this we have to
 close the file  by calling close ()  function  at end of the program
    a.file name
    b.mode - Modes("r","w","a","x","t")'''
# "r" -- (read) to read the file we will  use  this mode and if the file doesnt exist it.

any = open("demo.txt","r")
print(any.read( ))
any.close( )

#"w"--(write) To write  the text into  the file we will use  this mode and it will create
              the file if the file doesnt exist, it will overide  the data in it .
any = open("demo.txt","w")
print(any.write( ))
any.close( )

#"a" --(append)  to add the text  into the file  , it also create a file if it doesnt exist.
any = open("demo.txt","a")
print(any.write( ))
any.close( )

#"x" --(create) used to create anew file
any = open("demo.txt","x")
print(any.write( ))
any.close( )

'''
To read a file :
1.read( ) -  This method is used to read entire file chunk by chunk  ,even space 
2.realine( ) - This only read  1st line or one line
3readlines( ) -  This method can read the entire  file and return into list with  each line  is one
                         index in the list.

''any = open("demo.txt","r")
print(any.read( ))
any.close( )
'''



2.with open ( ) -to write the text into the file we will  use this mode and it will create the
file  if it  doesn't  exist.

    +
    
with open ("demo.txt","r")as any:
    print(any.read( ))
