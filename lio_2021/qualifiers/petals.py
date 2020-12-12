def main():
    # get total amount of petals
    n = int(input())

    assert 1 <= n <= 10e5, f"{n} is not a valid amount of petals for this program"

    # Read description of lioflower
    petals = input().split("")

    assert len(petals) == int(n), "inappropriate amount of petals"

    # get lowest amount there is for one colour
    lowest_amount = min(petals.count("r"), petals.count("w"), petals.count("b"))

    # return sum of petals that have to be cut off for each colour to match lowest_amount
    print(sum([(petals.count(c) - lowest_amount) for c in ["r", "w", "b"]]))


if __name__ == "__main__":
    main()
