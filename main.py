from maze_env import Maze
from visualiser import Visualiser
from rl_brain import QLearn
import time

TEST = False
N_EPISODES = 5000
def test():
	start_time = time.time()
	for episode in range(N_EPISODES):
		# initial observation
		observation = env.reset()
		if(episode % 500 == 0):
			print(str(float(episode) / N_EPISODES * 100) + "%")
		while True:
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
	RL.save_Qtable()

def run_optimal():
	RL.load_Qtable()
	for episode in range(20):
		observation = env.reset()
		while(True):
			vis.update_canvas(env.actor, env.enemy)
			action = RL.choose_action(str(observation))
			observation_, reward, done = env.step(action)
			observation = observation_
			if done:
				break
	vis.destroy()

if __name__ == '__main__':
	if(TEST):
		env = Maze()
		RL = QLearn(actions=list(range(env.n_actions)))
		test()
	else:
		env = Maze()
		vis = Visualiser(4,4,80, env.hell_blocks, env.goal, env.enemy)
		RL = QLearn(actions=list(range(env.n_actions)), e_greedy=1.0)
		run_optimal()



