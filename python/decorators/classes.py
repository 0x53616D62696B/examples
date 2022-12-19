from typing import Callable

class TimedEvent():

    def __init__(self, func):
        
        self.list_of_events = []
        self.test_var = 0
        self.func = func

    def run_event(self):
        self.func(self)

class ProcedureFramework():
    def __init__(self):
        self.list_of_events = []
        self.dict_of_events = {}
    
    #def append_to_timed_event_list(self, *args, **kwargs):
    def append_to_timed_event_list(self, some_value): 

        def decorator(func):
            self.list_of_events.append(TimedEvent(func)) 

            self.dict_of_events.update({func.__name__:TimedEvent(func)})

            print(some_value) 
            print('inside the decorator function')
        return decorator