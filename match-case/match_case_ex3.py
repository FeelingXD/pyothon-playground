heros = ["batman", "robin"]
villains = ["joker"]
ext = ["엑스트라1", "엑스트라2"]
for p in heros+villains+ext:
    match p:
        case x if x in heros:
            print(f'{x} is a hero')
        case x if x in villains:
            print(f'{x} is a villain')
        case x:
            print(f'{x} who are you ?')
