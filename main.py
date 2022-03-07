import random
from component import A, B, P
from worker import Worker
from ProductionLine import ProductionLine


def production_simulation(n):
    unfinished_component_a = 0  # Unfinished part counter
    unfinished_component_b = 0
    finished_product = 0
    line = ProductionLine(['A', 'B', None], [.3, .3, .3], 5)  # Create production line
    # Create workers

    workers = []
    slot_index = 0
    available_slot_index = 0
    for x in range(3):  # Create 3 pairs of workers
        # Create pair of workers
        workers.append(Worker(slot_index, available_slot_index))
        workers.append(Worker(slot_index, available_slot_index))
        slot_index += 2
        available_slot_index += 1

    for x in range(n):  # Run n step of simulation
        for z in line.available_slot:  # reset available slot flag for workers
            line.available_slot[z] = True

        component_type = random.choices(line.components, line.distribution).pop()  # Generate parts
        if component_type == 'A':
            line.conveyor.insert(0, A())
        elif component_type == 'B':
            line.conveyor.insert(0, B())
        else:
            line.conveyor.insert(0, None)
        output = line.conveyor.pop()  # Take last item from conveyor

        if isinstance(output, A):  # Count finished products and unpicked parts
            unfinished_component_a += 1
        elif isinstance(output, B):
            unfinished_component_b += 1
        elif isinstance(output, P):
            finished_product += 1
        del output

        for y in range(len(workers)):
            workers[y].check_hands(line.conveyor, line.available_slot)

    print("Summary A:" + str(unfinished_component_a) + " B:" + str(unfinished_component_b) + " P:" + str(
        finished_product))
    del line


production_simulation(100)
