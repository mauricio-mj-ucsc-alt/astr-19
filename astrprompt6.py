#Create a Jupyter Notebook where, in separate cells, you define functions 
# that return sin(x) and cos(x).  Use Markdown cells to comment your Notebook,
#  and describe what each function does. Create a third Python cell that will 
# tabulate sin(x) and cos(x) using these previously defined functions vs. x,
#  where x is tabulated between 0 and 2 with a thousand entries. Write a fourth
#  Python cell that will use a for loop to print out the first 10 values of x,
#  sin(x), and cos(x) in columns.

import math
import numpy as np

def f_sin(x):
    return math.sin(x)

def f_cos(x):
    return math.cos(x)

x_values = np.linspace(0, 2, 1000)

sin_values = [f_sin(x) for x in x_values]
cos_values = [f_cos(x) for x in x_values]

print(f"{'x':>10} {'sin(x)':>15} {'cos(x)':>15}")
print("-" * 42)

for i in range(10):
    print(f"{x_values[i]:10.5f} {sin_values[i]:15.8f} {cos_values[i]:15.8f}")
