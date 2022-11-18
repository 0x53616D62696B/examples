import os
'''
If you want to include all modules in this directory with 'from MODULE import *' 
import (bad) practice, you would have to specify it in __all__ list, otherwise 
it will not import anything if we importing from package.
'''
#__all__ = ['old_module', 'retained_module'] #LIST OF ALL MODULEES YOU WANT TO INCLUDE WITH *


'''
Option 0
#new package reimports from old package
NOTE: Reimported module name has to be the same as the old module name. 
        Use import DIFFERENT_NAME as SAME_NAME instead
'''
"""
from new_package import new_module as old_module 
sys.modules['old_package.old_module'] = old_module
"""

'''
Option 1) - #! WINNER
First search the new package, than the old one.
'''
#get_absolute_path = os.getcwd()
__path__ = [os.getcwd() + '\\python\\package_redirection\\new_package', __path__[0]]


'''
Option 2)
Change submodule search locations - THIS POSSIBILITy is.. weird.. :D  BUT IT IS WORKING!
'''
"""
__spec__.submodule_search_locations = ['c:\\dev\\examples\\python\\package_redirection\\new_package', 
                                        __spec__.submodule_search_locations[0]]
"""


'''
Option 3)
Loader nebo finder
'''
# To use appropriate finder youu should basically use my Option 1, __path__.


print('test')