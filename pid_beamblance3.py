import gym
import ballbeam_gym
import matplotlib.pyplot as plt
import math

kwargs = {'timestep': 0.05, 
          'beam_length': 1.0,
          'max_angle': 0.5,
          'init_velocity': 0.5,
          'max_timesteps': 100,
          'setpoint':0,
          'action_mode': 'continuous'
          }

env = gym.make('BallBeamSetpoint-v0', **kwargs)
obs=env.reset()

#Values of constants
kp=0.9
ki=0.03
kd=0.005
pos=0.01
ei=0
e_old=0

pos_arr=[]
t_arr=[]

for i in range(100):
    t_arr.append(i/20)
    e=0-pos
    ei=ei+e
    ed=(e-e_old)/0.05
    pos=kp*e+ki*ei+kd*ed #PID control
    pos_arr.append(pos)
    # print(pos)
    theta=math.tanh(pos) # Using the tan hyperbolic function to map position values between -1 and 1,and thus keep theta in this range
    # angle=theta/2
    # print(angle)
    # print(pos, theta)
    # print(obs)

    obs,done,reward,info=env.step(theta)

    env.render()

env.reset()

# print(t_arr)
# print(pos_arr)
plt.plot(t_arr,pos_arr)
plt.show()