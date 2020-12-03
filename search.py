# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


class Search_Algo_Implementation:

    def __init__(self, visited_nodes, valid_legal_actions, data_structure, initial_state, problem, hueristic=None,
                 dfs=None, bfs=None):
        self.data_structure = data_structure
        self.visited_nodes = visited_nodes
        self.valid_legal_actions = valid_legal_actions
        self.initial_state = initial_state
        self.problem = problem
        self.hueristic = hueristic
        self.bfs = bfs
        self.dfs = dfs

    def implementation(self):
        while self.data_structure:
            # get current state and current actions
            current_state, current_actions = self.data_structure.pop()
            # print('action', current_actions, 'state', current_state)
            # chek if current not already visited and add to visited nodes if true
            if current_state not in self.visited_nodes:
                self.visited_nodes.append(current_state)
                # print("============",self.visited_nodes, "===================")
                # check if current state is the goal of the problem
                if self.problem.isGoalState(current_state):
                    # print(current_actions)
                    return current_actions

                else:
                    # push next states to queue if the goal is not reach
                    successor_states = self.problem.getSuccessors(current_state)
                    for successor_state in successor_states:
                        x_y_coordinates = successor_state[0]
                        pacman_direction = successor_state[1]

                        get_to_successor_state_actions = [y for x in [current_actions, [pacman_direction]] for y in x]
                        next_successor_state = (x_y_coordinates, get_to_successor_state_actions)
                        # breadthfirst or depthfirst
                        if self.bfs or self.dfs:
                            self.data_structure.push(next_successor_state)
                        else:
                            # astar or uniform
                            if self.hueristic:
                                next_cost = self.problem.getCostOfActions(
                                    get_to_successor_state_actions) + self.hueristic(x_y_coordinates, self.problem)
                                # print('Heuristic')
                            else:
                                next_cost = self.problem.getCostOfActions(get_to_successor_state_actions)
                                # print('uniform')
                            self.data_structure.push(next_successor_state, next_cost)


def uniformCostSearch(problem):
    uniform_cost_search = Search_Algo_Implementation(visited_nodes=[], valid_legal_actions=[],
                                                     data_structure=util.PriorityQueue(),
                                                     problem=problem,
                                                     initial_state=problem.getStartState())

    uniform_cost_search.data_structure.push(
        (uniform_cost_search.initial_state, uniform_cost_search.valid_legal_actions), uniform_cost_search.problem)

    return uniform_cost_search.implementation()


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    astar_search = Search_Algo_Implementation(visited_nodes=[], valid_legal_actions=[],
                                              data_structure=util.PriorityQueue(),
                                              problem=problem, hueristic=heuristic,
                                              initial_state=problem.getStartState())

    astar_search.data_structure.push((astar_search.initial_state, astar_search.valid_legal_actions),
                                     astar_search.hueristic(astar_search.initial_state, astar_search.problem))

    return astar_search.implementation()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    breadth_first_search = Search_Algo_Implementation(visited_nodes=[], valid_legal_actions=[],
                                                      data_structure=util.Queue(),
                                                      problem=problem, bfs=True,
                                                      initial_state=problem.getStartState())

    breadth_first_search.data_structure.push(
        (breadth_first_search.initial_state, breadth_first_search.valid_legal_actions))

    return breadth_first_search.implementation()


def depthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    depth_first_search = Search_Algo_Implementation(visited_nodes=[], valid_legal_actions=[],
                                                    data_structure=util.Stack(),
                                                    problem=problem, dfs=True,
                                                    initial_state=problem.getStartState())

    depth_first_search.data_structure.push((depth_first_search.initial_state, depth_first_search.valid_legal_actions))

    return depth_first_search.implementation()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
