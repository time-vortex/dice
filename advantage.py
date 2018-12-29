#!/usr/bin/env python
"""Ability check advantage statistics."""

import numpy as np
import pylab as plt

def dist():
    """Calculate advantage/disadvantage probability distributions."""

    pa = np.zeros(20)
    pd = np.zeros(20)
    for k in range(20):
        for i in range(20):
            for j in range(20):
                if max(i, j) >= k:
                    pa[k] += 1.0
                if min(i, j) >= k:
                    pd[k] += 1.0

    return pa / 400.0, pd / 400.0

def plot(pa, pd, p20):
    """Plot statistics."""

    x = np.arange(1, 21)

    plt.plot(x, pa, "o:", alpha=0.8, color="g")
    plt.plot(x, pd, "o:", alpha=0.8, color="r")
    plt.plot(x, p20, "o:", alpha=0.8, color="b")
    plt.axis([0, 21, 0.0, 1.05])
    plt.xticks(x, x)
    plt.xlabel("Difficulty Class (DC)")
    plt.ylabel("Probability of Success")
    plt.text(13.5, 0.65, "Advantage", color="g")
    plt.text(4.2, 0.4, "Disadvantage", color="r")
    plt.text(10.3, 0.55, "Normal", color="b", rotation=-39)
    plt.show()

if __name__ == "__main__":
    pa, pd = dist()

    p20 = [] # normal d20 probability distribution
    for i in range(20):
        p20.append((20 - i) / 20.0)

    for i, pi in enumerate(pa):
        bonus = round(20*(pi - p20[i]))
        print("{:2d} | {:5.1f} | {}".format(i+1, 100*pi, bonus))

    plot(pa, pd, p20)
