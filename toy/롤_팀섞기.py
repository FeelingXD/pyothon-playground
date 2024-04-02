import random
from collections import defaultdict


# input
player_list_input = [
    "영우 1",
    "상혁 3",
    "하진 4",
    "진철 4",
    "이준 1",
    "성규 4",
    "희성 5",
    "태민 4",
    "연우 5",
    "연찬 5",
]

top_list_input = ["영우", "상혁", "하진"]
jg_list_input = ["진철", "이준", "성규"]
mid_list_input = ["상혁", "희성", "진철"]
ad_list_input = ["태민", "연찬", "진철", "상혁"]
sup_list_input = ["연우", "상혁", "태민"]

# static init
lines_input = [
    top_list_input,
    jg_list_input,
    mid_list_input,
    ad_list_input,
    sup_list_input,
]

TOP = 0
JG = 1
MID = 2
AD = 3
SUP = 4
line = ["TOP", "JG", "MID", "AD", "SUP"]
candidate_score = {
    player.split()[0]: int(player.split()[1]) for player in player_list_input
}


def init_process() -> None:
    global red_team, blue_team, check
    red_team = []
    blue_team = []
    check = defaultdict(lambda: False)
    # shuffle line
    for line in lines_input:
        random.shuffle(line)


def print_team():
    red_score = cal_score(red_team)
    blue_score = cal_score(blue_team)
    print(
        "\t",
        "\t".join(line),
        "\tSCORE",
    )
    print("레드", *red_team, red_score, sep="\t")
    print("블루", *blue_team, blue_score, sep="\t")


def validate_balance():
    red_score = cal_score(red_team)
    blue_score = cal_score(blue_team)
    return 2 <= abs(red_score - blue_score)


def candidate_pick(line_index):
    global check
    for line_candidate in lines_input[line_index]:
        if not check[line_candidate]:
            check[line_candidate] = True
            return line_candidate


def append_team(candidate_1, candidate_2):
    if not red_team:
        red_team.append(candidate_1)
        blue_team.append(candidate_2)

    else:
        red_score = cal_score(red_team)
        blue_score = cal_score(blue_team)

        weak_team, strong_team = (
            [red_team, blue_team] if red_score <= blue_score else [blue_team, red_team]
        )
        weak_candidate, strong_candidate = (
            [candidate_1, candidate_2]
            if candidate_score[candidate_1] <= candidate_score[candidate_2]
            else [candidate_2, candidate_1]
        )

        weak_team.append(strong_candidate)
        strong_team.append(weak_candidate)

    # 후보 체크
    check[candidate_1] = True
    check[candidate_2] = True


def cal_score(team):
    return sum([candidate_score[player] for player in team])


def solution():
    init_process()
    need_retry = False

    # if picked then power will be 0
    for line_index in range(5):  # line
        candidate_1, candidate_2 = candidate_pick(line_index), candidate_pick(
            line_index
        )

        if None in [candidate_1, candidate_2]:
            solution()
        append_team(candidate_1, candidate_2)
    if validate_balance():
        need_retry = True
    if need_retry:
        solution()
    else:
        print_team()
    exit()


if __name__ == "__main__":
    solution()
    pass
