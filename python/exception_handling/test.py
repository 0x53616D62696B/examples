# For testing purposes only
if __name__ == '__main__':

    class ExceptionFailure(Exception):
        """Procedure execution failed."""
        pass

    class ExceptionPrecondFailed(ExceptionFailure):
        """Procedure execution cancelled because precondition not fulfilled."""
        pass


    #print("%i", range(3))
    i = range(3)
    print('range(3) is: "%s" '% range(3))# ('some name', 'some text'))
    msg = 'testing msg'
    try:
        print(msg)
        raise ExceptionPrecondFailed(msg)
    except:
        print("exception raised")
    else:
        print("no exception raised")
    finally: # always executed
        print("finally raised")

    print("Hi ThermoWorld!")