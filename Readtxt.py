import matplotlib.pyplot as plt
import numpy as np

specter = np.zeros(10001)
tof = [2.000000026702864e-10*i for i in range(10001)]

for i in range(19):
    with open("Zr"+str(i)+".txt") as f:
        lines = f.readlines()
        lines = lines[0].split("\t")
        lines[-1] = lines[-1].split("\n")[0]
        lines = [float(l) for l in lines]
        for j in range(len(specter)):
            specter[j]+=lines[j]/19

    with open("Al"+str(i)+".txt") as f:
        lines = f.readlines()
        lines = lines[0].split("\t")
        lines[-1] = lines[-1].split("\n")[0]
        lines = [float(l) for l in lines]
        for j in range(len(specter)):
            specter[j]+=lines[j]/19

np.save("specter",arr=specter)

plt.plot(tof,specter)
plt.show()