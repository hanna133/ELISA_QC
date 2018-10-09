import glob
import numpy as np
from get_c_point import Point, Final_point


class File_Parser:
    """Create an object from datas that is a list of Points objects from the
    different files fed to it.

    Attributes:
        file_names (list): List of the files used to generate datas.

        list_of_points (list): List of the different points across a file.
        For more info, see the Point class.

        list_of_final_point (list): List of "final points", for all the files in
        file_names aggregate all the points corresponding to one given
        concentration.

        list_of_conc (list): List of each concentration used. For now, it wont
        work if the files used to create data have different concentrations
        across them.

    """
    def __init__(self, input_dic, data=None, user_input=None):
        """Initialise a File_Parser object from a list of files
        Args:
            input_dic (dict): Dictionary of user inputs(given by GUI)

            data (str): A string with the type of data. For now, only 'csv' is
            supported. Pandas compatible file will be explored later.

            user_input (str): A string for input_dict. Original plan was to
            take all file in the same folder that finish with the same text. For
            example 'Plate1good' and 'Plate2good" will be parsed together in a
            File_Parser object and 'good' should be user_input.
            As the program (for now) is built, we expect userinput1 or
            userinput2.

        """
        # Init lists
        self.file_names = []
        self.list_of_points = []
        self.list_of_final_point = []
        self.list_of_conc = []
        if data == 'csv':
            for files in glob.glob("*%s.csv" % user_input):
                self.file_names.append(files)
                # This is the delimitation used in the original repository and
                # the files i'm using to test the program. We could extend the
                # program to let user choose the data input (here it's array)
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
                    if point.mean[0] not in self.list_of_conc:
                        self.list_of_conc.append(point.mean[0])

        elif data == 'pandas':
            # Pandas handling is planned. Pandas is much more easier to use
            # than random arrays and would require an formated input with clear
            # labels on values.
            pass
        else:
            print('Unknown data format')

        self.mask = list(range(len(self.file_names)))
        # Take all points of a same concentration and average them into the
        # Final_point class
        for concentration in self.list_of_conc:
            dummy_list = []
            for point in self.list_of_points:
                if point.mean[0] == concentration:
                    dummy_list.append(point)
            self.list_of_final_point.append(Final_point(dummy_list))
