import numpy as np

input_data = np.load("dims.npy")
print(input_data.shape)
data = input_data.reshape(1, -1)
print(data.shape)
print(data.dtype)
np.savetxt(".txt/dims.txt", data, delimiter=',')

