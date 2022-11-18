import sys

'''
#new package reimports from old package
NOTE: Reimported module name has to be the same as the old module name. 
        Use import DIFFERENT_NAME as SAME_NAME instead
'''
from new_package import new_module as old_module 
sys.modules['old_package.old_module'] = old_module

'''
If you want to include all modules in this directory with 'from MODULE import *' 
import (bad) practice, you would have to specify it in __all__ list, otherwise 
it will not import anything if we importing from package.
'''
#__all__ = ['tng', 'adapt']
