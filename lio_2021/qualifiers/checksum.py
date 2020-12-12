from string import ascii_letters, ascii_uppercase


def checksum(code):
    """Step 1"""
    # remove empty spaces
    code = code.replace(" ", "")

    # evaluate checksum of code assuming there cannot contain a "?" nor a letter ("a number between 02 and 98")
    check_sum = code[2] + code[3]

    """Step 2"""
    # copy code in case it checksum has to be adapted or if code contains a joker
    copy_code = code

    # switching places of first four characters
    first_characters = code[:4]
    code = code[4:] + first_characters

    """Step 3"""
    # replace letters with numbers considering their position in alphabet
    for c in code:
        if not (c.isdigit() or c == "?"):
            code = "".join([c if c.isdigit() or c == "?" else str(ascii_uppercase.index(c.upper()) + 10) for c in code])

    """Step 4"""

    # consider what to return depending on whether jokers are included or not
    if not "?" in code:  # i.e. if code is complete
        if int(code) % 97 == 1:
            return "OK"
        else:
            # Otherwise return the complete code with a valid checksum
            for possible_checksum in list(str(a) + str(b) for a in range(0, 10) for b in range(0, 10)):
                if possible_checksum not in ["01", "00", check_sum]:
                    if int(code[:-2] + possible_checksum) % 97 == 1:
                        return (copy_code[:2] + possible_checksum + copy_code[4:]).upper()
    else:
        index_of_jokes = code.index("?")
        valid_codes = []
        # check all valid codes where ? is replaced by either a digit or a letter
        for joker in list(str(i) for i in range(36)):
            code_to_check = code[:-1] + joker if index_of_jokes + 1 == len(code) else \
                code[:index_of_jokes] + joker + code[index_of_jokes + 1:]

            if int(code_to_check) % 97 == 1:
                # get index of joker in unchanged code
                code_joker_index = copy_code.index("?")

                # turn joker to either letter or digit depending on its value
                joker = ascii_uppercase[int(joker) - 10] if int(joker) > 9 else joker

                # add valid version of code where ? has been replaced by joker
                valid_codes.append((copy_code[:-1] + joker).upper() if code_joker_index + 1 == len(copy_code) else \
                                       (copy_code[:code_joker_index] + joker + copy_code[
                                                                               code_joker_index + 1:]).upper())

        # return impossible if no valid codes were found, otherwise return all separated by a space if more than one
        return "impossible" if len(valid_codes) == 0 else " ".join(valid_codes)


def main():
    n = int(input())

    for _ in range(n):
        print(checksum(input()))


if __name__ == "__main__":
    main()
