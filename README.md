# Principles of Financial Computing 2020 Spring

## Homework

1. Write a program to calculate the modified duration and convexity of a cash flow. All numbers are period based for simplicity. Inputs: (1) s (spot rates), (2) C (cash flows). Output: (1) modified duration and (2) convexity. For example, assume s = [0.053, 0.051, 0.049, 0.047, 0.040] and C = [3, 2, 3, 2, 103]. Then the modified duration is 4.5624 and convexity is 0.2588. 
2. Write a binomial tree program to calculate the put prices of Bermuda options. For such options, early exercise is allowed only on specific dates. Inputs: S (stock price), X (strike price), r (continuously compounded annual interest rate in percentage), s (annual volatility in percentage), T (time to maturity in days, which of course is also an exercise date), E (set of exercise dates from now), m (number of periods per day for the tree). For example, suppose S = 100, X = 100, r = 3%, s = 30%, T = 60, E = [10, 20, 30, 40, 50, 60], and m = 5, The put price of Bermuda option is about 4.617072772551505. 
3. Write a least-squares Monte Carlo program to price up-and-out American-style Asian puts. Note that the payoff is the same as the Asian put, and the knock-out barrier is triggered by the average price. Output its price, standard error, and delta. Inputs: (1) S (spot price), (2) X (strike price), (3) H (barrier price), (4) T (years), (5) r (risk-free interest rate), (6) s (volatility), (7) n (number of periods), and (8) k (number of simulation paths). Output: put price, its standard error, and its delta. For example, assume S = 100, X = 100, H = 110, T = 1, r = 0.05, s = 0.30, n = 250, and k = 1000000. Then the put price is about 5.4310, the standard error about 0.0085, and the delta about -0.4122.
4. Write a program to price an x-year American-style put option on a zero coupon bond that matures at year y with a par value of 1 dollar. Use binomial trees for the CIR model. Inputs: x (year), y (year), r (%) (initial short rate), b (%), m (%), s (%), number of partitions during the option's life n, and strike price X (% of par). For example, the option price is about 1.01555 (% of par) when x = 1, y = 3, r = 1 (%), b = 30 (%), m = 2 (%), s = 30 (%), n = 150 and X = 95 (%). As another example, the option price is about 4.42332 (% of par) when x = 1, y = 2, r = 5 (%), b = 10 (%), m = 6 (%), s = 30 (%), n = 100 and X = 95 (%).

## Note
There are something wrong on HW2, the answer is not exactly correct.