import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import csv
from tkinter import *
from tkinter import messagebox
import helper
import get_c_point
from Extract_data import File_Parser

font_size = 6
matplotlib.rc('font', size=font_size)


# set up the GUI labels
master = Tk()
master.wm_title('ELISA Control Charts')
Label(master, text="Tag for Included (control)").grid(row=0)
Label(master, text="Tag for Excluded (test)").grid(row=1)
Label(master, text="Row data begins").grid(row=2)
Label(master, text="Column (Conc)").grid(row=3)
Label(master, text="Column (OD)").grid(row=4)

# Create the user entries
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)


def graphs():
    global fig1
    # Set up the figures
    fig1 = plt.figure(1)
    ax1 = plt.subplot2grid((6, 6), (0, 0), colspan=4, rowspan=2)
    ax2 = plt.subplot2grid((6, 6), (2, 0), colspan=2)
    ax3 = plt.subplot2grid((6, 6), (2, 2), colspan=2)
    ax4 = plt.subplot2grid((6, 6), (3, 0), colspan=2)
    ax5 = plt.subplot2grid((6, 6), (3, 2), colspan=2)
    ax6 = plt.subplot2grid((6, 6), (4, 0), colspan=2)
    ax7 = plt.subplot2grid((6, 6), (4, 2), colspan=2)
    ax8 = plt.subplot2grid((6, 6), (5, 0), colspan=2)
    ax9 = plt.subplot2grid((6, 6), (5, 2), colspan=2)

    # Convert the userinputs to integers
    userinput1 = e1.get()
    userinput2 = e2.get()
    userinput3 = e3.get()
    userinput3 = int(userinput3)
    userinput4 = e4.get()
    userinput4 = int(userinput4)
    userinput5 = e5.get()
    userinput5 = int(userinput5)

    input_dic = {'user_input1': userinput1, 'user_input2': userinput2,
                 'user_input3': userinput3, 'user_input4': userinput4,
                 'user_input5': userinput5}

    # Initialise lists
    list_of_axes = [ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]
    list_of_conc = []
    list_of_final_points = []
    list_of_final_test_points = []

    # Extract data ending with userinput1
    good_file = File_Parser(input_dic, data='csv', user_input=input_dic['user_input1'])

    ax1.plot(list(map(get_c_point.Point.get_concentration,
                      good_file.get_list_of_points())),
             list(map(get_c_point.Point.get_absorbance,
                      good_file.get_list_of_points())), 'ko', markersize=5)

    # Extract data ending with userinput2 ("Test data")
    if userinput2 is not 'none':
        test_file = File_Parser(input_dic, data='csv', user_input=input_dic['user_input2'])

        ax1.plot(list(map(get_c_point.Point.get_concentration,
                          test_file.get_list_of_points())),
                 list(map(get_c_point.Point.get_absorbance,
                          test_file.get_list_of_points())),
                 'mo', markersize=5)
    else:
        print('no test group')

    # Give a table of each point by concentration
    list_of_points = np.array(np.split(
        np.array(good_file.get_list_of_points()), len(good_file.get_file_names())))
    list_of_test_points = np.array(np.split(
        np.array(test_file.get_list_of_points()), len(test_file.get_file_names())))

    # Format the file names for printing in the terminal
    printable, xmask1, key = helper.print_key(good_file.get_file_names())
    print('Good Key')
    print(key)

    printablee, xmask1e, keye = helper.print_key(test_file.get_file_names())
    print('Test Key')
    print(keye)

    # take the final means, then plot everything
    for counter, value in enumerate(list_of_axes):
        final_point = get_c_point.Final_point(list_of_points[:, counter])
        final_test_point = get_c_point.Final_point(list_of_test_points[:, counter])
        helper.plot_everything(value, final_point.get_sd(),
                               final_point.get_y(),
                               final_point.get_mean(), xmask1)
        list_of_final_points.append(final_point)
        list_of_final_test_points.append(final_test_point)

    if userinput2 is not 'none':
        for counter, ax in enumerate(list_of_axes):
            ax.plot(xmask1e, list_of_final_test_points[counter].get_mean(), 'mo')
            ax.plot(xmask1e, list_of_final_test_points[counter].get_mean(), 'm')
            ax.set_xlabel('%s ug/mL' % good_file.get_list_of_conc()[counter])

    ax1.set_xlabel('Concentration')
    ax1.set_ylabel('OD')
    ax2.set_ylabel('OD')
    ax4.set_ylabel('OD')
    ax6.set_ylabel('OD')
    ax8.set_ylabel('OD')

    # Prints where there is a point outside 2 or 3 SD
    for counter, item in enumerate(list_of_final_points):
        helper.print_outside_sd(printable,
                                list(map(get_c_point.Point.get_mean, list_of_points[:, counter])),
                                item.get_y(),
                                list_of_final_test_points[counter].get_mean(),
                                userinput2,
                                item.get_sd(),
                                good_file.get_list_of_conc()[counter])

    # Figure plotting
    fig1.tight_layout()
    fig1.subplots_adjust(wspace=2.5, hspace=1)
    plt.show()
    fig1.savefig('Control charts.tiff', dpi=600)

    # File saving

    columns = [list_of_conc,
               list(map(get_c_point.Final_point.get_y, list_of_final_points)),
               list(map(get_c_point.Final_point.get_sd, list_of_final_points)),
               list(map(get_c_point.Final_point.get_cv, list_of_final_points))]

    with open('ELISASTATS.csv', 'w',  encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(['Concentration', 'Mean OD', 'SD', 'CV'])
        for row in zip(*columns):
            writer.writerow(row)


def popup():
    messagebox.showinfo(
        "Help",
        "Tag must appear immediately prior to the .csv \n Example: "
        "if the included tag is 'good', and test tag is 'test' \n appropriate file "
        "naming could be Plate1good.csv and Plate1test.csv \n For more help, see user manual")


Button(master, text='Run', command=graphs).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Tags help', command=popup).grid(row=5, column=4, sticky=W, pady=4)

mainloop()
