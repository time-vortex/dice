#!/usr/bin/env python
"""Ability score statistics."""

import numpy as np
import pylab as plt
import random
import dice

_MOD = [0, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4]
_I = range(-24, 25)

def d6():
    """Roll a 6-sided die."""

    return random.randint(1, 6)

def dist():
    """Brute force probability distribution for ability score modifiers."""

    P3d6 = dice.dist_3d6()
    P4d6 = dice.dist_4d6()

    p3d6 = np.zeros(49)  # 49 values from [-24, 24]
    p4d6 = np.zeros(49)

    for STR in range(3, 19):
        for DEX in range(3, 19):
            for CON in range(3, 19):
                for INT in range(3, 19):
                    for WIS in range(3, 19):
                        for CHA in range(3, 19):
                            mod = _MOD[STR] + _MOD[DEX] + _MOD[CON] + \
                                  _MOD[INT] + _MOD[WIS] + _MOD[CHA]
                            i = _I.index(mod)
                            p3d6[i] += P3d6[STR]*P3d6[DEX]*P3d6[CON]* \
                                       P3d6[INT]*P3d6[WIS]*P3d6[CHA]
                            p4d6[i] += P4d6[STR]*P4d6[DEX]*P4d6[CON]* \
                                       P4d6[INT]*P4d6[WIS]*P4d6[CHA]

    return p3d6, p4d6

def mean(p):
    """Mean value of ability score modifier."""

    v = 0.0
    for i, pi in zip(_I, p):
        v += i*pi

    return v

def plot(p3d6, p4d6):
    """Plot ability score modifier probability distribution."""

    plt.bar(_I, p3d6, color="b", align="center", alpha=0.2)
    plt.bar(_I, p4d6, color="b", align="center", alpha=0.6)
    plt.xticks(_I[::4], _I[::4])
    plt.xlabel("Sum of Ability Score Modifiers")
    plt.ylabel("Probability")
    plt.xlim([-25, 25])
    plt.show()

def std(p):
    """Standard deviation of ability score modifier."""

    p0 = mean(p)

    v2 = 0.0
    for i, pi in zip(_I, p):
        v2 += pi*(i - p0)**2

    return np.sqrt(v2)

if __name__ == "__main__":
    p3d6, p4d6 = dist()

    n = 0
    for i, pi in zip(_I, p4d6):
        print("{:3d} {:14.6f} {:14.6f}".format(i, pi, np.sum(p4d6[:n])))
        n += 1

    print("3d6: mean, std = {:5.2f} {:7.4f}".format(mean(p3d6), std(p3d6)))
    print("4d6: mean, std = {:5.2f} {:7.4f}".format(mean(p4d6), std(p4d6)))
    plot(p3d6, p4d6)
