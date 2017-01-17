class Door:
    id = None
    is_open = None

    def __init__(self, id):
        self.is_open = False
        self.id = id

    def toggle(self):
        self.is_open = not self.is_open

    def __str__(self):
        print(str(self.id) + ": " + str(self.is_open))
