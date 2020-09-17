#Files

#In order to open a file from python comandline yo need to specify the full path but with double '\\' 
#or if your file is in the same directory with the .py file you can just call it by his name
my_file = open ('D:\\PROIECTE\\Python\\python_udemy\\object-and_data_structure\\text.txt')

#To read what is inside a file we can use .read() function
print(my_file.read())   #it will display as a single string separated with \n at the end of a line

#If you type again 'print(test.read())', you get '' because it was read before and now the cursor is at the end of your text file
print(my_file.read())

#In order read it again you need to type: test.seek(0) => your cursor is now at the begining of the file
my_file.seek(0)

#Now if you call .read() function again you will see the entire document 'print(test.read())'
print(my_file.read())

my_file.seek(0)
#If we want to separate all the lines inside a file we can type:
print(my_file.readlines())

#After that you finish to work with your file you have to close it
my_file.close()

#In order to open an external file you have to write the path to that file but with double '\\'
#my_file = open ("D:\\PROIECTE\\Python\\python_udemy\\object-and_data_structure\\text.txt")

#The next method will no longer need a file to be closed (it will do it automatically)
with open ('D:\\PROIECTE\\Python\\python_udemy\\object-and_data_structure\\text.txt') as my_new_file:
    contents=my_new_file.read()
    print(contents)

#Reading, Writing, Appending modes

#mode='r'  is read only
#mode='W'  is write only(will overwrite files or create new ones!)
#mode='a'  is append only(will add on to files)
#mode='r+' is reading and writing
#mode='w+' is writing and reading(overwrites existing files or creates a new file!)

#Read a file with mode=r
with open ('D:\\PROIECTE\\Python\\python_udemy\\object-and_data_structure\\text.txt','r') as f:
    print(f.read())

#Append to a file with mode=a  |  it will append to the file for each time that you will run the code until will be closed
with open ('D:\\PROIECTE\\Python\\python_udemy\\object-and_data_structure\\text.txt','a') as f:
    f.write('\nFourth line')      #after that you append something to the file you need to read it again as below
with open ('D:\\PROIECTE\\Python\\python_udemy\\object-and_data_structure\\text.txt','r') as f:
    print(f.read())

with open('test.txt','w') as f:
    f.write('New file')
with open('test.txt','r') as f:
    print(f.read())