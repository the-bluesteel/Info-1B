from my_main_functions import Stack


def convert_to_binary(i):
    s = Stack()
    while i != 0:
        print(i)
        s.push(i % 2)
        i //= 2

    binary = 0
    print(s)
    while not s.is_empty():
        n = s.pop()
        binary += n * (10 ** s.size())

    return binary


print(convert_to_binary(100))
