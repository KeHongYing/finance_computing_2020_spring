import numpy as np
import sys

def f(x):
	return x ** 2 * s ** 2 / 4

x, y, r, b, m, s, n, X = list(map(float, sys.argv[1: ]))
x, y, r, b, m, s, n, X = int(x), int(y), r / 100, b / 100, m / 100, s / 100, int(n), X / 100

dt = x / n
dx = np.sqrt(dt)
x0 = 2 * np.sqrt(r) / s
gamma = np.sqrt(np.square(b) + 2 * np.square(s))
c1, c2 = (b + gamma) / 2, 2 * (b * m) / np.square(s)

x_tree = np.array([(x0 + (i - 2 * j) * dx) if j < i + 1 else 0 for i in range(n + 1) for j in range(n + 1)]).reshape(n + 1, n + 1)
r_tree = f(x_tree)

r_u, r_d = f(x_tree + dx), f(x_tree - dx)
prob_tree = np.clip((b * (m - r_tree) * dt + r_tree - r_d) / np.where((r_u - r_d) == 0, 1, r_u - r_d), 0, 1)

ss = np.array([y - dt * i for i in range(n + 1)]).reshape(n + 1, 1)
price_tree = np.power(gamma * np.exp(c1 * ss) / (c1 * (np.exp(gamma * ss) - 1) + gamma), c2) * np.exp(-(np.exp(gamma * ss) - 1) / (c1 * (np.exp(gamma * ss) - 1) + gamma) * r_tree[: n + 1, : n + 1])

value_tree = np.zeros((n + 1, n + 1))
value_tree[-1] = np.maximum(X - price_tree[n], 0)

for i in range(n - 1, -1, -1):
	cont = (prob_tree[i, : i + 1] * value_tree[i + 1, : i + 1] + (1 - prob_tree[i, : i + 1]) * value_tree[i + 1, 1: i + 2]) / np.exp(r_tree[i, : i + 1] * dt)
	value_tree[i, : i + 1] = np.maximum(cont, X - price_tree[i, : i + 1])

print('price:', value_tree[0][0] * 100)
