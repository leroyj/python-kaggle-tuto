#!/Users/jleroy/miniforge3/bin/python
from locale import currency
import numpy as np
import time

##
# Implementation of Reinforcement Learning using Q-Learning algorithm
# example: find the way out from the following house
# 
#  +-----+--+
#  |  0  |  |   5  +---+
#  +--  -+  +-  ---+   |
#  |     |  1      |   |
#  | 4   +----  ---| 2 |
#  |     |             |
#  |           3   |   |
#  +--  -+---------+---+
##

# the final reward ($_$)
success_reward = 100
# the discount factor (attenuation of the delta_time/step memory) probability to survive/success
gamma = 0.8
# learning rate
# O means you rely on past knowledge (learn nothing)
# 1 means you only consider newest information
# (1 is optimal for deterministic)
alpha = 1
# number of training iterations
training_iterations=100

# initial Quality matrix
Q = np.zeros((6,6))
print ("Q matrix initialization")
print(Q)
R=np.zeros((6,6))-np.ones((6,6))

# set initial state (room we're in)
initial_state = 2

## Initialize policies
# from room 0 to room 4 
R[0,4]=0
# from room 1 to room 3 (no reward) or 5 (max reward)
R[1,3]=0
R[1,5]=success_reward
# from room 2 to room 3 (no reward)
R[2,3]=0
# from room 3 to room 1 or 2 or 4 (no reward)
R[3,1]=0
R[3,2]=0
R[3,4]=0
# from room 4 to room 0 or 3 (no reward) or 5 (max reward)
R[4,0]=0
R[4,3]=0
R[4,5]=success_reward
# from room 5 to room 1 or 4 (no reward) or 5 (max reward)
R[5,1]=0
R[5,4]=0
R[5,5]=success_reward
print ("R matrix initialization (policies)")
print(R)


##
# Function definition
##

def available_actions(state):
    """return the available actions for a given state

    Args:
        state (int): given state
    Returns:
        Array[int]: index of policy matrix Q 
        
    >>> available_actions(2)
    """
    # return np.where( R[state,:] >=0 )[1]
    return [ index for index,element in enumerate(R[state,:]) if element>=0] 

available_act=available_actions(initial_state)

def update (current_state,action,gamma):
    """rate the quality of the action 

    Args:
        current_state (int): state
        action (int): move to this next state
        gamma (int): attenuation

    >>> next_q(2,3,0.8)
    """
    # print ("DEBUG> from Q[",str(current_state),",",action,"] = ",str(Q[current_state,action]))
    max_index = np.where(Q[action,] == np.max(Q[action,]))[0]
    if max_index.shape[0]>1:
        max_index = int(np.random.choice(max_index,size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]
    # Q learning formula
    Q[current_state,action] = Q[current_state,action] + alpha * (R[current_state,action] + gamma * max_value - Q[current_state,action])
    # print ("DEBUG>                to ",str(Q[current_state,action]))

def try_action(available_actions_range):
    """randomly choose an action from a range of action

    Args:
        available_actions_range ([int]): available actions range

    Returns:
        int: th selected action
        
    >>> try_action([1,2,4])
    """
    return int(np.random.choice(available_actions_range,1))

action = try_action(available_act)

update (initial_state,action,gamma)

##
# Training
##
print("Training...")
for i in range (training_iterations):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = try_action(available_act)
    update(current_state,action,gamma)

print ("Result of training (Q normalized)")
print (np.matrix.round(Q / np.max(Q) * 100, 2))

##
# Testing
# Goal State = 5
# Best sequence path starting from 2 -> 2, 3, 1, 5
## 

current_state=2
steps = [current_state]

while current_state!= 5:
    print ("Current step is ",str(current_state))
    print ("Quality of actions for this state: ", str(np.matrix.round(Q[current_state,])))
    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[0]
    print ("best action to take",next_step_index)
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size=1))
    else:
        next_step_index = int(next_step_index)
    steps.append(next_step_index)
    current_state=next_step_index

print("=> Selected Path:", str(steps))

