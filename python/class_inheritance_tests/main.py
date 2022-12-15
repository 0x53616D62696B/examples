

class Masses:
    mass_list = [100] * 32
    def __init__(self, mass):
        self.mass = mass

class Event:
    def __init__(self, event):
        self.event = event
    event = 456

    def append_to_event_list(self, event):
        print("appended to event list")


class FrameworkedProcedures(Masses, Event):

    def __init__(self):
        pass
    
    some_parameter = 10
    #NOTE: This is howto write print() similarly to Cpp
    #print('Parameter is: %i' %some_parameter)

    def my_procedure():
        print('This is my procedure!')

    def my_procedure_2():
        print('This is my procedure NUMBER 2!')



my_procedure = FrameworkedProcedures()

my_procedure.event = 1
print(my_procedure.event)

my_procedure_2 = FrameworkedProcedures()

print(my_procedure_2.event)