import time

def timethis(function, *args, **kwargs):
    """
Times how long it takes to execute a function with particular parameters.

Returns a tuple where the 1st element is the output from the function and the 
2nd is the execution time in seconds.
    """
    t0 = time.time()
    output = function(*args, **kwargs)
    t1 = time.time()
    return (output, t1 - t0)