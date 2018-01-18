import numpy as np
import time
import sys
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
		goal_origin = np.array([(2*SCALE)+SCALE/2, (2*SCALE)+SCALE/2])
		self.rect = self.canvas.create_rectangle(
            goal_origin[0] - SCALE/2, goal_origin[1] - SCALE/2,
            goal_origin[0] + SCALE/2, goal_origin[1] + SCALE/2,
            fill='red')

		self.canvas.pack()
		# self.reset()

	def reset(self):
		self.update()
		time.sleep(0.5)
		self.canvas.delete(self.rect)
		rect_origin = np.array([SCALE/2, SCALE/2])
		self.rect = self.canvas.create_rectangle(
            rect_origin[0] - SCALE/2, rect_origin[1] - SCALE/2,
            rect_origin[0] + SCALE/2, rect_origin[1] + SCALE/2,
            fill='red')
		# print(self.canvas.coords(self.rect))
		return self.canvas.coords(self.rect)

	def step(self, action):
		self.update()
		time.sleep(0.5)
		s = self.canvas.coords(self.rect)
		base_action = np.array([0,0])
		if action == 0: #up
			if s[1] >= SCALE:
				base_action[1] -= SCALE
		if action == 1: #right
			print(s)
			if s[0] < WIDTH - SCALE:
				base_action[0] += SCALE
		if action == 2: #down
			if s[1] < HEIGHT - SCALE:
				base_action[1] += SCALE
		if action == 3: #left
			if s[0] >= SCALE:
				base_action[0] -= SCALE

		self.canvas.move(self.rect, base_action[0], base_action[1])







