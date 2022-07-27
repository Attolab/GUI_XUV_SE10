import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.stats import norm

specter = np.zeros(10001)
tof = [2.000000026702864e-10*i for i in range(10001)]

#This is used for reading .txt files and combining specters with Al and Zr filters, check CXRO

# with open("Ne- calibration 30 V retarding potential_0.txt") as f:
#     lines = f.readlines()
#     lines = lines[0].split("\t")
#     lines[-1] = lines[-1].split("\n")[0]
#     lines = [float(l) for l in lines]
#     lines = np.array(lines)


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

#This is used to save an array into an .npy file to be read later

# np.save("Ne30",arr=lines)
# a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
# np.savetxt("foo.csv", a, delimiter=",")

#This is used to read a csv file and plot it with gaussians for comparison

#You have to put the csv in the same folder as of now
with open("Ne-CH3i_20_Xe_calib.csv") as file_name:
    file_read = csv.reader(file_name)
    array = list(file_read)
    array = array[1:]
    x = [float(array[i][0]) for i in range(len(array))]
    y = [float(array[i][1]) for i in range(len(array))]

omega = 1.54 #differnce between harmonic and sideband

def gaussian(x,peak,sigma):
    g=0
    for i in range(5):
        #always a 2 : 1 difference between binding energies peaks
        g += 0.2*norm.pdf(x, loc = peak+2*omega*i, scale = sigma)
        g += 0.4*norm.pdf(x, loc = peak+1.8+2*omega*i, scale = sigma)

        #for sidebands

        # g -= 0.01*norm.pdf(x, loc = peak+omega*(2*i+1), scale = sigma)
        # g -= 0.02*norm.pdf(x, loc = peak+1.8+omega*(2*i+1), scale = sigma)
    return g


peak = 57*omega-58.4 #first harmonic to plot
sigma = 0.3 #width
y_fit = np.zeros(len(y))

for j in range(len(y_fit)):
     y_fit[j] = gaussian(x[j],peak,sigma)


plt.figure()

plt.plot(x,y)
plt.plot(x,y_fit)

plt.xlabel("Energie (eV)")
plt.ylabel("Signal (mV)")

plt.xlim(25, 50)
# plt.ylim(-0.1,0.1)

plt.show()
