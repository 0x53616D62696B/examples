


# need to use static variable!!
def increment_your_value():
    var_ = 10
    print(var_)
    var_ = var_ + 1

i=0
while i < 10:
    increment_your_value()
    i = i + 1  



# global variable used!!
var_ = 10
def increment_your_global_value():
    global var_
    print(var_)
    var_ = var_ + 1

i=0
while i < 10:
    increment_your_global_value()
    i = i + 1  


# static variable used!!
#! totally useless way!!!!!!! dont do that again!!! 
#! static is good aproach only in C++
# not a good example.. cant find anything else right now
# perhaps use this if needed 
# https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
class static:
    var_ = 20

def increment_your_static_value():
    var = static
    print(var.var_)
    print(static.var_)
    var.var_ = var.var_ + 1

i=0
while i < 10:
    increment_your_static_value()
    i = i + 1  
