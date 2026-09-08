import numpy as np
import matplotlib.pyplot as plt

constant = np.array([0.0623,
0.834,
0.949,
0.784,
1.05,
1.06,
1.12,
1.29,
1.17,
1.13,
1.54,
1.49,
1.56,
0.95,
1.46,
1.61,
1.56,
1.18,
1.91,
1.53
])

mass2 = np.array([105,
105.5,
106,
106.5,
107,
107.5,
108,
108.5,
109,
109.5,
110,
110.5,
111,
111.5,
112,
112.5,
113,
113.5,
114,
114.5,
])

mass1 = np.array([105,
104.5,
104,
103.5,
103,
102.5,
102,
101.5,
101,
100.5,
100,
99.5,
99,
98.5,
98,
97.5,
97,
96.5,
96,
95.5,
])
y = mass2 - mass1
x = np.array([float(f"{v:.3g}") for v in constant])
slope = np.sum(x * y) / np.sum(x * x)
x_fit = np.linspace(0, max(x) * 1.1, 100)
y_fit = slope * x_fit
print(f"Slope = {slope:.3g}")
print(f"Equation: y = {slope:.3g}x")
plt.scatter(x, y, label="Experimental Data")
plt.plot(x_fit, y_fit, label=f"Proportional Fit: y = {slope:.3g}x")

plt.xlabel("Constant Acc")
plt.ylabel("Mass 2 − Mass 1")
plt.title("Mass Difference vs Constant Acc")

plt.grid()
plt.legend()
plt.show()
