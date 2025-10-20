#Write a Python program that writes out a table of the function sin(x) vs.
#  x, where x is tabulated between 0 and 2 with a thousand entries. Follow 
# the basic Python program structure, including a main program function.

import math

def main():
    start = 0
    end = 2
    num_points = 1000

    step = (end - start) / (num_points - 1)

    print(f"{'x':>10} {'sin(x)':>15}")
    print("-" * 26)

    for i in range(num_points):
        x = start + i * step
        print(f"{x:10.5f} {math.sin(x):15.8f}")

if __name__ == "__main__":
    main()
