import sys

'''
#new package reimports from old package
NOTE: Reimported module name has to be the same as the old module name. 
        Use import DIFFERENT_NAME as SAME_NAME instead
'''

"""
from new_package import new_module as old_module 
sys.modules['old_package.old_module'] = old_module
"""

'''
If you want to include all modules in this directory with 'from MODULE import *' 
import (bad) practice, you would have to specify it in __all__ list, otherwise 
it will not import anything if we importing from package.
'''
__all__ = ['retained_module']
#__all__ = ['old_module', 'retained_module']
#__path__ = []
# moznost cislo 1: hodit sem prvne aegir a pak az tuhle slozku (tecku nebomezeru stringu) - aneb kdyz to nenajde modul v
# aegir, zkusi to hledat zde..


'''
Option 2)

dalsi moznost upravit submodule search locations - THIS POSSIBILITy is.. weird.. :D  BUT IT IS WORKING!
'''
__spec__.submodule_search_locations.append(__spec__.submodule_search_locations[0])
__spec__.submodule_search_locations[0] = 'c:\\dev\\examples\\python\\package_redirection\\new_package'

'''
Option 3)

testnout loader nebo finder
'''


print('test')

