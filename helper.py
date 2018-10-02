# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:08:38 2018

@author: kercy_000
"""
import numpy as np


def plot_everything(ax, sd, y, mean, xmask1):
    ax.plot(xmask1, mean, 'ko', markersize=7)
    ax.plot(xmask1, mean, 'k')
    ax.axhline(y=y)
    ax.axhline(y=(y + sd * 2), color='g', linewidth=2)
    ax.axhline(y=(y - sd * 2), color='g', linewidth=2)
    ax.axhline(y=(y + sd * 3), color='r', linewidth=2)
    ax.axhline(y=(y - sd * 3), color='r', linewidth=2)


def get_final_mean(points):
    """
    Compute stats for each Point object at the same concentration.
    :param points: Must be a list of point object of the same concentration.
    :return: return standard deviation, y, and mean of them.
    """
    y = []
    mean = []
    for items in points:
        y.append(items.get_y())
        mean.append(items.get_mean())
    sd = np.std(y)
    y = np.mean(y)
    return sd, y, mean


def print_outside_sd(printable, meanind, meantot, meaninde, userinput2, sd, conc):
    """
    To refactor
    """
    if userinput2 == 'none':
        meanind = meaninde
    if (meanind > meantot+sd*2).any or (meanind < meantot-sd*2).any:
        print("Control set outside 2SD at %s: \n %s" % (conc, printable))
    if (meanind > meantot+sd*3).any or (meanind < meantot-sd*3).any():
        print("Control set outside 3SD at %s: \n %s" % (conc, printable))



