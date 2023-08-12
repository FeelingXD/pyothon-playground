pos = 5, 10
pos2 = 1, 10
test = [pos, pos2]

for t in test:
    match t:
        case (5, y):
            print(f"this case 5,{y}")
        case x:
            print(f"wild card used input {x}")
