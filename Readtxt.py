import matplotlib.pyplot as plt
import numpy as np
import csv

# specter = np.zeros(10001)
# tof = [2.000000026702864e-10*i for i in range(10001)]

# for i in range(19):
#     with open("Zr"+str(i)+".txt") as f:
#         lines = f.readlines()
#         lines = lines[0].split("\t")
#         lines[-1] = lines[-1].split("\n")[0]
#         lines = [float(l) for l in lines]
#         for j in range(len(specter)):
#             specter[j]+=lines[j]/19

#     with open("Al"+str(i)+".txt") as f:
#         lines = f.readlines()
#         lines = lines[0].split("\t")
#         lines[-1] = lines[-1].split("\n")[0]
#         lines = [float(l) for l in lines]
#         for j in range(len(specter)):
#             specter[j]+=lines[j]/19

# np.save("specter",arr=specter)
# a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
# np.savetxt("foo.csv", a, delimiter=",")

with open("Ne-CH3i_30.csv") as file_name:
    file_read = csv.reader(file_name)
    array = list(file_read)
    array = array[1:]
    x = [float(array[i][0]) for i in range(len(array))]
    y = [float(array[i][1]) for i in range(len(array))]
    

plt.plot(x,y)
plt.show()
