## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search, depth_first_search

class RoverState :
    def __init__(self, loc="station", sample_extracted=False, holding_tool=False, holding_sample=False, charged=False):
        self.loc = loc
        self.sample_extracted=sample_extracted
        self.holding_tool = holding_tool
        self.holding_sample = holding_sample
        self.charged=charged
        self.prev = None
        self.depth = 0

    ## you do this.
    def __eq__(self, other):
        if other is None:
            return False
        return (self.loc == other.loc and
                self.sample_extracted == other.sample_extracted and
                self.holding_sample == other.holding_sample and
                self.charged == other.charged and 
                self.holding_tool == other.holding_tool)

    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}")

    def __hash__(self):
        return self.__repr__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.
def pick_up_tool(state):
    r2 = deepcopy(state)
    r2.holding_tool = True
    r2.prev = state
    return r2

def drop_tool(state):
    r2 = deepcopy(state)
    r2.holding_tool = False
    r2.prev = state
    return r2

def use_tool(state):
    r2 = deepcopy(state)
    if state.holding_tool and state.loc == "sample":
        r2.sample_extracted = True
    r2.prev = state
    return r2

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev=state
    return r2
def move_to_station(state) :
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2
# add tool functions here


def pick_up_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "station":
        r2.holding_sample = False
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.charged = True
    r2.prev = state
    return r2


action_list = [charge, drop_sample, pick_up_sample,
               move_to_sample, move_to_battery, move_to_station, pick_up_tool, drop_tool, use_tool]

def battery_goal(state) :
    return state.loc == "battery"

def charged_goal(state):
    return state.charged

def sample_goal(state):
    return state.sample_extracted and not state.holding_sample

def mission_complete(state) :
    return (state.loc == "battery"
            and state.charged
            and state.sample_extracted
            and not state.holding_sample)

# question #2-6: problem decomposition
def move_to_sample_goal(state):
    return state.loc == "sample"

def remove_sample_goal(state):
    return state.holding_sample and state.sample_extracted

def return_to_charger_goal(state):
    return state.loc == "battery"

if __name__=="__main__" :
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




