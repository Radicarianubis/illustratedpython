# Class example, model the flow of skiiers up the hill on a chairlift
import random
import time

class CorrectChair:
    ''' A Chair on a chairlift'''
    max_occupants = 4

    def __init__(self, id):
        self.id = id
        self.count = 0

    def load(self, number):
        new_val = self._check(self.count + number)
        self.count = new_val

    def unload(self, number):
        new_val = self._check(self.count - number)
        self.count = new_val

    def _check(self, number):
        if number < 0 or number > self.max_occupants:
            raise ValueError('invalid count:{}'.format(number))
        return number

NUM_CHAIRS = 100

chairs = []
for num in range(1, NUM_CHAIRS + 1):
    chairs.append(CorrectChair(num))

def avg(chairs):
    total = 0
    for c in chairs:
        total += c.count
    return total/len(chairs)

in_use = []
transported = 0
x = 0
number_of_riders = 42  # Chang this to limit the number of people who can enter the lift
while x != number_of_riders:
    # loading
    loading = chairs.pop(0)
    in_use.append(loading)
    in_use[-1].load(random.randint(0, CorrectChair.max_occupants))

    # unloading
    if len(in_use) > NUM_CHAIRS / 2:
        unloading = in_use.pop(0)
        transported += unloading.count
        unloading.unload(unloading.count)
        chairs.append(unloading)
    print(f'Loading Chair {loading.id} Count:{loading.count} Avg:{avg(in_use):.2} Total:{transported}')
    time.sleep(.25)
    x += 1

# counts the number of time the chairlift slows down since some dumbass didn't get on properly
class StallChair(CorrectChair):
    def __init__(self, id, is_stalled):
        super().__init__(id)
        self.is_stalled = is_stalled
        self.stalls = 0

    def load(self, number):
        if self.is_stalled(number, self):
            self.stalls += 1
        super().load(number)

def ten_percent(number, chair):
    "Return True 10% of the time"""
    return random.random() < .1

stall42 = StallChair(42, ten_percent)
print(stall42.stalls)




