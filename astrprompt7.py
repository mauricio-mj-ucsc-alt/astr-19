#Create a Jupyter notebook, import matplotlib. Write cells that create 
# an array x ranging from [0,1] in 100 steps and that defines a function 
# that returns exp(x).  In a new cell use the function to set y=exp(x), 
# and then plot x vs. y. Label the x-axis as “Time [milliseconds]” and the
#  y-axis as “Awesomeness”. Save the figure as a PDF.  
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

def my_exp(x):
    return np.exp(x)

y = my_exp(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label='exp(x)', color='blue')
plt.xlabel("Time [milliseconds]")
plt.ylabel("Awesomeness")
plt.title("Exponential Growth of Awesomeness")
plt.legend()
plt.savefig("exp_plot.pdf")
plt.show()

