import traceback

try:
    print(1/0)
except ZeroDivisionError:
    print('Aconteceu um erro')
    trace = traceback.format_exc()
    print('Aconteceu um erro:\n',trace)
    open('trace.log','a').write(trace)
    
    raise SystemExit
 