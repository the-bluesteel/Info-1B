from my_main_functions import Stack


def check_brackets(s):
    pile = Stack()
    open = ["[", "(", "{"]
    close = ["]", ")", "}"]
    for c in s:
        if c in open:
            pile.push(c)
        elif c in close:
            last_bracket = pile.pop()
            if open[close.index(c)] != last_bracket:
                return False
    return True


"""
print(check_brackets("[1*2{7-1-1(3-y})]"))
print(check_brackets("[1*2{7-1}-1(3-y)]"))
"""
