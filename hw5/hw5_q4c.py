import numpy as np

cov_matrix = np.zeros((4, 4))
cov_matrix[0, :] = 1
cov_matrix[:, 0] = 1
cov_matrix[1, 1:] = 2
cov_matrix[1:, 1] = 2
cov_matrix[2, 2:] = 3
cov_matrix[3, 2] = 3
cov_matrix[3, 3] = 4
print(cov_matrix)

inv_cov_matrix = np.linalg.inv(cov_matrix)
print(inv_cov_matrix)

