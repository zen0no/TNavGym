import gym
import os

import logging
import uuid
from deepfield import Field


FIELD_CONFIG = {

}

class ReservoirGym(gym.Env):
    def __init__(self, gdm_path, tnav_exec_path, data_path, loglevel="INFO"):
        super().__init__()

        self.tnav_exec_path = tnav_exec_path

        self.logging_path = data_path

        self.model = Field(gdm_path, config=FIELD_CONFIG).load()
        self.env_steps = 0

        self._logger = logging.getLogger('ReservoirGym')
        self._logger.setLevel(getattr(logging, loglevel))

        if not os.path.exists(data_path):
            self._logger.warn("Data path not found, creating it")
            os.makedirs(data_path)
        elif not os.listdir(data_path):
            self._logger.warn("Data path is not empty, errors may occur while working")
        
        self.data_path = data_path
                 
        



    def  step(self, action):
        """TODO: make this function return next observation"""
        reward = self._make_action(action)
        obs = self._get_observation()
        done = self._state_is_done(obs)

        self.env_steps += 1

        return obs, reward, done


    def reset(self):
        """Resets environment """
        self.model.load()
        self.run_title = f"resenv_{uuid.uuid4()}"
        
        self.model.dump(path=self.data_path, title=self.run_title)

        self.env_steps = 0

        obs0 = self._get_observation()
        reward,  is_done = 0, False
        return obs0, reward, is_done



    def _run_simulation(self):
        """TODO: make this function run simulation of the env"""
        pass

    def _get_observation(self):
        """This function returns observation of the current model state
        """
        pass

    def _make_action(self, action):
        reward = 0
        return reward

    def _state_is_done(self, state):
        return False