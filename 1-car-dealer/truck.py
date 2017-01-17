from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self):
        self.ccm = None
        self.top_speed = None
        self.carry_limit = None
        self.current_carriage_weight = 0

    def has_carriage(self):
        if self.current_carriage_weight > 0:
            return True
        else:
            return False

    def attach_carriage(self, carriage):
        if carriage > self.carry_limit:
            return False
        else:
            return True

    def detach_carriage(self):
        self.current_carriage_weight = None
