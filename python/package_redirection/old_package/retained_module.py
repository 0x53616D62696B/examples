import old_package.old_module
import sys

class try_something:
    def __init__(self):
        pass
    def hello(self):
        import_s = old_package.old_module.try_something2()
        import_s.hello()