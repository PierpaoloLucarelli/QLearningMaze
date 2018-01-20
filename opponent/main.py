from env import Maze
from rl_brain import QLearn
import time

def update():
	start_time = time.time()
	for episode in range(100):
		# initial observation
		observation = env.reset()

		while True:
			# fresh env
			env.render()

			# RL choose action based on observation
			action = RL.choose_action(str(observation))

			# RL take action and get next observation and reward
			observation_, reward, done = env.step(action)

			# RL learn from this transition
			RL.learn(str(observation), action, reward, str(observation_), done)

			# swap observation
			observation = observation_

			# break while loop when end of this episode
			if done:
				break
	# end of game
	print "My program took", time.time() - start_time, "to run"
	print('game over')
	env.destroy()

if __name__ == '__main__':
	env = Maze()
	RL = QLearn(actions=list(range(env.n_actions)))
	env.after(100, update)
	env.mainloop()