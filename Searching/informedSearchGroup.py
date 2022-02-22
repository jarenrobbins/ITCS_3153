class Node():
    def __init__(self, g, h, value = [0,0], parent = None):
        self.value = value
        self.parent = parent
        self.h = h #cost of node (heuristic cost)
        self.g = g #path cost
        self.f = g + h 
    def __lt__(self, other):
        return self.f < other.f
    
    
def heuristic(Node_Coordinate,Goal_Coordinate):
    # Calculate the Diagonal Distance
    x = Node_Coordinate[1] - Goal_Coordinate[1]
    y = Node_Coordinate[0] - Goal_Coordinate[0]
    return (x**2 + y**2)**.5
