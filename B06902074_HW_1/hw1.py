import numpy as np

def Duration(s, C, P, n):
	return -np.sum([C[i] * -(i + 1) * (1 + s[i]) ** (-i - 2) for i in range(n)]) / P

def Convexity(s, C, P, n):
	return np.sum([C[i] * -(i + 1) * (-i - 2) * (1 + s[i]) ** (-i - 3) for i in range(n)]) / P / 100

s, C = np.array(list(map(float, input("Spot rate:\n").split(",")))), np.array(list(map(float, input("Cash flow:\n").split(","))))
year = s.shape[0]
P = np.sum([C[i] / (1 + s[i]) ** (i + 1) for i in range(year)])

print(f"Modified Duration: {Duration(s, C, P, year)}\nConvexity:         {Convexity(s, C, P, year)}")
