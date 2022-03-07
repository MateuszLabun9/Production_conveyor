from production_line import ProductionLine


def production_simulation(n):

    line = ProductionLine(['A', 'B', None], [.3, .3, .3], 5)  # Create production line
    line.create_workers(0, 0)  # Create workers on line

    for x in range(n):  # Run n step of simulation
        line.generate_parts()  # Generate parts
        line.start_working()  # Workers begin working on line

    # Print Results
    print("Summary A:" + str(line.unfinished_component_a) + " B:" + str(line.unfinished_component_b) + " P:" + str(
        line.finished_product))
    del line  # Delete line


production_simulation(100)
