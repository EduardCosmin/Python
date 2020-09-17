Steps to use unit testing (python)

1.Create a file and write down some code and save it        
2.Create another file with the same extension and save it  
3.In the second file import at the begining unittest 
and the name of the function/s that you had created at 
point 1 that you want to test.
4.Create a class where you inherit between paranthesis
'unittest.TescCase'
5.Write down one(or more) function(s) about what you want
to test.
6.(Optional) After that you finished your test function
write down outside the class:
"if __name__=='__main__':
    unittest.main()"
7.Open cmd where you have located the files and type:
python 'name_of_the_test_file'.extension

Example:
First file: function.py
Second file: test_function.py
In cmd: python test_function.py