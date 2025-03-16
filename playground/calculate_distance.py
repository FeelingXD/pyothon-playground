
import math
## 두점 사이의 좌표 의 거리를 구한다


def cal_distnace_2(x1,x2,y1,y2)->float:
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    pass
def cal_distance(x1,x2,y1 ,y2)->float:
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
    pass


def distance(x1, y1, x2, y2):  # 거리를 구하는 함수 정의
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)  # 거리를 구하는 공식


if __name__ == "__main__":
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    print(cal_distance(x1,x2,y1,y2))
    print(cal_distnace_2(x1,x2,y1,y2))
    print(distance(x1, y1, x2, y2))

    pass