import numpy as np
import time
import sys
from random import randint
if sys.version_info.major == 2:
	import Tkinter as tk
else:
	import tkinter as tk


WIDTH = 400
HEIGHT = 400
SCALE = 80

class Maze(tk.Tk, object):
	# constructor
	def __init__(self):
		super(Maze, self).__init__()
		self.actions = ['u', 'r', 'd', 'l']
		self.n_actions = len(self.actions)
		self.title('qmaze')
		self.geometry('{0}x{1}'.format(WIDTH, HEIGHT))
		self.build_maze()

	# create env maze
	def build_maze(self):
		self.canvas = tk.Canvas(self, bg='white',
						   height=HEIGHT,
						   width=WIDTH)
		# make grid
		#rows
		for r in range(0, WIDTH, SCALE):
			x0, y0, x1, y1 = 0, r, WIDTH, r
			self.canvas.create_line(x0, y0, x1, y1)
		# columns
		for c in range(0, HEIGHT, SCALE):
			x0, y0, x1, y1 = c, 0, c, HEIGHT
			self.canvas.create_line(x0, y0, x1, y1)

		bad_origin = np.array([2*SCALE, 2*SCALE]);
		# bad blocks

		bad_center = bad_origin + np.array([SCALE/2, SCALE/2])
		self.bad1 = self.canvas.create_rectangle(
			bad_center[0] - SCALE/2, bad_center[1] - SCALE/2,
			bad_center[0] + SCALE/2, bad_center[1] + SCALE/2,
			fill='black')
		bad_origin2 = np.array([3*SCALE, 2*SCALE]);
		bad_center2 = bad_origin2 + np.array([SCALE/2, SCALE/2])
		self.bad2 = self.canvas.create_rectangle(
			bad_center2[0] - SCALE/2, bad_center2[1] - SCALE/2,
			bad_center2[0] + SCALE/2, bad_center2[1] + SCALE/2,
			fill='black')
		bad_origin3 = np.array([1*SCALE, 3*SCALE]);
		bad_center3 = bad_origin3 + np.array([SCALE/2, SCALE/2])
		self.bad3 = self.canvas.create_rectangle(
			bad_center3[0] - SCALE/2, bad_center3[1] - SCALE/2,
			bad_center3[0] + SCALE/2, bad_center3[1] + SCALE/2,
			fill='black')

		# goal
		goal_center = np.array([2*SCALE, 3*SCALE])
		oval_center = goal_center + np.array([SCALE/2, SCALE/2])
		self.oval = self.canvas.create_oval(
			oval_center[0] - SCALE/2, oval_center[1] - SCALE/2,
			oval_center[0] + SCALE/2, oval_center[1] + SCALE/2,
			fill='yellow')

		# actor
		goal_origin = np.array([SCALE/2,SCALE/2])
		self.rect = self.canvas.create_rectangle(
			goal_origin[0] - SCALE/2, goal_origin[1] - SCALE/2,
			goal_origin[0] + SCALE/2, goal_origin[1] + SCALE/2,
			fill='green')

		# enemy
		enemy_origin = np.array([2*SCALE, 4*SCALE])
		enemy_center = enemy_origin + np.array([SCALE/2, SCALE/2])
		self.enemy = self.canvas.create_rectangle(
			enemy_center[0] - SCALE/2, enemy_center[1] - SCALE/2,
			enemy_center[0] + SCALE/2, enemy_center[1] + SCALE/2,
			fill='red')

		self.canvas.pack()

	def reset(self):
		# self.update()
		# time.sleep(0.5)
		self.canvas.delete(self.rect)
		self.canvas.delete(self.enemy)

		rect_origin = np.array([SCALE/2, SCALE/2])
		self.rect = self.canvas.create_rectangle(
			rect_origin[0] - SCALE/2, rect_origin[1] - SCALE/2,
			rect_origin[0] + SCALE/2, rect_origin[1] + SCALE/2,
			fill='green')

		# enemy
		enemy_origin = np.array([2*SCALE, 4*SCALE])
		enemy_center = enemy_origin + np.array([SCALE/2, SCALE/2])
		self.enemy = self.canvas.create_rectangle(
			enemy_center[0] - SCALE/2, enemy_center[1] - SCALE/2,
			enemy_center[0] + SCALE/2, enemy_center[1] + SCALE/2,
			fill='red')

		# print(self.canvas.coords(self.rect))
		return self.canvas.coords(self.rect)

	def step(self, action):
		self.update()
		time.sleep(0.1)
		s = self.canvas.coords(self.rect)
		enemy_s = self.canvas.coords(self.enemy)
		base_action, oob = self.action_outcome(action, s)
		self.canvas.move(self.rect, base_action[0], base_action[1])
		enemy_base_action = self.action_outcome(randint(0,3), enemy_s)[0]
		self.canvas.move(self.enemy, enemy_base_action[0], enemy_base_action[1])
		# get next state
		s_ = self.canvas.coords(self.rect)
		enemy_s = self.canvas.coords(self.enemy)
		# get the reward
		r, done = self.reward(s_, enemy_s, oob)
		return s_, r, done

	def reward(self, state, enemy_state, oob):
		if state == self.canvas.coords(self.oval):
			r = 1
			done = True
		elif state in [self.canvas.coords(self.bad1), self.canvas.coords(self.bad2), self.canvas.coords(self.bad3)] or oob == True:
			r = -1
			done = True
		elif np.array_equal(state, enemy_state):
			r = -1
			done = True
		else:
			r = 0
			done = False
		return r, done

	def action_outcome(self, action, s):
		oob = False
		base_action = np.array([0,0])
		if action == 0: #up
			if s[1] >= SCALE:
				base_action[1] -= SCALE
			else:
				oob = True
		elif action == 1: #right
			if s[0] < WIDTH - SCALE:
				base_action[0] += SCALE
			else:
				oob = True
		elif action == 2: #down
			if s[1] < HEIGHT - SCALE:
				base_action[1] += SCALE
			else:
				oob = True
		elif action == 3: #left
			if s[0] >= SCALE:
				base_action[0] -= SCALE
			else:
				oob = True
		return base_action, oob

	def render(self):
		time.sleep(0.1)
		self.update()







