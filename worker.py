from component import A, B, P


class worker:
    def __init__(self, place_index, pair_index):
        self.place_index = place_index  # Slot index of place where worker is operating
        self.pair_index = pair_index  # Pair index used to check availability of conveyor slot
        self.hands = []  # Worker hands
        self.assembly_time = 4  # Amount of time needed to assembly product
        self.is_busy = False  # Busy flag used to check if worker is in assembling stage

    def put_on_conveyor(self, conveyor):  # Method used to put product on conveyor
        if conveyor[self.place_index] is None:  # Check if conveyor slot is empty
            conveyor[self.place_index] = self.hands[0]  # Put product on conveyor
            self.hands.pop(0)

    def pick_item(self, conveyor, available):  # Pick item from conveyor
        self.hands.append(conveyor[self.place_index])  # Pick item
        conveyor[self.place_index] = None  # Update conveyor slot
        available[self.pair_index] = False  # Block availability for the worker opposite (in pair)

    def assembly_product(self, conveyor):  # Finish product and try to put it on conveyor
        self.hands.clear()
        self.hands.append(P())  # Create product
        self.is_busy = False  # Change working status
        self.assembly_time = 4  # Update time
        self.put_on_conveyor(conveyor)  # Try to put product on conveyor

    def check_hands(self, conveyor, available):  # Method to check if item could be picked or placed on conveyor
        if self.is_busy:  # If worker is assembling product
            self.assembly_time -= 1
            if self.assembly_time == 0:  # Check if worker finished assembling
                self.assembly_product(conveyor)

        elif available[self.pair_index]:  # Check if slot is available for worker
            if not self.hands:  # If hands are empty
                if isinstance(conveyor[self.place_index], A) or isinstance(conveyor[self.place_index], B):
                    self.pick_item(conveyor, available)

            elif any(isinstance(x, A) for x in self.hands) and len(self.hands) < 2:  # If part A is in worker's hands
                # And second hand is empty
                if isinstance(conveyor[self.place_index], B):  # Check if part B is on belt
                    self.pick_item(conveyor, available)  # Pick item from conveyor
                    self.is_busy = True  # Worker start assembling

            elif any(isinstance(x, B) for x in self.hands) and len(self.hands) < 2:  # If part B is in worker's hands
                # And second hand is empty
                if isinstance(conveyor[self.place_index], A):  # Check if part A is on belt
                    self.pick_item(conveyor, available)  # Pick item from conveyor
                    self.is_busy = True  # Worker start assembling

            elif any(isinstance(x, P) for x in self.hands) and len(
                    self.hands) < 2:  # If product is in worker's hand and second hans is empty
                if isinstance(conveyor[self.place_index], A) or isinstance(conveyor[self.place_index], B):
                    self.pick_item(conveyor, available)  # Pick item from conveyor
                elif conveyor[self.place_index] is None:  # If its None, worker can put finished product on conveyor
                    self.put_on_conveyor(conveyor)
            elif any(isinstance(x, P) for x in self.hands):  # When worker have product and component in hand already
                if conveyor[self.place_index] is None:
                    self.put_on_conveyor(conveyor)
