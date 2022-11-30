import sys
import types
import inspect
"""
def function_test():
    print('func test')
class FeatureCS:
    def __init__(self):
        pass

    def method_redefined_at_instance_level(self):
        print('method defined at class level')
    
    def run_my_methods(self, *args):
        '''
        Abstracted pipeline implementation

        '''
        for func in args:
            # Display function name
            print(func.__name__)

            # CHeck whether is method
            '''
            if isinstance(func, types.MethodType): # True
                if func.some_parameter is not None:
                    func.some_parameter = 20
            '''
            if inspect.ismethod(func): #does not work as intended
                if func.some_parameter is not None:
                    func.some_parameter = 20

            if func.__name__ == 'my_procedure_2': #does not work as intended
                func.some_parameter = 20
                print('test')

            # Run the function
            func()

function_test()
                
            
"""
# implement method 3
            

