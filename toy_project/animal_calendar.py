# 60 갑자의 갑자년 계산기 Earthly Branches
import sys
import datetime

input = sys.stdin.readline

decade = ["갑甲", "을乙", "병丙", "정丁", "무戊", "기己", "경庚", "신辛", "임(壬)", "계癸"]  # 10 간
zodiac = ["자子", "축丑", "인寅", "묘卯", "진辰", "사巳", "오午", "미未", "신申", "유酉", "술戌", "해亥"]  # 12지


def get_earthly_branches(year) -> tuple:
    """
    parameters:
        year - year that get earthly branches
    The return :
        type of tuple[korean, chinese]
    """
    decade_word = decade[year % 10]
    zodiac_word = zodiac[year % 12]
    kor_branches = decade_word[0] + zodiac_word[0]
    ch_branches = decade_word[1] + zodiac_word[1]
    return (kor_branches, ch_branches)
    pass


def get_current_year():
    """
    parameters: None
    return :
        int - current_year by system
    """
    return datetime.datetime.now().year


def print_animal_calendar(year: int) -> None:
    earthly_branches = get_earthly_branches(year)

    print(
        f"{year}년은 {earthly_branches[0]} 년 입니다. 한자로는 {earthly_branches[1]} 으로 표기 됩니다."
    )

    pass


if __name__ == "__main__":
    current_year = get_current_year()
    print_animal_calendar(current_year)
    pass
