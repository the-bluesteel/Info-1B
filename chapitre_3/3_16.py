from random import randint
from my_main_functions import Queue


class Shopper:
    def __init__(self):
        self.articles = randint(1, 50)
        self.unweighted = True if randint(1, 20) == 1 else False
        self.bad_card = True if randint(1, 50) == 1 else False
        self.check_out = 0
        self.waiting_time = 0
        self.total_waiting_time = 0

    def has_bad_card(self):
        return self.bad_card

    def has_not_weighted(self):
        return self.unweighted

    def set_checkout(self, checkout):
        self.check_out = checkout

    def get_checkout(self):
        return self.check_out

    def get_articles(self):
        return self.articles

    def get_total_waiting_time(self):
        return self.total_waiting_time

    def checkout_time(self):
        time = 5 * self.articles
        time += 3 * 60 if self.has_bad_card() else 15
        time += 55 if self.has_not_weighted() else 0

        return time

    def tick(self):
        self.waiting_time += 1
        self.total_waiting_time += 1
        if self.waiting_time == 60:
            return True
        return False

    def nervous(self, checkout):
        self.waiting_time = 0
        self.check_out = checkout


class CheckOut:
    def __init__(self, number):
        self.queue = Queue()
        self.remaining_time = 0
        self.number = number
        self.customer = None

    def get_number(self):
        return self.number

    def get_queue(self):
        return self.queue

    def start(self):
        if not self.queue.is_empty():
            self.customer = self.queue.pop()
            self.remaining_time = self.customer.checkout_time()

    def busy(self):
        return self.remaining_time > 0

    def tick(self):
        if self.busy():
            self.remaining_time -= 1
            if self.remaining_time == 0:
                return self.customer
        return ""

    def add_to_queue(self, shopper):
        self.queue.enqueue(shopper)

    def remove_from_queue(self, shopper):
        self.queue.remove(shopper)

    def stop(self):
        self.queue.empty()
        self.remaining_time = 0
        self.customer = None


def simulation(amount_of_checkouts, days, simulation_time, arriving_time):
    best_queue = [0] * amount_of_checkouts
    checkouts = []
    waiting_time = [0, 0]
    articles_sold = 0
    changements_de_file = 0
    clients_servis = 0
    heures_supplementaires = 0
    sss = 0
    for _ in range(amount_of_checkouts):
        checkouts.append(CheckOut(_))

    for day in range(days):
        time = 0
        for second in range(simulation_time):
            if time % arriving_time == 0:
                sss += 1
                shopper = Shopper()
                number_of_checkout = best_queue.index(min(best_queue))
                shopper.set_checkout(number_of_checkout)
                best_queue[number_of_checkout] += 1
                checkout = checkouts[number_of_checkout]
                checkout.add_to_queue(shopper)

            for c in checkouts:
                for shopper in c.get_queue().get_queue():
                    b = shopper.tick()
                    if b:
                        l = [shopper.get_checkout() + 1, shopper.get_checkout() - 1]
                        if l[0] >= amount_of_checkouts:
                            l.remove(l[0])
                        if l[-1] < 0:
                            l.remove(l[-1])
                        b = True
                        for i in l:
                            if b:
                                if best_queue[i] < checkouts[shopper.get_checkout()].get_queue().size():
                                    b = False
                                    checkouts[shopper.get_checkout()].remove_from_queue(shopper)
                                    best_queue[shopper.get_checkout()] -= 1
                                    shopper.nervous(i)
                                    best_queue[i] += 1
                                    checkouts[i].add_to_queue(shopper)
                                    changements_de_file += 1

            for checkout in checkouts:
                if not checkout.get_queue().is_empty() and not checkout.busy():
                    checkout.start()
                c = checkout.tick()
                if c != "":
                    waiting_time[0] += c.get_total_waiting_time()
                    waiting_time[1] += 1
                    articles_sold += c.get_articles()
                    best_queue[checkout.get_number()] -= 1
                    clients_servis += 1
            time += 1
        while sum(best_queue) != 0:
            print(best_queue)
            for checkout in checkouts:
                if not checkout.get_queue().is_empty() and not checkout.busy():
                    checkout.start()
                c = checkout.tick()
                if c != "":
                    waiting_time[0] += c.get_total_waiting_time()
                    waiting_time[1] += 1
                    articles_sold += c.get_articles()
                    best_queue[checkout.get_number()] -= 1
                    clients_servis += 1
            time += 1
            heures_supplementaires += 1
    print(sss, "Shoppers")
    return clients_servis, articles_sold, waiting_time, changements_de_file, heures_supplementaires


"""
arrival_time = int(input("Un client arrive toutes les n secondes en moyenne. n = "))
simulation_time = int(input("Duree d un jour: "))
days = int(input("Nombre de jours: "))
amount_of_checkouts = int(input("Nombre de caisses ouvertes: "))

results = simulation(amount_of_checkouts, days, simulation_time, arrival_time)

print(f"Nombre total de clients servis: {results[0]}")
print(f"Nombre total d articles vendus: {results[1]}")
print(f"Nombre total de minutes d attente: {(results[2][0] / results[2][1]) / 60}")
print(f"Nombre total de changements de file: {results[3]}")
print(f"Nombre total d heures supplementaires: {results[4] / 3600}")
"""
