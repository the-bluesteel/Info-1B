from string import ascii_lowercase
from math import ceil


def find_key(c, l):
    for index, element in enumerate(l):
        if element == c:
            return index

    return -1


def find_key_r(c, l):
    if len(l) == 0:
        return -1

    if l[-1] == c:
        return len(l) - 1
    l.pop()
    return find_key_r(c, l)


def find_all_keys(c, l):
    keys = []
    for index, elements in enumerate(l):
        if elements == c:
            keys.append(index)

    return keys


def find_all_keys_r(c, l, s=[]):
    if len(l) == 0:
        return s

    if l[-1] == c:
        s.append(len(l) - 1)

    l.pop()
    return find_all_keys_r(c, l, s)


def find_key_sorted(c, l):
    while len(l) != 0:
        if len(l) == 1:
            return True if l[0] == c else False
        k = ceil(len(l) / 2)
        if len(l[k]) == len(c):
            b = True
            for index, carac in enumerate(l[k]):
                if b:
                    if carac != c[index]:
                        b = False
                        if ascii_lowercase.index(carac.lower()) < ascii_lowercase.index(c.lower()[index]):
                            l = l[k:]
                        else:
                            l = l[:k]
            if b:
                return True

        else:
            max_len = len(c) if len(c) < len(l[k]) else len(l[k])
            if max_len == 0:
                l = l[k + 1:]
                if c == "":
                    return True
            else:
                b = True
                for index in range(max_len):
                    if b:
                        if l[k][index] != c[index]:
                            b = False
                            if ascii_lowercase.index(l[k][index].lower()) < ascii_lowercase.index(c.lower()[index]):
                                l = l[k:]
                            else:
                                l = l[:k]


def find_key_sorted_r(c, l):
    if len(l) == 0:
        return False
    if len(l) == 1:
        return True if l[0] == c else False

    k = ceil(len(l) / 2)
    b = True
    if len(l[k]) != len(c):

        max_len = len(c) if len(c) < len(l[k]) else len(l[k])
        if max_len == 0:
            return find_key_sorted_r(c, l[k + 1:])

        for index in range(max_len):
            if b:
                if l[k].lower()[index] != c.lower()[index]:
                    b = False
                    if ascii_lowercase.index(l[k].lower()[index]) < ascii_lowercase.index(c.lower()[index]):
                        return find_key_sorted(c, l[k + 1:])
                    else:
                        return find_key_sorted(c, l[:k])

    else:
        if c == l[k]:
            return True
        for index, carac in enumerate(l[k]):
            if b:
                if carac != c[index]:
                    b = False
                    if ascii_lowercase(carac.lower()) < ascii_lowercase(c.lower()[index]):
                        return find_key_sorted_r(c, l[k + 1:])
                    else:
                        return find_key_sorted_r(c, l[:k])
