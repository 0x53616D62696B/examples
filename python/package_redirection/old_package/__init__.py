import sys

#new package reimports from old package
from new_package import new_module as old_module 
sys.modules['old_package.old_module'] = old_module

#all retained modules from old package
from old_package import retained_module
sys.modules['old_package.retained_module'] = retained_module