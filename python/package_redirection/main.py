'''
About:
--------------------
This example shows how to redirect certain module from package to different module 
in different package. Usefull when rewriting module with legacy backward compatability.

old_package is the old package and old_module is the old module
new_package is the new package and new_module is the module we are redirecting to

Function:
--------------------
When you use import mechanism: from old_package import old_module in retained_module, 
it will actually does from new_package import new_module.

Importing old module from retained module will return new module.

Start file:
--------------------
This file is main executable.

NOTE:
--------------------
You have to redirect all subfolders in packages too!
'''

import old_package.retained_module

instance = old_package.retained_module.RetainedCS()
instance.test_package_redirection()

