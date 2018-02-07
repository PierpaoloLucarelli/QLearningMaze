import numpy as np

WIDTH = 4
HEIGHT = 4
SCALE = 1

class Maze(object):

	def __init__(self):
		self.actions = ['u', 'r', 'd', 'l']
		self.n_actions = len(self.actions)
		self.hell_blocks = np.array([np.array([2,2]),np.array([3,2]),np.array([1,3])])
		self.goal = np.array([2,3])
		self.actor = np.array([0,0])
		self.enemy = np.array([2,4])
		self.win_count = 0


	def reset(self):
		self.actor = np.array([0,0])
		self.enemy = np.array([2,4])
		return np.append(self.actor, self.enemy)


	def a_step(self,action):

