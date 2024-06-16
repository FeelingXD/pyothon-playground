import pandas as pd


def main():
    data = {
        "학번": range(2000, 2010),
        "성적": [85, 95, 75, 70, 100, 100, 95, 85, 80, 85],
    }
    frame = pd.DataFrame(data)
    print(frame)
    pass


if __name__ == "__main__":
    main()
    pass
