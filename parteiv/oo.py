###########
#decorator
###########

def dumpargs(f):

    def func(*args):

        print(args)

        return f(*args)
    
    return func

@dumpargs
def multiply(*nums):
    m = 1

    for n in nums:
        m = m * n
    
    return m

print(multiply(1,2,3))