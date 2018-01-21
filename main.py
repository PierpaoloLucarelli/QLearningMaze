from env import Maze
from rl_brain import QLearn
import time

TEST = False

def update():
	start_time = time.time()
	for episode in range(5000):
		# initial observation
		observation = env.reset()
		print(episode)
		while True:
			# fresh env
			slow = False
			# if(episode > 4900):
			# 	slow = True
			env.render(slow)

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
	RL.save_Qtable()

def run_optimal():
	RL.load_Qtable()
	for episode in range(20):
		observation = env.reset()
		while(True):
			slow = True
			env.render(slow)
			action = RL.choose_action(str(observation))
			observation_, reward, done = env.step(action)
			observation = observation_
			if done:
				break
	env.destroy()
	print(env.get_game_stats())

if __name__ == '__main__':
	env = Maze()
	if(TEST):
		RL = QLearn(actions=list(range(env.n_actions)))
		env.after(100, update)
		env.mainloop()
	else:
		RL = QLearn(actions=list(range(env.n_actions)), e_greedy=1.0)
		env.after(100, run_optimal)
		env.mainloop()
