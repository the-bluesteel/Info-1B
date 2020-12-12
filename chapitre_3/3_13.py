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
        self.remaining_time = randint(30, 5*60)

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


def simluation(arrival_average, simulation_time, days):
    time = 0
    waiting_time = [0, 0]
    g = Guichet()
    q = Queue()
    impatient_clients = 0
    apres_fermeture = 0
    for day in range(days):
        for second in range(simulation_time):
            if time % arrival_average == 0:
                q.enqueue(Client(time))

            if not g.busy() and not q.is_empty():
                client = q.pop()
                waiting_time[0] += time - client.get_time()
                waiting_time[1] += 1
                g.start()

            for client in q.get_queue():
                if client.tick(time):
                    q.remove(client)
                    impatient_clients += 1

            g.tick()
            time += 1

        apres_fermeture += q.size()
        g.stop()
        q.empty()

    return g.clients, impatient_clients, apres_fermeture, waiting_time



"""
average_client_time = int(input("Un client arrive toutes les n secondes en moyennes. n = "))
simulation_time = int(input("Duree de la simulation: "))
days = int(input("Nombre de simulations: "))
results = simluation(average_client_time, simulation_time, days)
total_clients = results[0] + results[1] + results[2]

print(f"Nombre de clients servis: {results[0]}")
print(f"Nombre de clients impatients partis: {results[1]} ({(results[1] / total_clients) * 100}%)")
print(
    f"Nombre de clients en attente apres la fermeture du guichet: {results[2]} ({(results[2] / total_clients) * 100}%)")
print(f"Temps moyen d attente: {results[3][0] / results[3][1]} seconds")
"""


