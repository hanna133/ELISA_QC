import glob
import numpy as np
from get_c_point import Point

class Good_file:
    def __init__(self, input_dic, data=None):
        self.file_names = []
        self.list_of_points = []
        self.list_of_conc = []

        if data == 'csv':
            for files in glob.glob("*%s.csv" % input_dic['user_input1']):
                self.file_names.append(files)
                array = np.genfromtxt(files, delimiter=';',
                              skip_header=input_dic['user_input3']-1,
                              usecols=(input_dic['user_input4'],
                                       input_dic['user_input5']-1))
                list_of_slices = [array[0:3], array[3:6], array[6:9], array[9:12],
                                  array[12:15], array[15:18], array[18:21],
                                  array[21:24]]

                for elements in list_of_slices:
                    point = Point(elements)
                    self.list_of_points.append(point)
                    self.list_of_conc.append(np.mean(point.get_concentration()))