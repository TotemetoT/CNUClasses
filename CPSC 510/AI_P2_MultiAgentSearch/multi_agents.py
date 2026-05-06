"""
multiAgents.py
--------------
Licensing Information:  You are free to use or extend these projects for
educational purposes provided that (1) you do not distribute or publish
solutions, (2) you retain this notice, and (3) you provide clear
attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

Attribution Information: The Pacman AI projects were developed at UC Berkeley.
The core projects and autograders were primarily created by John DeNero
(denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
Student side autograding was added by Brad Miller, Nick Hay, and
Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""


import random
from operator import truediv

import util

from util import manhattan_distance
from game import Agent, Directions


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def get_action(self, game_state):
        """
        You do not need to change this method, but you're welcome to.

        get_action chooses among the best options according to the evaluation function.

        Just like in the previous project, get_action takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legal_moves = game_state.get_legal_actions()

        # Choose one of the best actions
        scores = [self.evaluation_function(game_state, action) for action in legal_moves]
        best_score = max(scores)
        best_indices = [index for index in range(len(scores)) if scores[index] == best_score]
        chosen_index = random.choice(best_indices)  # Pick randomly among the best

        # Add more of your code here if you want to

        return legal_moves[chosen_index]

    def evaluation_function(self, current_game_state, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (new_food) and Pacman position after moving (new_pos).
        new_scared_times holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successor_game_state = current_game_state.generate_pacman_successor(action)
        new_pos = successor_game_state.get_pacman_position()
        new_food = successor_game_state.get_food()
        food_list = new_food.as_list()
        new_ghost_states = successor_game_state.get_ghost_states()
        new_scared_times = [ghost_state.scared_timer for ghost_state in new_ghost_states]

        score = successor_game_state.get_score()

        # Closest Food
        if food_list:
            min_food = min(abs(new_pos[0]-food[0]) + abs(new_pos[1]-food[1])for food in food_list)
        else:
            min_food = 0

        # Ghost Distances
        ghost_pos = [ghost_state.get_position() for ghost_state in new_ghost_states]
        ghost_dist = [abs(new_pos[0] - ghost[0]) + abs(new_pos[1] - ghost[1]) for ghost in ghost_pos]
        if ghost_dist:
            min_ghost_dist = min(ghost_dist)
        else:
            min_ghost_dist = float('inf')

        # Scared Ghosts
        scared_ghost_dists = [dist for ghost_state, dist in zip(new_ghost_states, ghost_dist) if ghost_state.scared_timer > 0]
        min_scared_ghost_dist = min(scared_ghost_dists) if scared_ghost_dists else None

        if min_food > 5:
            score += -2 * (min_ghost_dist + 1)
        elif min_ghost_dist >= 2:
            score += -2 * min_food
        else: score -= 500

        if action == 'Stop':
            score -= 10

        if min_scared_ghost_dist:
            score += 4.0 / (min_scared_ghost_dist + 1)

        return score


def score_evaluation_function(current_game_state):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return current_game_state.get_score()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, eval_fn='score_evaluation_function', depth='2'):
        super().__init__()
        self.index = 0  # Pacman is always agent index 0
        self.evaluation_function = util.lookup(eval_fn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def get_action(self, game_state, agent_index=0, current_depth=0):
        """
    #       Returns the minimax action from the current game_state using self.depth
    #       and self.evaluation_function.
    #
    #       Here are some method calls that might be useful when implementing minimax.
    #
    #       game_state.get_legal_actions(agent_index):
    #         Returns a list of legal actions for an agent
    #         agent_index=0 means Pacman, ghosts are >= 1
    #
    #       game_state.generate_successor(agent_index, action):
    #         Returns the successor game state after an agent takes an action
    #
    #       game_state.get_num_agents():
    #         Returns the total number of agents in the game
    #     """
        num_agents = game_state.get_num_agents()
        depth = self.depth

        if current_depth == depth:
            return self.evaluation_function(game_state)

        legal_actions = game_state.get_legal_actions(agent_index)
        if not legal_actions:
            return self.evaluation_function(game_state)

        next_agent = (agent_index + 1) % num_agents
        next_depth = current_depth + 1 if next_agent == 0 else current_depth

        # Max
        if agent_index == 0:
            best_score = float('-inf')
            best_action = None
            for action in legal_actions:
                successor = game_state.generate_successor(agent_index, action)
                score = self.get_action(successor, next_agent, next_depth)
                if score > best_score:
                    best_score = score
                    best_action = action
            # Top-Level
            if current_depth == 0:
                return best_action
            return best_score

        # Min
        else:
            best_score = float('inf')
            for action in legal_actions:
                successor = game_state.generate_successor(agent_index, action)
                score = self.get_action(successor, next_agent, next_depth)
                if score < best_score:
                    best_score = score
            return best_score


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def get_action(self, game_state):
        alpha = float('-inf')
        beta = float('inf')
        best_value = float('-inf')
        best_action = None

        for action in game_state.get_legal_actions(0):  # Pacman is MAX
            value = self.min_value(game_state.generate_successor(0, action), 1, 0, alpha, beta)
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, best_value)

        return best_action

    def max_value(self, state, agent_index, depth, alpha, beta):
        if depth == self.depth or state.is_win() or state.is_lose():
            return self.evaluation_function(state)

        value = float('-inf')
        for action in state.get_legal_actions(agent_index):
            successor = state.generate_successor(agent_index, action)
            value = max(value, self.min_value(successor, agent_index + 1, depth, alpha, beta))
            if value > beta:  # PRUNE
                return value
            alpha = max(alpha, value)

        return value

    def min_value(self, state, agent_index, depth, alpha, beta):
        if depth == self.depth or state.is_win() or state.is_lose():
            return self.evaluation_function(state)

        value = float('inf')
        next_agent = agent_index + 1
        if next_agent == state.get_num_agents():  # Last Ghost
            next_agent = 0
            next_depth = depth + 1
        else:
            next_depth = depth

        for action in state.get_legal_actions(agent_index):
            successor = state.generate_successor(agent_index, action)
            if next_agent == 0:
                value = min(value, self.max_value(successor, next_agent, next_depth, alpha, beta))
            else:
                value = min(value, self.min_value(successor, next_agent, next_depth, alpha, beta))

            if value < alpha:
                return value
            beta = min(beta, value)

        return value

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def get_action(self, game_state):
        """
          Returns the expectimax action using self.depth and self.evaluation_function

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        best_score = float('-inf')
        best_action = None

        for action in game_state.get_legal_actions(0):  # Pacman (MAX)
            successor = game_state.generate_successor(0, action)
            value = self.expectimax(successor, agent_index=1, depth=0)
            if value > best_score:
                best_score = value
                best_action = action

        return best_action

    def expectimax(self, state, agent_index, depth):
        if depth == self.depth or state.is_win() or state.is_lose():
            return self.evaluation_function(state)

        num_agents = state.get_num_agents()
        next_agent = (agent_index + 1) % num_agents
        next_depth = depth + 1 if next_agent == 0 else depth  # Increase depth only after full round

        if agent_index == 0:
            return self.max_value(state, next_agent, next_depth)
        else:
            return self.exp_value(state, next_agent, next_depth)

    def max_value(self, state, next_agent, next_depth):
        values = []
        for action in state.get_legal_actions(0):
            successor = state.generate_successor(0, action)
            values.append(self.expectimax(successor, next_agent, next_depth))
        return max(values) if values else self.evaluation_function(state)

    def exp_value(self, state, next_agent, next_depth):
        values = []
        actions = state.get_legal_actions(next_agent - 1)  # because caller passed next_agent already
        if not actions:
            return self.evaluation_function(state)
        prob = 1 / len(actions)

        for action in actions:
            successor = state.generate_successor(next_agent - 1, action)
            values.append(prob * self.expectimax(successor, next_agent, next_depth))

        return sum(values)


def better_evaluation_function(current_game_state):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """

    # Useful information you can extract from a GameState (pacman.py)
    successor_game_state = current_game_state
    new_pos = successor_game_state.get_pacman_position()
    new_food = successor_game_state.get_food()
    new_ghost_states = successor_game_state.get_ghost_states()
    food_list = new_food.as_list()
    new_scared_times = [ghost_state.scared_timer for ghost_state in new_ghost_states]

    score = successor_game_state.get_score()

    if food_list:
        min_food = min(abs(new_pos[0] - food[0]) + abs(new_pos[1] - food[1]) for food in food_list)
    else:
        min_food = 0

    ghost_pos = [ghost_state.get_position() for ghost_state in new_ghost_states]
    ghost_dist = [abs(new_pos[0] - ghost[0]) + abs(new_pos[1] - ghost[1]) for ghost in ghost_pos]
    if ghost_dist:
        min_ghost_dist = min(ghost_dist)
    else:
        min_ghost_dist = float('inf')

    if min_food < min_ghost_dist:
        score += -2 * (min_ghost_dist + 1)
    elif min_ghost_dist >= 2:
        score += -2 * min_food
    else:
        score -= 500

    return score

# Abbreviation
better = better_evaluation_function
