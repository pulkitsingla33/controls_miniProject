from cProfile import label
from tkinter import E
from turtle import title
import gym
import numpy as np
import math
import matplotlib.pyplot as plt

env=gym.make("CartPole-v1")

# class Error():
#     def pole_angle(c_angle):
#         error=0-c_angle
#         return error
    
#     def cart_position(c_position):
#         error=0-c_position
#         return error

# class Action():
#     def action(error):
#         err=Error(env)
#         pole_angle=state[2]
#         action=0 if err.pole_angle(pole_angle) >0 else 1
#         return action

# class PID():
#     def angle_control(error):
#         err=Error(env)
#         angle_old=state[2]
#         e=err.pole_angle(angle_old)


state=env.reset()
angle_e=0
angle_ei=0
angle_ed=0
angle_kp=0.1
angle_ki=0.02
angle_kd=0.01

velocity_e=0
velocity_ei=0
velocity_ed=0
velocity_kp=0.06
velocity_ki=0.10
velocity_kd=9.5
t_arr=[]
angle_arr=[]
velocity_arr=[]

for _ in range(350):
    t_arr.append(_/0.1)
    
    p_angle=state[2]
    angle_e_new=-1*p_angle
    angle_ei=angle_ei+angle_e_new
    angle_ed=(angle_e_new-angle_e)/0.1
    angle_e=angle_e_new
    p_angle_new=p_angle+angle_kp*angle_e+angle_ki*angle_ei+angle_kd*angle_ed
    # p_angle_new=angle_kp*angle_e+angle_ki*angle_ei+angle_kd*angle_ed
    state[2]=p_angle_new

    velocity=state[1]
    velocity_e_new=-1*velocity
    velocity_ei=velocity_ei+velocity_e_new
    velocity_ed=(velocity_e_new-velocity_e)/0.1
    velocity_e=velocity_e_new
    velocity_new=velocity+velocity_kp*velocity_e+velocity_ki*velocity_ei+velocity_kd*velocity_ed
    state[1]=velocity_new
    # if(p_angle_new<0):  #Try using sigmoid and other mapping functions later
    #     action=0
    # else:
    #     action=1
    action=round(1/(1+math.exp(-p_angle_new)))
    angle_arr.append(p_angle_new)
    velocity_arr.append(velocity_new)
    state, reward, done, info = env.step(action)
    env.render()

plt.subplot(211)
plt.plot(t_arr,angle_arr,label='Pole Angle')

plt.subplot(212)
plt.plot(t_arr,velocity_arr,label='Velocity')

plt.show()