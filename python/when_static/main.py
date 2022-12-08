import values

# no need for static variables
i=0
while i < 10:
    values.change_your_value()
    values.show_value()
    i = i + 1


# need to use static variables - #! NOT TRUE, how is it?
i=0
while i < 10:
    values.var_ = values.var_ + 1
    print(values.var_)
    i = i + 1  