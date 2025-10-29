# Create a Jupyter notebook, import matplotlib. Use numpy to pull 1000 random numbers 
# distributed uniformly between [0,1]. Histogram the random numbers into 100 bins, and
#  plot the histogram. Label your axes and save the figure as a PDF.
import numpy as np
import matplotlib.pyplot as plt

data = np.random.uniform(0, 1, 1000)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=100, color='skyblue', edgecolor='black')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Uniformly Distributed Random Numbers")

plt.savefig("uniform_histogram.pdf")
plt.show()
