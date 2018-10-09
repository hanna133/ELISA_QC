import numpy as np


class Point:
    """Create a point object from datas in the File_Parser class.

    Attributes:
        concentration (numpy array): Array containing concentration of a point.
        (the x)
        absorbance (numpy array): Array containing all the absorbance
        for a given point (the y)
        mean (numpy array): Array containing mean of concentration and
        mean of absorbance. Should be of the form [concentration, absorbance]

    """
    def __init__(self, data):
        """
        Initialise Point object from datas from the File_Parser class.

        Args:
            data (numpy array): For now a numpy array from the csv parsing.
        """
        self.concentration = data[:, 0][np.logical_not(np.isnan(data[:, 0]))]
        data[np.where(np.isnan(data))] = np.take(self.concentration,
                                                 np.where(np.isnan(data))[1])
        self.mean = np.mean(data, axis=0)
        self.absorbance = data[:, 1]

    def get_absorbance(self): return self.absorbance

    def get_mean(self): return self.mean

    def get_concentration(self): return self.concentration


class Final_point():
    """Point that combine all Point objects of the same concentration
    from different files

    Attributes:
        mean (list): List that contains the means of absorbance of all Point
        object in data.
        sd (float): Standard deviation of all absorbances of all points.
        y (float): Mean of all absorbances of all points.
        cv (float): Coefficient of variation of sd and y.
    """
    def __init__(self, data):
        """Initialise the Final Point class.
        Args:
             data (list): List of points of the same concentration.
        """
        y = []
        self.mean = []
        for item in data:
            y.append(item.get_absorbance())
            self.mean.append(item.get_mean()[1])
        self.sd = np.std(y)
        self.y = np.mean(y)
        self.cv = round(self.sd/self.y*100, 3)

    def get_y(self): return self.y

    def get_mean(self): return self.mean

    def get_sd(self): return self.sd

    def get_cv(self): return self.cv
