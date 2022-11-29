import cs_test.feature

'''
With functions
'''

def my_procedure():
    print('This is my procedure!')

def my_procedure_2():
    some_parameter = 10
    print('This is my procedure NUMBER 2!')
    print('Parameter is: %i' %some_parameter)

my_instance = cs_test.feature.FeatureCS()
my_instance.run_my_methods(my_procedure, my_procedure_2)

'''
With class methods

#TODO: I believe I can rewrite method of class.. 
#TODO: !!OR ADD METHOD TO A CLASS on different page...
'''
#my_instance.method_redefined_at_instance_level(self):
#    pass

