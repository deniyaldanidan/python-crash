

def op_sum(*args):
    sm=0
    for i in args:
        sm+=i
    
    return sm;

def op_average(*args):
    sm = op_sum(*args)
    return sm/len(args)