import cs_test.feature

'''
First method: With functions
'''
'''
def my_procedure():
    print('This is my procedure!')

def my_procedure_2():
    some_parameter = 10
    print('This is my procedure NUMBER 2!')

    #NOTE: This is howto write print() similarly to Cpp
    print('Parameter is: %i' %some_parameter)

my_instance = cs_test.feature.FeatureCS()
my_instance.run_my_methods(my_procedure, my_procedure_2)
'''
'''
Second method: With class methods

#TODO: I believe I can rewrite method of class.. 
#TODO: !!OR ADD METHOD TO A CLASS on different page...

Something like this (od kunca)

import src.core.circumference
import src.core.addition
import src.core.multiplication

#TODO: this
Circumference: src.core.circumference.Circumference = None
Addition: src.core.addition.Addition = None
Multiplication: src.core.multiplication.Multiplication = None

'''
class MyProcedures:

    def __init__(self):
        pass
    
    some_parameter = 10
    #NOTE: This is howto write print() similarly to Cpp
    print('Parameter is: %i' %some_parameter)

    def my_procedure():
        print('This is my procedure!')

    def my_procedure_2():
        print('This is my procedure NUMBER 2!')



my_instance = cs_test.feature.FeatureCS()
my_instance.run_my_methods(MyProcedures.my_procedure, MyProcedures.my_procedure_2)

#my_instance.method_redefined_at_instance_level(self):
#    pass

'''
Third method: With class inheritance from Master class (Procedure_Framework class)
- Procedure is going to be a inheritted class and subtests are going to be methods of the class, with inheritance from 
  Master class (Procedure_Framework class).
- Than you may have multiple instances of subclasses of Master class each with slightly different input parameters and
  each in its own tree node.
- use encapsulation to prevent changing some parameters   

'''

