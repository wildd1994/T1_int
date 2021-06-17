import threading
from time import sleep
import random
forks = 5
philosophers = 5

forks_lock = [threading.Lock() for n in range(forks)]


def philosophers_dinner(right_fork, left_fork, philosopher):
    while True:
        first_fork = min(right_fork, left_fork)
        second_fork = max(right_fork, left_fork)
        forks_lock[first_fork].acquire()
        forks_lock[second_fork].acquire()
        print(f'Философ {philosopher} ест')
        sleep(random.randint(1, 5))
        forks_lock[second_fork].release()
        forks_lock[first_fork].release()


for philosopher in range(philosophers):
    right_fork = philosopher
    left_fork = (philosopher+1) % philosophers
    threading.Thread(target=philosophers_dinner, args=(right_fork, left_fork, philosopher)).start()
