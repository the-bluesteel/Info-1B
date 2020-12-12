from my_main_functions import Queue


class CarWash:
    def __init__(self, tw):
        self.time_wash = tw
        self.time_remaining = 0
        self.washed_cars = 0

    def busy(self):
        return self.time_remaining > 0

    def tick(self):
        if self.busy():
            self.time_remaining -= 1
            if self.time_remaining == 0:
                self.washed_cars += 1

    def get_washed_cars(self):
        return self.washed_cars

    def start_wash(self):
        self.time_remaining = self.time_wash

    def __str__(self):
        return f"Lavage total = [{self.time_wash}] reste = [{self.time_remaining}]"


class Car:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time

    def get_arrival_time(self):
        return self.arrival_time


def washing(arrival_time, washing_time):
    time = 0
    cw = CarWash(washing_time)
    q = Queue()
    waiting_time = [0, 0]
    for days in range(10):
        for seconds in range(36000):
            if time % arrival_time == 0:
                q.enqueue(Car(time))
            if not cw.busy():
                car = q.pop()
                waiting_time[0] += time - car.get_arrival_time()
                waiting_time[1] += 1
                cw.start_wash()
            time += 1
            cw.tick()
    return cw.get_washed_cars(), waiting_time, q.size()



"""
b = int(input("Temps pour laver une voiture: "))
a = int(input("Une voiture arrive toutes les n secondes en moyenne. n = "))
print("Duree de la simulation: 36000 seconds")
print("Nombre de simulations: 10")
results = washing(a, b)

print(f"Nombre de voitures lavees: {results[0]}")
print(f"Nombre de voitures non lavees: {results[2]}")
print(f"Temps moyen d attente: {results[1][0]/results[1][1]}")
"""

