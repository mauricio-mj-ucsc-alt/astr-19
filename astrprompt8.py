#Create a Jupyter notebook, import matplotlib. Write cells that 
# create an array x ranging from [0,1] in 100 steps and that defines 
# functions that return sin(x) and cos(x).  In a new cell use to create
#  a multipanel plot (1 row, 2 columns), plotting sin(x) vs. x in the left 
# panel and cos(x) vs. x in the right panel. Label the panels with sin(x) and 
# cos(x), and save the figure as a PDF.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

def my_sin(x):
    return np.sin(x)

def my_cos(x):
    return np.cos(x)

y_sin = my_sin(x)
y_cos = my_cos(x)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, y_sin, color='blue')
axes[0].set_title("sin(x)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("sin(x)")

axes[1].plot(x, y_cos, color='red')
axes[1].set_title("cos(x)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("cos(x)")

plt.tight_layout()
plt.savefig("sine_cosine_plots.pdf")
plt.show()

