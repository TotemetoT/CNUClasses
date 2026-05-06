"""
search.py
---------
Licensing Information:  You are free to use or extend these projects for
educational purposes provided that (1) you do not distribute or publish
solutions, (2) you retain this notice, and (3) you provide clear
attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

Attribution Information: The Pacman AI projects were developed at UC Berkeley.
The core projects and autograders were primarily created by John DeNero
(denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
Student side autograding was added by Brad Miller, Nick Hay, and
Pieter Abbeel (pabbeel@cs.berkeley.edu).

In search.py, you will implement generic search algorithms which are called by
Pacman agents (in search_agents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue

from game import Directions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in this_ojb-oriented terminology: an abstract class).

    You do not need to change anything in this class, EVER.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """
        util.raise_not_defined()

    def is_goal_state(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raise_not_defined()

    def get_successors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raise_not_defined()


def tiny_maze_search(_):  # needs param Problem but doesnt use it, replaced with _
    """
    Returns a sequence of moves that solves tiny_maze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tiny_maze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print(f'Start: {problem.get_start_state()}')
    print(f'Is the start a goal? {problem.is_goal_state(problem.get_start_state())}')
    print(f'Start\'s successors: {problem.get_successors(problem.get_start_state())}')

    NOTE: If you use the above print statements, the get_successors( ) method
    will cause you to show an extra expansion and fail the autograder.
    Be sure to remove the extra call to get_successors() before final submission.
    """

    if problem.is_goal_state(problem.get_start_state()): return []
    visited = set()
    current = problem.get_start_state()
    stack = Stack()
    stack.push((current, []))
    while not stack.is_empty():
        location, path = stack.pop()
        if location in visited:
            continue

        visited.add(location)

        if problem.is_goal_state(location):
            return path

        successors = problem.get_successors(location)
        for move, direction, cost in successors:
            if move not in visited:
                stack.push((move, path + [direction]))
    return []

def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""

    if problem.is_goal_state(problem.get_start_state()): return []
    visited = set()
    queue = Queue()
    queue.push((problem.get_start_state(), []))

    while not queue.is_empty():
        location, path = queue.pop()

        if location in visited:
            continue
        visited.add(location)

        if problem.is_goal_state(location):
            return path

        successors = problem.get_successors(location)
        for move, direction, cost in successors:
            if move not in visited:
                queue.push((move, path + [direction]))
    return []

def uniform_cost_search(problem):
    """Search the node of least total cost first."""

    start = problem.get_start_state()
    if problem.is_goal_state(start):
        return []

    visited = set()
    prio_queue = PriorityQueue()
    prio_queue.push((start, [], 0), 0)

    while not prio_queue.is_empty():
        location, path, cost = prio_queue.pop()

        if location in visited:
            continue
        visited.add(location)

        if problem.is_goal_state(location):
            return path

        for next_state, direction, step_cost in problem.get_successors(location):
            if next_state not in visited:
                new_cost = cost + step_cost
                prio_queue.push((next_state, path + [direction], new_cost), new_cost)

    return []

def null_heuristic(_, __):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    start = problem.get_start_state()
    if problem.is_goal_state(start):
        return []

    visited = set()
    prio_queue = PriorityQueue()
    prio_queue.push((start, [], 0), heuristic(start, problem))  # f = g + h

    while not prio_queue.is_empty():
        location, path, cost = prio_queue.pop()

        if location in visited:
            continue
        visited.add(location)

        if problem.is_goal_state(location):
            return path

        for next_state, direction, step_cost in problem.get_successors(location):
            if next_state not in visited:
                new_cost = cost + step_cost  # g(n)
                priority = new_cost + heuristic(next_state, problem)  # f(n) = g+h
                prio_queue.push((next_state, path + [direction], new_cost), priority)

    return []

# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
