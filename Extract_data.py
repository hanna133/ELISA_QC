import glob
import numpy as np
from get_c_point import Point


class File_Parser:
    def __init__(self, input_dic, data=None, user_input=None):
        self.file_names = []
        self.list_of_points = []
        self.list_of_conc = []

        if data == 'csv':
            for files in glob.glob("*%s.csv" % user_input):
                """
                For each file, should collect a list of Points
                """
                self.file_names.append(files)
                array = np.genfromtxt(files, delimiter=';',
                              skip_header=input_dic['user_input3']-1,
                              usecols=(input_dic['user_input4']-1,
                                       input_dic['user_input5']-1))
                list_of_slices = [array[0:3], array[3:6], array[6:9], array[9:12],
                                  array[12:15], array[15:18], array[18:21],
                                  array[21:24]]

                for elements in list_of_slices:
                    point = Point(elements)
                    self.list_of_points.append(point)
                    self.list_of_conc.append(point.get_mean()[0])

        elif data == 'pandas':
            pass
        else:
            print('Unknown data format')

    def get_list_of_points(self): return self.list_of_points

    def get_list_of_conc(self): return self.list_of_conc

    def get_file_names(self): return self.file_names