import random
from collections import deque
from csv import excel
from itertools import product

## MAT INFO
play_map: list = [[]]
visited_map: list = [[]]
base_map: list = [[]]
BOARD_SIZE: int = 0
MINE_MAP = []
FLAG_MAP = []

## GAME
PLAYING = True
MINE_PERCENT = 0.1
ACCEPT = True
BOMB = False

## COMMAND
SEARCH_COMMAND: int = 1
MARK_MINE_COMMAND: int = 2
EXIT_COMMAND: int = 0

## BOARD VALUE
MINE = '*'
BLANK_ZERO = 0
BLIND_SITE = '#'
FLAG = '⚐'
MINE_COUNT = 0
FLAG_COUNT = 0

## MOVE
udlr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cross_move = [-1, 1]
MOVES = udlr + [i for i in product(cross_move, repeat=2)]

## MSG
INFO_MSG = f"""
    커맨드를 입력해주세요 .
    0 : 종료
    1 : 지점 탐색
    2 : 지뢰 표시
    남은 지뢰 수 :: {MINE_COUNT}
"""
COMMAND_ERR_MSG = """
    올바르지않은 명령입니다.
"""
BOARD_SIZE_MSG = """
보드 사이즈를 입력해 주세요.
"""
EXIT_MSG = """
    종료 하셨습니다. 
"""
SEARCH_MSG = """
    탐색할 좌표를 선택해주세요. (y,x)
"""

FLAG_MSG = """
    깃발을 놓을 좌표를 선택해주세요 . (y, x)
"""
GAME_OVER_MSG = """
    폭탄 ! 게임오버 x_X
"""
def update_info_msg():
    global INFO_MSG,FLAG_MSG,MINE_COUNT
    INFO_MSG = f"""
        커맨드를 입력해주세요 .
        0 : 종료
        1 : 지점 탐색
        2 : 지뢰 표시
        남은 지뢰 수 :: {MINE_COUNT}
        남은 깃발 수 :: {FLAG_COUNT}
    """

def validate_index(y, x):
    return 1 <= y <= BOARD_SIZE and 1 <= x <= BOARD_SIZE


def create_board(size, default_value: str | int = 0):
    return [[default_value for _ in range(size)] for _ in range(size)]


def zero_spread(y, x):
    global base_map, play_map, visited_map
    q = deque()
    q.append((y, x))
    visited_map[y][x] = True
    while q:
        y, x = q.popleft()
        for move in MOVES:
            my, mx = move
            ny, nx = y + my, x + mx

            if validate_index(ny,nx) and base_map[ny][nx] != MINE:
                play_map[ny][nx] = base_map[ny][nx]
                if base_map[ny][nx] == BLANK_ZERO and not visited_map[ny][nx]:
                    visited_map[ny][nx] = True
                    q.append((ny, nx))

    ...


def update_near_mat_mine_score(y, x):
    global visited_map, base_map, play_map
    """ 주변칸 지뢰 포인트 업데이트"""
    for move in MOVES:
        my, mx = move
        ny, nx = y + my, x + mx
        if validate_index(ny, nx) and base_map[ny][nx] != MINE:
            base_map[ny][nx] = base_map[ny][nx] + 1


def create_mine(mat):
    global MINE_COUNT
    for y in range(1,len(mat)):
        for x in range(1,len(mat[y])):
            if random.random() <= MINE_PERCENT:
                mat[y][x] = MINE
                MINE_COUNT+=1
                MINE_MAP.append((y,x))
                update_near_mat_mine_score(y, x)
            ...


def search(y, x):
    global base_map, play_map
    """
    플레이보드에서 y , x  좌표 탐색
    :param y: 
    :param x: 
    :return: 
    """
    match base_map[y][x]:
        case n if n == MINE:
            return BOMB
        case n if n == BLANK_ZERO:
            zero_spread(y, x)
        case n:
            play_map[y][x] = base_map[y][x]
    return ACCEPT


def mark_flag(y, x):
    global play_map
    """
    :param y:
    :param x:
    :return:
    """
    global FLAG_COUNT

    match play_map[y][x]:
        case n if isinstance(n,int):
            return
        case n if n == FLAG:
            play_map[y][x] = BLIND_SITE
        case _:
            play_map[y][x] = FLAG


def init_play_map(map):
    """
    인덱스 그리는 함수
    :param map:
    :return:
    """
    map[0][0]=0
    for i in range(1,len(map)):
        map[0][i] = i
        map[i][0] = i
    pass


def main():
    global play_map, visited_map, base_map, BOARD_SIZE,FLAG_COUNT, MINE_COUNT
    BOARD_SIZE = int(input(BOARD_SIZE_MSG))
    visited_map = create_board(BOARD_SIZE+1, BLANK_ZERO)
    base_map = create_board(BOARD_SIZE+1, BLANK_ZERO)
    play_map = create_board(BOARD_SIZE+1, BLIND_SITE)
    init_play_map(play_map)
    init_play_map(base_map)
    create_mine(base_map)
    FLAG_COUNT = MINE_COUNT

    # print_mat(base_map, "base_map")
    print_mat(play_map, "play_mat")
    # print_mat(visit_map, "visit_mat")

    while PLAYING:
        update_info_msg()
        command = input(INFO_MSG)
        try:
            c = int(command)
            match c:
                case x if x == SEARCH_COMMAND:
                    # SEARCH OPTION
                    print(SEARCH_MSG)
                    # 서치 프로세스
                    y, x = map(int, input().split())
                    result = search(y, x)

                    if result == BOMB:
                        print(GAME_OVER_MSG)
                        print_mat(base_map, "base_map")
                        exit(0)
                case x if x == MARK_MINE_COMMAND:
                    # MARK_MINE OPTION
                    print(FLAG_MSG)
                    y, x = map(int, input().split())
                    # 깃발 놓는 프로세스
                    mark_flag(y, x)
                    ...
                case x if x == EXIT_COMMAND:
                    # EXIT
                    print(EXIT_MSG)
                    exit(0)
                case n:
                    raise ValueError
        except Exception as e:
            print(e)
            print(COMMAND_ERR_MSG)
        print_mat(play_map)


def print_mat(mat, mat_name=None):
    """ 지도 출력 함수 DEBUG """
    board_padding = len(str(BOARD_SIZE))
    if mat_name:
        print(mat_name)

    for row in mat:
        padded_row = [f"{r: >{board_padding}}" for r in row]
        print(*padded_row)

if __name__ == '__main__':
    main()
