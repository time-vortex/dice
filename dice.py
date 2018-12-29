#!/usr/bin/env python
"""Statistics for 3d6 vs 4d6 dice."""

import numpy as np
import pylab as plt

def dist_3d6():
    """Probability distribution for 3d6."""

    p = np.zeros(19)
    for m in range(1, 7):
        for n in range(1, 7):
            for q in range(1, 7):
                i = sum([m, n, q])
                p[i] += 1.0

    return p / 216.0

def dist_4d6():
    """Probability distribution for 4d6 drop lowest."""

    p = np.zeros(19)
    for m in range(1, 7):
        for n in range(1, 7):
            for q in range(1, 7):
                for r in range(1, 7):
                    roll = sorted([m, n, q, r])
                    i = sum(roll[1:])
                    p[i] += 1.0

    return p / 1296.0

def mean(p):
    """Mean value."""

    v = 0.0
    for i, pi in enumerate(p):
        v += i*pi

    return v

def plot(p3d6, p4d6):
    """Plot 3d6 vs 4d6 probability distributions."""

    x = np.arange(0, 19)

    plt.bar(x, p3d6, color="b", align="center", alpha=0.2)
    plt.bar(x, p4d6, color="b", align="center", alpha=0.5)
    plt.xticks(x, x)
    plt.xlabel("Ability Score")
    plt.ylabel("Probability")
    plt.xlim([0, 19])
    plt.show()

def std(p):
    """Standard deviation."""

    p0 = mean(p)

    v2 = 0.0
    for i, pi in enumerate(p):
        v2 += pi*(i - p0)**2

    return np.sqrt(v2)

if __name__ == "__main__":
    p3d6 = dist_3d6()
    p4d6 = dist_4d6()

    print("3d6: mean, std = {:5.2f} {:7.4f}".format(mean(p3d6), std(p3d6)))
    print("4d6: mean, std = {:5.2f} {:7.4f}".format(mean(p4d6), std(p4d6)))
    plot(p3d6, p4d6)
