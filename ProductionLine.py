class ProductionLine:

    def __init__(self, components, weights, length):
        self.components = components  # List of available components
        self.distribution = weights  # List of probabilities
        self.conveyor = [None] * length  # Initial conveyor length
        self.available_slot = [True, True, True]  # Available slot flag used by workers
