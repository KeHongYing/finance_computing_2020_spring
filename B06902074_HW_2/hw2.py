import numpy as np

def floor_max(n):
	return int((2 + n) * (n - 1) / 2)

def find_floor(x):
	return int(np.ceil((-1 + np.sqrt(9 + 8 * x)) / 2))

data = list(map(float, input("Suppose S = 100, X = 110, r = 3%, s = 30%, T = 60, E = [10, 20, 30, 40, 50], and m = 5\ninput format is 100 110 3 30 60 10 20 30 40 50 5:\n").split()))

S = data[0]
X = data[1]
r = data[2] * 0.01
s = data[3] * 0.01
T = data[4]
E = data[5: -1]
m = data[-1]

period_time = 1 / (365 * m)
u = np.exp(s * np.sqrt(period_time))
d = np.exp(-s * np.sqrt(period_time))
r_hat = r * period_time
R = np.exp(r_hat)
p = (R - d) / (u - d)

assert s * np.sqrt(period_time) > r_hat

num = int((T * m + 1) * (T * m + 2) / 2)
stock_price, put_price = np.zeros(num), np.zeros(num)

stock_price[0] = S

#for i in range(1, num):
#	my_floor = find_floor(i)
#	last_floor_max = floor_max(my_floor - 1)
#	my_index = i - last_floor_max
#
#	if my_index == 1:
#		stock_price[i] = stock_price[last_floor_max - (my_floor - 2)] * d
#	else:
#		stock_price[i] = stock_price[floor_max(my_floor - 2) + my_index - 1] * u


for i in range(2, int(T * m + 2)):
	last_floor_max = floor_max(i - 1)
	stock_price[last_floor_max + 1: last_floor_max + i + 1] = np.hstack((stock_price[last_floor_max - i + 2] * d, stock_price[last_floor_max - i + 2: last_floor_max + 1] * u))

#for i in range(floor_max(T * m) + 1, floor_max(T * m + 1) + 1):
#	put_price[i] = max(0, X - stock_price[i])

put_price[floor_max(T * m) + 1:] = np.maximum(X - stock_price[floor_max(T * m) + 1:], 0)

for i in range(int(T * m), 0, -1):
	last_floor_max = floor_max(i - 1)
	price1 = (X - stock_price[last_floor_max + 1: last_floor_max + i + 1]) * (np.ceil((i - 1) / m) in E)
	price2 = (put_price[last_floor_max + i + 1: last_floor_max + 2 * i + 1] * (1 - p) + put_price[last_floor_max + 2 + i: last_floor_max + 2 * i + 2] * p) / R
	put_price[last_floor_max + 1: last_floor_max + i + 1] = np.maximum(price1, price2)

#for i in range(floor_max(T * m), -1, -1):
#	my_floor = find_floor(i)
#	if np.ceil((my_floor - 1) / m) in E:
#		put_price[i] = max(X - stock_price[i], (put_price[i + my_floor] * (1 - p) + put_price[i + my_floor + 1] * p) / R)
#	else:
#		put_price[i] = (put_price[i + my_floor] * (1 - p) + put_price[i + my_floor + 1] * p) / R
	
print(put_price[0])
