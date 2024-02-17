# 몬티홀 문제
"""
닫혀 있는 문 3개가 있다.
한 문 뒤에는 상품(=자동차)이 있고, 나머지 두 문은 꽝(=염소)이다.
참가자는 이 3가지 문 중 하나를 골라야 상품을 얻을 수 있다.
참가자가 문 하나를 고르면, 이미 상품이 어딨는지 알고 있는 사회자는 남은 2가지 문 중에 하나를 열고 그게 '꽝'이라는 사실을 밝힌다.
여기서 참가자에게 다른 문으로 바꿀 수 있는 기회가 주어진다.
"""
import random


def mc_pick(participant_choice, answer):
    while True:
        pick = random.randint(0, 2)
        if pick != participant_choice and pick != answer:
            break
    return pick


def monty_hall_problem():
    """
    정답과 사용자의 선택은 랜덤이다.
    """
    answer = random.randint(0, 2)
    participant_choice = random.randint(0, 2)
    mc_choice = mc_pick(answer, participant_choice)

    new_choice = set(
        [i for i in range(3) if i not in (mc_choice, participant_choice)]
    ).pop()
    # 바꿔서 정답인경우, 바꾸지않아서 정답인경우

    return [answer == participant_choice, answer == new_choice]


if __name__ == "__main__":
    not_change_cnt = 0
    change_cnt = 0
    for _ in range(case := 100_000):  #
        not_change, change = monty_hall_problem()
        change_cnt = change_cnt + 1 if change else change_cnt
        not_change_cnt = not_change_cnt + 1 if not_change else not_change_cnt
    print(f"result {change_cnt =} , {not_change_cnt=}")

    pass
