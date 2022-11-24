import old_package.old_module
import old_package.old_subpackage.submodule
import sys

class RetainedCS:
    def __init__(self):
        pass

    def test_package_redirection(self):
        instance_package = old_package.old_module.CSToReimport()
        instance_package.hello()

        instance_subpackage = old_package.old_subpackage.submodule.CSToReimport()
        instance_subpackage.hello()
