'''
    CS386-02, Fall 2024
    Assignment #2

    Jeongyeon Lim (20816838)
'''

from search_algorithms import breadth_first_search, depth_first_search
from mars_planner import *
from routefinder import *
from antennae import *


''' question #2 '''

s = RoverState()
print("<bfs: mission_complete>")
result_bfs = breadth_first_search(s, action_list, mission_complete)
print(result_bfs)
print()
print()
print("<dfs: misstion_complete>")
result_dfs = depth_first_search(s, action_list, mission_complete)
print(result_dfs)
print()
print()
print("<bfs: problem decomposition>")
# move to sample
print("1. move to sample")
result_move = breadth_first_search(s, action_list, move_to_sample_goal)
print()
# remove sample
print("2. remove sample")
result_remove = breadth_first_search(result_move[0], action_list, remove_sample_goal)
print()
# return to charger
print("3. return to charger")
result_return = breadth_first_search(result_remove[0], action_list, return_to_charger_goal)
print()
print()
print("<dfs: problem decomposition>")
# move to sample
print("1. move to sample")
result_move = depth_first_search(s, action_list, move_to_sample_goal)
print()
# remove sample
print("2. remove sample")
result_remove = depth_first_search(result_move[0], action_list, remove_sample_goal)
print()
# return to charger
print("3. return to charger")
result_return = depth_first_search(result_remove[0], action_list, return_to_charger_goal)
print()
print()

''' question #3 '''

mars_graph = read_mars_graph("mars_map.txt")
start_state = map_state(location="8,8", mars_graph=mars_graph)

print("<A* Search>")
a_star(start_state, sld, map_state.is_goal)
print()

print("<Uniform Cost Search>")
a_star(start_state, h1, map_state.is_goal)
print()
print()

''' question #4 '''
assign_frequencies()