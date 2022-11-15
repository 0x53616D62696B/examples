import sys

#new package reimports from old package
#NOTE: name of reimported module has to be the same as old one
from new_package import new_module as old_module 
sys.modules['old_package.old_module'] = old_module
