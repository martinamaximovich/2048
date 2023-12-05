from os import devnull
from contextlib import redirect_stdout

from GameManager import play

def main() -> None:
    res = []
    with open(devnull, "w") as f, redirect_stdout(f):
        for _ in range(10):
            res.append(play())

    res.sort()
    print(res)

if __name__ == "__main__":
    main()