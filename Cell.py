class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0
        self.colOwner = None
        self.rowOwner = None
