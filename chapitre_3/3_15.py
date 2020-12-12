from random import randint, choice
from my_main_functions import Queue


class Customer:
    def __init__(self):
        self.taux = 0
        self.waiting = False

    def coma(self):
        return self.taux >= 3

    def order_beer(self):
        self.waiting = True

    def waiting(self):
        return self.waiting()

    def drink_beer(self):
        self.taux += randint(200, 300) / 1000

    def tick(self):
        if not self.coma():
            if self.taux > 0:
                self.taux *= 35999 / 36000
                if self.taux <= 0:
                    self.taux == 0


class Bar:
    def __init__(self):
        self.prepare_time = 30
        self.remaining_time = 0
        self.beer = 0

    def prepare_beer(self):
        self.remaining_time = self.prepare_time

    def busy(self):
        return self.remaining_time > 0

    def tick(self, queue):
        if self.busy():
            self.remaining_time -= 1
            if self.remaining_time == 0:
                self.beer += 1
                return queue.pop()
        return ""

    def stop(self):
        self.remaining_time = 0

    def get_beers(self):
        return self.beer


def simulate(days, simulation_time, arriving_time, number_of_guests):
    q = Queue()

    bar = Bar()

    assoiffes = 0
    guests_in_coma = 0
    for day in range(days):
        time = 0
        coma = []
        guests_not_waiting = []
        for _ in range(number_of_guests):
            guests_not_waiting.append(Customer())
        for second in range(simulation_time):
            if time % arriving_time == 0 and len(guests_not_waiting) != 0:
                c = choice(guests_not_waiting)
                guests_not_waiting.remove(c)
                q.enqueue(c)
                c.order_beer()
                bar.prepare_beer()

            for g in guests_not_waiting:
                g.tick()
            for g in q.get_queue():
                g.tick()

            b = bar.tick(q)
            if b != "":
                b.drink_beer()
                if b.coma():
                    coma.append(b)
                else:
                    guests_not_waiting.append(b)

            time += 1
        assoiffes += q.size()
        q.empty()
        guests_in_coma += len(coma)
        bar.stop()

    return guests_in_coma, bar.get_beers(), assoiffes


"""
arriving_time = int(input("Un client arrive toutes les n secondes en moyenne. n = "))
simulation_time = int(input("Duree d une soiree: "))
days = int(input("Nombre de soirees: "))
number_of_guests = int(input("Nombre de clients par soiree: "))

results = simulate(days, simulation_time, arriving_time, number_of_guests)

print(f"Nombre total de bieres servies: {results[1]}")
print(f"Nombre total de clients dans le coma: {results[0]}")
print(f"Nombre total de clients assoiffes: {results[2]}")
"""
