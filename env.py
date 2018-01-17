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

		self.canvas.pack()



