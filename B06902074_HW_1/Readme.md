# Financial Computing 2020 Spring HW1

**b06902074 柯宏穎**

### Introduction

&emsp; To compute the $Modified\ Duration$ and $Convexity$, we can use the following formula to find it.
$$
PV = \sum_{i=1}^n\frac{C_i}{(1+y_i)^i} \\
Modified\ Duration = -\frac{\partial P}{\partial y}\frac{1}{P} = -\sum_{i=1}^n\frac{C_i}{(1+y_i)^{i+1}}(-i) \\
Convexity = \frac{\partial^2P}{\partial y_i^2} = \sum_{i=1}^n\frac{C_i}{(1+y_i)^{i+2}}(-i)(-i-1)
$$


### How to run

&emsp; I use $python3$ to accomplish this assignment.

```powershell
pip3 install -r requirement.txt
python3 hw1.py (then input the spot rate and cash flow respectively)
```

&emsp; Example:

```powershell
python3 hw1.py
0.053, 0.051, 0.049, 0.047, 0.040
3, 2, 3, 2, 103
```

&emsp; Output:

```powershell
Modified Duration: 4.562384213864675
Convexity:         0.2587936757475601
```

