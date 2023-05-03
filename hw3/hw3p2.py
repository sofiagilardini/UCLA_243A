"""
ECE C143/C243 Homework-3 Problem-2

"""
import numpy as np
import matplotlib.pyplot as plt
import nsp as nsp # these are helper functions that we provide.
import scipy.special


# ## 2a
# bin_width = 20                             # (ms)
# s = np.arange(8)*np.pi/4                   # (radians)
# num_cons = np.size(s)                      # num_cons = 8 in this case, number of directions
# print("s is", s)
# print("num_cons is", num_cons)
# r_0 = 35 # (spikes/s)
# r_max = 60 # (spikes/s)
# s_max = np.pi/2 # (radians)
# T = 1000 #trial length (ms)
# num_trials = 100 # number of spike trains to generate

# tuning = r_0 + (r_max-r_0)*np.cos(s-s_max) # tuning curve
# spike_times = np.empty((num_cons, num_trials), dtype=list)


## 2a
bin_width = 20                             # (ms)
s = np.arange(8)*np.pi/4                   # (radians)
num_cons = np.size(s)                      # num_cons = 8 in this case, number of directions
r_0 = 35 # (spikes/s)
r_max = 60 # (spikes/s)
s_max = np.pi/2 # (radians)
T = 1000 #trial length (ms)
num_trials = 100 # number of spike trains to generate

tuning = r_0 + (r_max-r_0)*np.cos(s-s_max) # tuning curve
spike_times = np.empty((num_cons, num_trials), dtype=list)

def findfiringrate(angle: int) -> float:
    return r_0 + (r_max-r_0)*np.cos(angle-s_max) # tuning curve

for con in range(num_cons):
    angle = s[con]
    for rep in range(num_trials):
        firingrate = findfiringrate(angle)
        spike_times[con, rep] = nsp.GeneratePoissonSpikeTrain(T, firingrate)


print(spike_times.shape)

s_labels = ['0', '$\pi$/4', '$\pi$/2', '3$\pi$/4', '$\pi$', '5$\pi$/4', '3$\pi$/2', '7$\pi$/4']
num_plot_rows = 5
num_plot_cols = 3
subplot_indx = [9, 6, 2, 4, 7, 10, 14, 12]
num_rasters_to_plot = 5 # per condition

# Generate and plot homogeneous Poisson process spike trains
plt.figure(figsize=(10,8))
for con in range(num_cons):

    # Plot spike rasters
    plt.subplot(num_plot_rows, num_plot_cols, subplot_indx[con])    
    nsp.PlotSpikeRaster(spike_times[con, 0:num_rasters_to_plot])
    
    plt.title('Spike trains, s= '+s_labels[con]+' radians')
    plt.tight_layout()







# def findfiringrate(angle: int) -> float:
#     return r_0 + (r_max-r_0)*np.cos(angle-s_max) # tuning curve

# for con in range(num_cons):
#     firingrate = findfiringrate(s[con])
#     t = 0
#     tau = 1

#     for rep in range(num_trials):
#         #====================================================#
#         list = []

#         while (t < tau):
#             sample = np.random.exponential(scale=(1.0/firingrate))
#             t += sample
#             #print("sample is", sample)
#             list.append(sample)

#         #====================================================#
#         spike_times[con, rep] = list
#         pass
#         #====================================================#
#         # END YOUR CODE
#         #====================================================#










# t = 0
# tau = 1
# list = []

# while (t < tau):
#     sample = np.random.exponential(scale=0.010)
#     t += sample
#     #print("sample is", sample)
#     list.append(sample)

# #print(list)
# print("list1 size is", len(list))

# t2 = 0
# tau2 = 1
# list2 = []

# while (t2 < tau2):
#     sample = np.random.exponential(scale=0.10)
#     t2 += sample
#     #print("sample is", sample)
#     list2.append(sample)

# #print(list2)
# print("list2 size is", len(list2))



