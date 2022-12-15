class TimedEvent():

    def __init__(self, func):
        
        self.list_of_events = []


class ProcedureFramework():
    def __init__(self):
        self.list_of_events = []
        self.dict_of_events = {}
    
    def append_to_timed_event_list(self, event_function:callable):
        #event_instance = TimedEvent(event_function)
        #self._list_of_events.append(event_instance)
        self.list_of_events.append(TimedEvent(event_function))
        #dictionary
        
        #! ? what name will this create???
        #self.dict_of_events.append({event_function.__name__:TimedEvent(self.event_instance)})
        self.dict_of_events.update({event_function.__name__:TimedEvent(event_function)})