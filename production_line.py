import random
from worker import Worker
from component import A, B, P


class ProductionLine:

    def __init__(self, components, weights, length):
        self.components = components  # List of available components
        self.distribution = weights  # List of probabilities
        self.conveyor = [None] * length  # Initial conveyor length
        self.available_slot = [True, True, True]  # Available slot flag used by workers
        self.workers = []
        self.unfinished_component_a = 0
        self.unfinished_component_b = 0
        self.finished_product = 0

    # Generate workers and assign them to position on production line
    def create_workers(self, slot_index, available_index):

        for x in range(3):  # Create 3 pairs of workers
            # Create pair of workers
            self.workers.append(Worker(slot_index, available_index))
            self.workers.append(Worker(slot_index, available_index))
            slot_index += 2
            available_index += 1

    def generate_parts(self):  # Generate parts on line, count how many parts come off line
        for z in self.available_slot:  # reset available slot flag for workers
            self.available_slot[z] = True

        component_type = random.choices(self.components, self.distribution).pop()  # Generate parts
        if component_type == 'A':
            self.conveyor.insert(0, A())
        elif component_type == 'B':
            self.conveyor.insert(0, B())
        else:
            self.conveyor.insert(0, None)

        output = self.conveyor.pop()  # Take last item from conveyor

        if isinstance(output, A):  # Count finished products and unpicked parts
            self.unfinished_component_a += 1
        elif isinstance(output, B):
            self.unfinished_component_b += 1
        elif isinstance(output, P):
            self.finished_product += 1

    def start_working(self):
        for y in range(len(self.workers)):
            self.workers[y].check_hands(self.conveyor, self.available_slot)

