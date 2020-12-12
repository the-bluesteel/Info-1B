from functools import lru_cache


@lru_cache(maxsize=128)
def pascal_rec(n, p):
    if p in [0, n]:
        return 1
    return pascal_rec(n - 1, p) + pascal_rec(n - 1, p - 1)


def main():
    input = input().split(" ")
    n, p = int(input[0]), int(input[1])

    print(pascal_rec(n, p))


if __name__ == "__main__":
    main()
