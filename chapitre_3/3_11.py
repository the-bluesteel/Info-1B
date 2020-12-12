from my_main_functions import Queue


def find_survivor(n, k):
    q = Queue()
    for _ in range(1, n + 1):
        q.enqueue(_)
    counter = 0
    msg_counter = 0
    msg = ""
    while q.size() != 1:
        counter += 1
        element = q.pop()
        if counter % k == 0:
            msg += str(element) + " "
            msg_counter += 1
            if msg_counter % 30 == 0:
                msg += "\n"
        else:
            q.enqueue(element)
    print(msg)
    return q.pop()


"""
n = int(input("Entrez le nombre de personnes : "))
k = int(input("Entrez k: "))
print(f"Dernière personne dans le cercle: {find_survivor(n, k)}")
"""
