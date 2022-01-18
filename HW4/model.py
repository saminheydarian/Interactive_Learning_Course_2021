import numpy as np
import copy
from gym import Env
import datetime

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

def set_max_min(var,maximum,minimum):
    return min(max(var,minimum),maximum)

def make_map(studentNum):
    np.random.seed(studentNum)  
    move = np.zeros(6)
    idx = np.random.choice(range(6),size=3,replace=False)
    move[idx] = 1

    point = [0,0]
    lowprobs = [tuple(point)]

    for m in move:
        if m:
            point[0] += 1
        else:
            point[1] += 1
        lowprobs.append(tuple(point))
    
    map = np.random.rand(4,4)
    idx = np.array(lowprobs)

    map[idx[:,0],idx[:,1]] = 0.001 
    map[0,0] = 0.0
    map[3,3] = 0.0 

    return map


class NSFrozenLake(Env):
    def __init__(self,studentNum:int=256, nonStationary = False):
        self.studentNum = studentNum
        self.nonStationary = nonStationary
        
        np.random.seed(self.studentNum)
        ##### changed {
        self.beginMap = make_map(self.studentNum) #*2
        self.beginMap[self.beginMap>1] = 1
        self.endMap = make_map(self.studentNum + 100)
        
        self.changeDir = self.endMap - self.beginMap
        self.changeDir *= 1/11000

        self.fixedMap = self.beginMap

        np.random.seed(datetime.datetime.now().microsecond)
        
        self.map = copy.deepcopy(self.fixedMap)
        self.time = 0
        self.reset()

    def reset(self):
        self.NSreset()
        if not self.nonStationary:
            self.map = copy.deepcopy(self.fixedMap)
            self.time = 0
        return self.state

    def NSreset(self):
        self.time += 1
        self.map += self.changeDir

        self.map[self.map>0.95]=0.95
        self.map[self.map<0.0]=0.0

        self.state = (0,0)
        self.done = False
        return self.state
    
    def states_transitions(self, state, action):
        x = state[0]
        y = state[1]
        states = np.array([[x,y-1], [x,y+1], [x-1 ,y], [x+1,y] ])

        if action == UP:
            selected = states[2]
        if action == DOWN:
            selected = states[3]
        if action == RIGHT:
            selected = states[1]
        if action == LEFT:
            selected = states[0]

        zero = np.zeros((4,2)).astype(int)
        three = (3 * np.ones((4,2))).astype(int)
        output = np.maximum(np.minimum(states, three),zero)
        output, indices = np.unique(output, axis = 0, return_counts= True)
        
        selected = np.maximum(np.minimum(selected, three[0]), zero[0])
        probs = indices * 0.025
        probs[np.argmax(np.sum(selected == output, axis = 1))] += 0.9

        return list(zip(output[:,0],output[:,1])), probs
    
    def possible_consequences(self,action:int,state_now=None):

        if state_now==None:
            state_now = self.state

        state = [state_now[0],state_now[1]]
        states, probs = self.states_transitions(state, action)
        aa = np.array(states) 
        fail_probs = self.map[(aa[:,0]),(aa[:,1])]
        dones = np.sum(aa == 3, axis = 1) == 2
        return states, probs, fail_probs,dones
    
    def step(self, a:int):
        if not (a in range(4)):
            raise Exception("action is not in range !!!")
        
        states, probs, fail_probs,dones = self.possible_consequences(a)
        
        next_idx = np.random.choice(np.arange(len(states)), p = probs)
        next_state = states[next_idx]
        self.state = tuple(next_state)
        
        self.done = dones[next_idx]

        r = -1

        if self.done:
            r += 50
        elif np.random.rand()< fail_probs[next_idx]:
            r -= 10
            self.done = True

        return (self.state, r, self.done, {})

    def render(self,state=None):
        if state == None:
            state = self.state

        out = ""
        for i in range(4):
            out += "\n------------------------------\n| "
            for j in range(4):
                if (i,j) == state:
                    out += "\033[44m{:.3f}\033[0m | ".format(self.map[i,j])
                else :
                    out += "{:.3f} | ".format(self.map[i,j])

        out += "\n------------------------------"
        print(out)

