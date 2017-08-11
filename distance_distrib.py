import numpy as np
import matplotlib.pyplot as plt

MAX_ITER = 10000

M = 1
N = 4

V = []

for N in range(1, 6):
    for M in range(1, N):
        print M, N
        D = []

        for i in range(MAX_ITER):
            A = np.random.uniform(size=M)
            B = np.random.uniform(size=N)
            D.append(np.mean([np.min(np.abs(0.5 - B)) for x in A]))

        D = np.array(D)

        weights = np.ones_like(D) / float(len(D))
        # bins = np.linspace(0, 1, 20)

        (values, bins) = np.histogram(D, bins=10, weights=weights)

        #print bins[:-1].shape
        #print values.shape

        plt.plot(bins[:-1], values)

plt.show()

