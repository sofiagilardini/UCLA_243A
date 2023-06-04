import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import scipy.io as sio

plt.rcParams["figure.dpi"] = 150

data = sio.loadmat("ps4_realdata.mat")  # load the .mat file.
num_traindata = data["train_trial"].shape[0]
num_class = data["train_trial"].shape[1]
num_testdata = data["test_trial"].shape[0]
num_neurons = 97

# contains the firing rates for all neurons on all 8 x 91 trials in the training set
traindata_arr = np.zeros((num_class, num_traindata, num_neurons))
# for the testing set
testdata_arr = np.zeros((num_class, num_testdata, num_neurons))

for class_idx in range(num_class):
    for traindata_idx in range(num_traindata):
        traindata_arr[class_idx, traindata_idx, :] = np.sum(
            data["train_trial"][traindata_idx, class_idx][1][:, 350:550], axis=1
        )
    for testdata_idx in range(num_testdata):
        testdata_arr[class_idx, testdata_idx, :] = np.sum(
            data["test_trial"][testdata_idx, class_idx][1][:, 350:550], axis=1
        )
