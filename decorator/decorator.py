# 파이썬 데코레이터
import time
from functools import wraps

def time_it(f):
    @wraps(f)
    def time_wrapper(*arg,**kwargs):
        start_time = time.perf_counter()
        f(*arg,**kwargs)
        end_time=time.perf_counter()
        print(f'time_it check start:{start_time}  end: {end_time} duration : {end_time-start_time}')
    return time_wrapper

def hello_deco(f):
    @wraps(f)
    def append_hello(*arg,**kwargs):
        print("this is Hello decorator")
        f(*arg,**kwargs)
    return append_hello

def python_deco(f):
    @wraps(f)
    def append_python_deco(*arg,**kwargs):
        print("life is short you need python")
        f(*arg,**kwargs)
    return append_python_deco

@hello_deco
@python_deco
def hello():
    print("Hello world")


hello()
    