a = "global" # 전역
def cool_func():
    a = "local" # 지역
    print(locals()) # 
cool_func()
print(locals()) 
print(globals())