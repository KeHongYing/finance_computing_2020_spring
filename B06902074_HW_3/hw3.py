import numpy as np
import sys
from tqdm import tqdm

def backward(S, X, H, T, r, s, n, k, seed = None):
	np.random.seed(seed)
	
	period_time = T / n
	R = np.exp(period_time * r)
	
	path = np.zeros((k, n + 1))
	path[:, 0] = S

	for i in tqdm(range(1, n + 1)):
		path[:, i] = np.exp((r - np.square(s) / 2) * period_time + np.random.standard_normal(k) * np.sqrt(period_time) * s) * path[:, i - 1]
	
	path = np.add.accumulate(path, axis = 1) / (np.arange(n + 1) + 1)

	option = np.maximum(X - path, 0)
	valid = path < H
	C = np.where(valid.all(axis = 1), option[:, n], 0)
	for i in tqdm(range(n - 1, -1, -1)):
		C /= R

		positive = valid[:, : i + 1].all(axis = 1) & (option[:, i] > 0)
		if not path[positive, i].any():
			continue
	  
		C[positive] = np.where(option[positive, i] > np.polyval(np.polyfit(path[positive, i], C[positive], 2), path[positive, i]), option[positive, i], C[positive])
	
	return C
		
S, X, H, T, r, s, n, k = [int(i) if i == int(i) else i for i in list(map(float, sys.argv[1: ]))]
delta = 1

seed = np.random.randint(1000000000 + 7)
C = backward(S, X, H, T, r, s, n, k, seed = seed)
C_delta = backward(S + delta, X, H, T, r, s, n, k, seed = seed)

put, put_delta = np.mean(C), np.mean(C_delta)
std_err = np.std(C) / np.sqrt(k)

print(f"put price: {put}")
print(f"stderr   : {std_err}")
print(f"delta    : {(put_delta - put) / delta}")
