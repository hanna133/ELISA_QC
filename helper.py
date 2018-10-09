# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:08:38 2018

@author: kercy_000
"""
import numpy as np
from itertools import repeat


def plot_everything(ax, sd, y, mean, xmask):
    ax.plot(xmask, mean, 'ko', markersize=7)
    ax.plot(xmask, mean, 'k')
    ax.axhline(y=y)
    ax.axhline(y=(y + sd * 2), color='g', linewidth=2)
    ax.axhline(y=(y - sd * 2), color='g', linewidth=2)
    ax.axhline(y=(y + sd * 3), color='r', linewidth=2)
    ax.axhline(y=(y - sd * 3), color='r', linewidth=2)


def print_outside_sd(printable, meanind, meantot, meaninde, userinput2, sd, conc):
    """
    To refactor to make it intelligible
    """
    if userinput2 == 'none':
        meanind = meaninde
    if (meanind > meantot+sd*2).any or (meanind < meantot-sd*2).any:
        print("Control set outside 2SD at %s: \n %s" % (round(conc, 3), printable))
    if (meanind > meantot+sd*3).any or (meanind < meantot-sd*3).any():
        print("Control set outside 3SD at %s: \n %s" % (round(conc, 3), printable))


def print_key(file_names):

    file_names = [x for item in file_names for x in repeat(item, 3)]
    return np.array(file_names[0::3])
