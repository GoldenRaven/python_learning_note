import numpy as np
m = []
for i in range(3):
    m.append(list(np.random.rand(4)))
    print(' '.join(map(str, m[i])))
