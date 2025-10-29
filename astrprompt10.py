#Create a Jupyter notebook, import matplotlib. On the numpy website, read about the 
# random number distributions available for pulling random variates.  Select your 
# favorite distribution (other than uniform) and pull 1000 random numbers from that
#  distribution. Histogram the random numbers into 100 bins, and plot the histogram.
#  Label your axes and save the figure as a PDF.
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=100, color='lightgreen', edgecolor='black')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normally Distributed Random Numbers")

plt.savefig("normal_histogram.pdf")
plt.show()

