import pygameconstants as pgc

class Coords:
    """
    Class to help deal with the screen coordinates.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, coords):
        return Coords(self.x + coords.x, self.y + coords.y)
    
    def __sub__(self, coords):
        return Coords(self.x - coords.x, self.y - coords.y)
    
    def __mul__(self, scalar):
        return Coords(scalar*self.x, scalar*self.y)

    def __rmul__(self, scalar):
        return Coords(scalar*self.x, scalar*self.y)
    
    def __invert__(self):
        return Coords(self.y, self.x)

    def get(self):
        return (self.x, self.y)


def unit_pos_in_scrn(cur_pos, next_pos, move_prog):
    """
    Calculates the unit position in the screen.
    """
    return (Coords(*pgc.MAP_CORNER_POS) + ~(pgc.GRID_SIZE*(move_prog*Coords(*next_pos) + (1-move_prog)*Coords(*cur_pos)))).get()

