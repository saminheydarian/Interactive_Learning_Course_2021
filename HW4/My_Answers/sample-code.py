#%% imports
from model import NSFrozenLake
import numpy as np

#%% allowed actions
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

ACTIONS = [LEFT,DOWN,RIGHT,UP]

#%% hyperparameters
REPS = 20
EPISODES = #100
EPSILON = 0.1
LEARNING_RATE = 0.1
DISCOUNT = 0.9
STUDENT_NUM = # 810198253

#%% get familiar with the environment
environment = NSFrozenLake(studentNum=STUDENT_NUM)

print("you can see the environment in each step by render command :")
environment.render()
print("\n\nand this is the bare map for debugging :")
print(environment.map)

#%% base code for Q1
environment = NSFrozenLake(studentNum=STUDENT_NUM)

for s0 in range(...):
    for s1 in range(...):
        for action in ....:
            states, probs, fail_probs, dones = environment.possible_consequences(action=action ,state_now=(s0,s1))

#%% base code for Q2

env = NSFrozenLake(studentNum=STUDENT_NUM)

for rep in range(REPS): 
    agent = # Agent Object instance from Algorithm_name(e.g Q_learning_agent) class which has inherited from Agentbase.
    for episode in range(EPISODES):
        env.reset()


        for ... :

            bestAction = np.random.choice(ACTIONS)

            next_state,rew,done,_ = environment.step(bestAction)
            
            if done:
                break

# Plot mean Cumulative Reward 


#%% base code for Q3
env = NSFrozenLake(studentNum=STUDENT_NUM,nonStationary=True)

for rep in range(REPS): 
    agent = # Agent Object instance from Algorithm_name(e.g Q_learning_agent) class which has inherited from Agentbase.
    for episode in range(EPISODES):
        env.reset()


        for ... :

            bestAction = np.random.choice(ACTIONS)

            next_state,rew,done,_ = environment.step(bestAction)
            
            if done:
                break
