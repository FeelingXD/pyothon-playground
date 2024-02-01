# 컴프리핸션 성능 테스트
import time
from functools import wraps

test_range = 10**8
sample_data = [str(i) for i in range(test_range)]


def excution_time(func):
    """
    feat - excution time decorator
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"Function {func.__name__}{args} {kwargs} Took {end_time-start_time:.4f} seconds"
        )

    return wrapper


@excution_time
def get_comprehension_time():
    global sample_data
    [int(i) for i in sample_data]


@excution_time
def get_list_exchange_time():
    global sample_data
    tmp = []
    for v in sample_data:
        tmp.append(int(v))


if __name__ == "__main__":
    get_comprehension_time()
    get_list_exchange_time()
