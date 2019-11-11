import logging
from models.q_learning import QLearning
from molecules import Molecule
from actions import *

'''Runs the Q-learning algorithm.'''


def main(epochs, epsilon):
    for i in range(epochs):
        r = 0
        # Initialise the environment.
        agent = Molecule()
        q = QLearning()

        state = q._state
        while True:
            prev_state = state
            # Select action using the epsilon-greedy policy.
            action = q.epsilon_greedy_policy(prev_state, epsilon)
            # Take action and proceed to the next state.
            next_state, reward, terminated = agent.step(action)
            q._update_q_table(
                prev_state,
                action,
                reward,
                next_state,
                alpha,
                gamma,
            )
            # Update to the next state.
            prev_state = next_state
            # Store rewards in r.
            r += reward
            logger.info('-'*50+'\n')
            logger.info('Epoch {i}')
            logger.info(agent._state+'\n')
            logger.info(f'Reward: {r}')
            if _is_terminated(epochs):
                break


