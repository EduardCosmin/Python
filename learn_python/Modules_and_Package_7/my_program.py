#Example how to import from a module

from my_module import my_func   
my_func()

#Example how to import from a Package:

from MyMainPackage import some_main_script  #import from a main package
from MyMainPackage.SubPackage import  my_sub_script  #import from a sub package

some_main_script.report_main()

my_sub_script.sub_report()