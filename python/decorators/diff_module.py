from classes import ProcedureFramework

first_procedure = ProcedureFramework()

@first_procedure.append_to_timed_event_list
def setup_negative_polarity_event(frameworked_procedure:ProcedureFramework): 
    pass


print(first_procedure.list_of_events[0].__class__.__name__)
print(first_procedure.dict_of_events['setup_negative_polarity_event'])