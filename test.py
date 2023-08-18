import numpy as np

npzfile = np.load("test.h5", allow_pickle=True)
print(npzfile['keypoints'])