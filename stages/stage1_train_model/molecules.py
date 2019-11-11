import stk
'''Defines the Markov Decision Process of creating a cage.
'''


class Molecule:
    def __init__(
        self,

    ):
        '''
        Initialises all the parameters for the Markov Decision Process

        Arguments
        ---------
        molecule : :class:`.ConstructedMolecule`
        '''
        if isinstance(molecule, stk.ConstructedMolecule):
            init_mol = molecule
        self._state = None
        self.init_mol = init_mol
        self._counter = 0
        self.reward = Reward()
        self.termination = termination
        self.reset_state()

        @property
        def _state(self):
            return self.state

        def reset_state(self):
            '''
            Resets the state to initial state.
            '''
            self._state = self.rdkit_mol
            self._counter = 0

        def _reward(self):
            '''
            Returns the reward for the molecule.
            '''
            reward = self.reward.get_reward(self._state)
            return reward

        def _goal_reached(self):
            '''
            Terminates the molecule generation process.
            '''
            if self.termination(self._counter):
                return False
            else:
                return True

        def step(self, action):
            '''
            Take a step by performing an action on the state.
            '''
            self._state = action(self._state)
            self.counter += 1
            terminated = self._goal_reached(self._counter)
            if terminated:
                return False
            self._counter += 1
            return reward
