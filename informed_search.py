import heapq
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
    return (x**2 + y**2)^.5

open_list = []
A = Node(3,90,[1,0])
B = Node(3,123,[3,0])
C = Node(3,99,[2,0])
D = Node(3,21,[3,1])
E = Node(3,10000,[0,1])
heapq.heappush(open_list,A) # Second lowest cost. Should be popped second
heapq.heappush(open_list,B)
heapq.heappush(open_list,C) # Third lowest cost. should be popped third
heapq.heappush(open_list,D) # Lowest cost. should be popped first
heapq.heappush(open_list,E)

print(heapq.heappop(open_list).value)
print(heapq.heappop(open_list).value)
print(heapq.heappop(open_list).value)
print("ordering:")
for i in open_list:
    print(i.value)
open_list.index(E)