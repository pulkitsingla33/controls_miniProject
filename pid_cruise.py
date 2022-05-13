import imp
import matplotlib.pyplot as plt
import numpy as np

v_ref=10
v_actual=0.1
kp=0.07
ki=0.001
kd=0
ei=0
e_old=0
v_arr=np.array([])
t_arr=np.array([])

for time in range(2000):
    time1=time/1000
    e_new=v_ref-v_actual
    ei=ei+e_new
    ed=(e_new-e_old)/0.001
    e_old=e_new
    v_arr=np.append(v_arr,v_actual)
    v_actual=v_actual+kp*e_new+ki*ei+kd*ed
    t_arr=np.append(t_arr,time1)

# print(v_arr)
plt.plot(t_arr,v_arr)
# print(v_arr)
plt.show()