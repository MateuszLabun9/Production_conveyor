import random
from component import A, B, P
from worker import worker
from ProductionLine import ProductionLine


def production_simulation(n):
    unfinished_component_a = 0  # Unfinished part counter
    unfinished_component_b = 0
    finished_product = 0
    line = ProductionLine(['A', 'B', None], [.3, .3, .3], 5)  # Create production line
    # Create workers
    worker1 = worker(0, 0)
    worker2 = worker(0, 0)
    worker3 = worker(2, 1)
    worker4 = worker(2, 1)
    worker5 = worker(4, 2)
    worker6 = worker(4, 2)

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

        worker1.check_hands(line.conveyor, line.available_slot)
        worker2.check_hands(line.conveyor, line.available_slot)
        worker3.check_hands(line.conveyor, line.available_slot)
        worker4.check_hands(line.conveyor, line.available_slot)
        worker5.check_hands(line.conveyor, line.available_slot)
        worker6.check_hands(line.conveyor, line.available_slot)

    print("Summary A:" + str(unfinished_component_a) + " B:" + str(unfinished_component_b) + " P:" + str(
        finished_product))


production_simulation(100)
