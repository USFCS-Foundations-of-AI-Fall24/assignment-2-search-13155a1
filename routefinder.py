from queue import PriorityQueue
from Graph import *
import math


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True):
    search_queue = PriorityQueue()
    closed_list = {}
    state_count = 0
    search_queue.put(start_state)

    while not search_queue.empty():
        current_state = search_queue.get()
        state_count += 1

        if goal_test(current_state):
            print(f"The number of states generated: {state_count}")
            return current_state 

        if use_closed_list and current_state in closed_list:
            continue

        closed_list[current_state] = True

        edges = current_state.mars_graph.get_edges(current_state.location) or []
        for edge in edges:
            neighbor = edge.dest
            new_g = current_state.g + edge.val
            new_state = map_state(location=neighbor, mars_graph=current_state.mars_graph, 
                                    prev_state=current_state, g=new_g)
            new_state.h = heuristic_fn(new_state)  # 여기서 heuristic_fn 호출
            if use_closed_list and new_state in closed_list:
                continue

            search_queue.put(new_state)

    print(f"The number of states generated: {state_count}")
    return None

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state):
    x, y = map(int, state.location.split(','))
    
    return math.sqrt((x - 1) ** 2 + (y - 1) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph()

    with open(filename, 'r') as file:
        for line in file:
            node, neighbors = line.strip().split(':', 1)
            node = node.strip()
            neighbor_nodes = neighbors.strip().split()

            graph.add_node(node)

            for neighbor in neighbor_nodes:
                graph.add_edge(Edge(node, neighbor.strip()))
    return graph

if __name__ == "__main__":
    mars_graph = read_mars_graph("mars_map.txt")
    start_state = map_state(location="8,8", mars_graph=mars_graph)
    
    print("<A* Search>")
    a_star(start_state, sld, map_state.is_goal)
    
    print("<Uniform Cost Search>")
    a_star(start_state, h1, map_state.is_goal)