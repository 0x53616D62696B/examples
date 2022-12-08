dict_ = {
    "hello": "world",
}
tuple_ = (0, 1, 2)
list_ = {2, 1, 0}
var_ = 10

def change_your_value():
    global var_
    var_ = var_ + 1

def show_value():
    global var_
    print(var_)    