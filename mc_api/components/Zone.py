from .Coordinates import BlockCoordinates

class Zone:
    """
    Custom component that is a set of two Coordinates(), representing
    a rectangular area
    """
    def __init__(self, pos1: BlockCoordinates or tuple, 
                        pos2: BlockCoordinates or tuple):

        self.pos1 = pos1
        self.pos2 = pos2

        if type(pos1) is tuple:
            self.pos1 = BlockCoordinates(*pos1)
        else:
            self.pos1 = pos1

    def __repr__(self):
        return (f'{repr(self.pos1)} {repr(self.pos2)}')
    