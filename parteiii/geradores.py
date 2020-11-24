import os

def find(path='.'):

    for item in os.listdir(path):
        fn = os.path.normpath(os.path.join(path, item))

        if os.path.isdir(fn):

            for f in find(fn):
                yield f
        
        else:
            yield fn

def gen_pares():
    """
    Gera numeros pares indefinidamente
    """

    i = 0

    while True:
        i += 2
        yield i

for fn in find():
    print(fn)

# for n in gen_pares():
    # print(n)

