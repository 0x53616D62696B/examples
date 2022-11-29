import sys

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
            # Run the function
            func()
                
            

            

