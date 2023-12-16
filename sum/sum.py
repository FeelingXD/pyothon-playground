# sum 알아보기
class test_sum():
    def __init__(self) -> None:
        pass
    def __add__(self,other):
        return other


    
# 2차원 배열 을 1차원 배열로 바꿔보기
def flat_arr():
    tmp=[[1,2],[3,4]]
    print(sum(tmp,[]))


if __name__=="__main__":
    print(sum(["1","2"], test_sum()))