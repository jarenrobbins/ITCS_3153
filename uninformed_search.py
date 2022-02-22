class Node():
    def __init__(self,value = [0,0], parent = None):
        self.value = value
        self.parent = parent
def getNeighbors(location,grid):
    list_coord = []
    
    # grid_dim[0] = num rows
    # grid_dim[1] = num cols
    grid_dim = [len(grid),len(grid[0])]
    
    row, col = location[0], location[1]
    # can we go left?
    if(col - 1 >= 0 and grid[row][col-1] != 0):
        list_coord.append([row,col-1])
    # can we go right?
    if(col + 1 <= grid_dim[1] - 1 and grid[row][col + 1] != 0):
        list_coord.append([row,col + 1])
    # up?
    if(row - 1 >= 0 and grid[row - 1][col] != 0):
        list_coord.append([row-1,col])
    # down?
    if(row + 1 <= grid_dim[0] - 1 and grid[row+1][col] != 0):
        list_coord.append([row+1,col])

    
    return list_coord
# Get the node's neighbors using getNeighbors
# Since open_list and closed_list have nodes in it, we need to access
# their location.
# Make 2 lists that store the locations of the closed nodes and open nodes
# Using our neighbors we just got:
# iterate through the neighbors and add it to open_list if and only if
# this location (this node) is not in open_list and is not in closed_list
# If we need to add a location, then create a new node with
# it's value being the location: open_list.append(Node(current_neighbors[i]))
# At the end, append the original node we passed in into the closed_list.


def expandNode(node_input,grid,closed_list,open_list):
    # Get the neighbors
    current_neighbors = getNeighbors(node_input.value,grid)
    # use a list comprhension to get the actual coordinates for both closed list and open list
    open_list_locations = [nodes.value for nodes in open_list]
    closed_list_locations = [nodes.value for nodes in closed_list]
    
    # loop through our neighbors:
    for i in range(len(current_neighbors)):
        # Add it to the open list if this location is NOT in open list and NOT in closed lists
        if current_neighbors[i] not in open_list_locations and current_neighbors[i] not in closed_list_locations:
            # Add it to the open_list which stores nodes so create a new one
            open_list.append(Node(current_neighbors[i],node_input))

# TESTING expandNode() method
a = [[1,1,1],[1,1,1],[1,1,1]]
b = Node([0,0])
c = Node([1,0])
closed_list = [b,c]
open_list = [Node([2,1])]

expandNode(Node([1,1]),a,closed_list,open_list)
for B in open_list:
    print(B.value)
print("aa")
for A in closed_list:
    print(A.value)
