import numpy as np 

a = np.array(np.arange(4, dtype=float))
b = np.array(np.arange(4,8, dtype=float))
c = np.stack((a, b)).T
c = c.reshape((2, 4))


a = np.zeros((4, 3))
for i in range(1, len(a)):    
    a[i] = np.ones(3)*(10 * i)


X = np.random.rand(4, 2)
min_val = np.min(X, axis=0)

print(X, "\n")

def standardize(X):

    col_mean = np.mean(X, axis=0)
    col_std = np.std(X, axis=0)
    return (X - col_mean)/col_std

print(standardize(X))