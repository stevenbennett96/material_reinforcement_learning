import numpy as np
from collections import Counter


class QLearning():
    def __init__(self):
        self.alpha = 0.4
        self.gamma = 0.999
        self.epsilon = 0.017

    def _init_q_table(self):
        self.q = np.matrix((len(states), len(actions)))
        self.q_map = {val : idx for idx, val in enumerate(states)}

    def _update_q_table(
        self,
        prev_state,
        action,
        reward,
        next_state,
        alpha,
        gamma
    ):
        idx_prev_state = self.q_map[prev_state]
        idx_next_state = self.q_map[next_state]
        qa = np.argmax(self.q[idx_next_state, idx_prev_state])
        q[(prev_state, action)] += alpha *
           (reward + gamma * qa - q[(prev_state, action)])

    def _epsilon_greedy_policy(
        state,
        action
    ):
        if np.random.uniform(0, 1) < epsilon:
            return TODO
        else:
            return max(list(range(action_space)), key=lambda x: q[(state, x)])


def get_fingerprint(mol):
    '''
    Gets Morgan fingerprint bit counts.
    '''
    info={}
    fp=rdkit.GetMorganFingerprintAsBitVect(
        mol=mol,
        radius=2,
        nBits=512,
        bitInfo=info,
    )
    fp=list(fp)
    for bit, activators in info.items():
        fp[bit]=len(activators)
    return fp
