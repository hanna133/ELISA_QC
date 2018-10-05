import numpy as np


class Point:
    """
    Each point is associated to a concentration,
    coordinates (x, y), and mean.
    """
    def __init__(self, data):
        self._concentration = data[:, 0][np.logical_not(np.isnan(data[:, 0]))]
        data[np.where(np.isnan(data))] = np.take(self._concentration,
                                                 np.where(np.isnan(data))[1])
        self._mean = np.mean(data, axis=0)
        self._x = data[:, 0]
        self._y = data[:, 1]

    def get_x(self): return self._x

    def get_y(self): return self._y

    def get_mean(self): return self._mean

    def get_concentration(self): return self._concentration


class Final_point():
    """
    Point that combine all points for a given concentration
    """
    def __init__(self, data):
        y = []
        self._mean = []
        for item in data:
            y.append(item.get_y())
            self._mean.append(item.get_mean()[1])
        self._sd = np.std(y)
        self._y = np.mean(y)
        self._cv = round(self._sd/self._y*100, 3)

    def get_y(self): return self._y

    def get_mean(self): return self._mean

    def get_sd(self): return self._sd

    def get_cv(self): return self._cv

