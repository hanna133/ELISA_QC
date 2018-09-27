# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:08:38 2018

@author: kercy_000
"""
import numpy as np


def get_means(data):
    temp_list = data
    #Take out concentration values
    concentrations = temp_list[:,0]
    #Remove the blanks
    concentrations = concentrations[np.logical_not(np.isnan(concentrations))]
    nan_list=np.where(np.isnan(temp_list))
    temp_list[nan_list]=np.take(concentrations, nan_list[1])
    
    mean_value = np.mean(temp_list, axis=0)
    x_value = temp_list[:,0]
    y_value = temp_list[:,1]
    
    return x_value, y_value, mean_value, concentrations

def plot_everything(ax, y, xmask1, meanind):
    mean1tot = np.mean(y)
    SD = np.std(y)
    meanind = np.array(meanind)
    meanind = meanind[:, 1]
    ax.plot(xmask1, meanind, 'ko', markersize=7)
    ax.plot(xmask1, meanind, 'k')
    ax.axhline(y=mean1tot)
    ax.axhline(y=(mean1tot + SD * 2), color='g', linewidth=2)
    ax.axhline(y=(mean1tot - SD * 2), color='g', linewidth=2)
    ax.axhline(y=(mean1tot + SD * 3), color='r', linewidth=2)
    ax.axhline(y=(mean1tot - SD * 3), color='r', linewidth=2)

    return SD, mean1tot, meanind
