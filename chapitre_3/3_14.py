from random import randint
from my_main_functions import Queue


class Client:
    def __init__(self, arrival_time):
        self.at = arrival_time
        self.p = randint(2 * 60, 10 * 60)

    def tick(self, time):
        return time - self.at >= self.p

    def get_time(self):
        return self.at


class Guichet:
    def __init__(self):
        self.remaining_time = 0
        self.clients = 0

    def start(self):
        self.remaining_time = randint(30, 5 * 60)

    def busy(self):
        return self.remaining_time > 0

    def tick(self):
        if self.busy():
            self.remaining_time -= 1
            if self.remaining_time == 0:
                self.clients += 1

    def stop(self):
        self.remaining_time == 0
        self.clients += 1


def simulation(arrival_time, simulation_time, days, guichets):
    g = []
    for _ in range(guichets):
        g.append(Guichet())

    time = 0
    waiting_time = [0, 0]
    q = Queue()
    impatient = 0
    apres_fermeture = 0
    for day in range(days):
        for seconds in range(simulation_time):
            if time % arrival_time == 0:
                q.enqueue(Client(time))
            for guichet in g:
                if not q.is_empty() and not guichet.busy():
                    client = q.pop()
                    waiting_time[0] += time - client.get_time()
                    waiting_time[1] += 1
                    guichet.start()
            for client in q.get_queue():
                if client.tick(time):
                    q.remove(client)
                    impatient += 1
            for guichet in g:
                guichet.tick()
            time += 1
            for guichet in g:
                guichet.tick()

        for guichet in g:
            guichet.stop()
        apres_fermeture += q.size()
        q.empty()

    c = 0
    for guichet in g:
        c += guichet.clients

    return waiting_time, impatient, c, apres_fermeture


"""
guichets = int(input("Entrez le nombre de guichets: "))
average_arrival_time = int(input("Un client arrive toutes les n secondes en moyenne. n = "))
simulation_time = int(input("Duree de la simulation: "))
days = int(input("Nombre de simulations: "))

results = simulation(average_arrival_time, simulation_time, days, guichets)
total_clients = results[1] + results[2] + results[3]

print(f"Nombre de clients servis: {results[2]}")
print(f"Nombre de clients impatients partis: {results[1]} ({(results[1] / total_clients) * 100}%)")
print(f"Nombre de clients en attente apres la fermeture du guichet: {results[3]} ({(results[3] / total_clients) * 100}%)")
print(f"Temps moyen d attente: {results[0][0]/results[0][1]} seconds")

"""
