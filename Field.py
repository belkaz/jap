import Cell

class Field:
    def __init__(self, width, height):
        self.field = []
        self.width = width
        self.height = height

        for i in range ( height ):
            self.field.append([])
            for j in range ( width ):
                self.field[i].append(Cell.Cell(i, j))

    def printField(self):
        for i in range (self.height):            
            print (1)    
                        