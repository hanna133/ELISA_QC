import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import csv
from tkinter import *
from tkinter import messagebox
from itertools import repeat
import helper, get_c_point

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
    # set up the figures
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

    # create empty lists to be filled in the loops
    fnames = []
    fnamese = []

    # convert the userinputs to integers

    userinput1 = e1.get()
    userinput2 = e2.get()
    userinput3 = e3.get()
    userinput3 = int(userinput3)
    userinput4 = e4.get()
    userinput4 = int(userinput4)
    userinput5 = e5.get()
    userinput5 = int(userinput5)

    # Initialise lists
    list_of_points = []
    list_of_test_points = []
    list_of_axes = [ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]
    list_of_final_means = []
    list_of_sd = []
    list_of_cv = []
    list_of_means = []
    list_of_conc = []
    list_of_mean_test = []

    # Extract data of good files
    for files in glob.glob("*%s.csv" % userinput1):
        fnames.append(files)
        array = np.genfromtxt(files, delimiter=';',
                              skip_header=userinput3-1,
                              usecols=(userinput4-1, userinput5-1))

        list_of_slices = [array[0:3], array[3:6], array[6:9], array[9:12],
                          array[12:15], array[15:18], array[18:21],
                          array[21:24]]
        for elements in list_of_slices:
            point = get_c_point.Point(elements)
            list_of_points.append(point)
            list_of_conc.append(np.mean(point.get_concentration()))

        ax1.plot(list(map(get_c_point.Point.get_x, list_of_points)),
                 list(map(get_c_point.Point.get_y, list_of_points)),
                 'ko', markersize=5)

    # Extract data on the files you want to test
    if userinput2 is not 'none':
        for files in glob.glob("*%s.csv" % userinput2):
            fnamese.append(files)
            array = np.genfromtxt(files, delimiter=';',
                                  skip_header=userinput3-1,
                                  usecols=(userinput4-1, userinput5-1))

            list_of_slices = [array[0:3], array[3:6], array[6:9], array[9:12],
                              array[12:15], array[15:18], array[18:21],
                              array[21:24]]
            for elements in list_of_slices:
                point = get_c_point.Point(elements)
                list_of_test_points.append(point)
            ax1.plot(list(map(get_c_point.Point.get_x, list_of_test_points)),
                     list(map(get_c_point.Point.get_y, list_of_test_points)),
                     'mo', markersize=5)
    else:
        print('no test group')

    # Give a table of each point by concentration
    list_of_points = np.array(np.split(
        np.array(list_of_points), len(fnames)))
    list_of_test_points = np.array(np.split(
        np.array(list_of_test_points), len(fnamese)))

    # format the file names for printing in the terminal,
    # and create a count for the x axis of the control charts
    # TO REFACTOR
    fnames = [x for item in fnames for x in repeat(item, 3)]
    length = len(fnames)
    xmask1 = list(range(length//3))
    printable = np.array(fnames[0::3])
    printcount = np.array(list(range(len(printable))))
    key = np.column_stack((printcount, printable))
    print('Standards Key')
    print(key)

    fnamese = [x for item in fnamese for x in repeat(item, 3)]
    lengthe = len(fnamese)
    xmask1e = list(range(lengthe//3))
    printablee = np.array(fnamese[0::3])
    printcounte = np.array(list(range(len(printablee))))
    keye = np.column_stack((printcounte, printablee))
    print('Test Key')
    print(keye)

    # take the final means, then plot everything
    for counter, value in enumerate(list_of_axes):
        sd, final_mean, mean = helper.get_final_mean(list_of_points[:, counter])
        helper.plot_everything(value, sd, final_mean, mean, xmask1)
        list_of_final_means.append(final_mean)
        list_of_sd.append(sd)
        list_of_means.append(mean)
        _, _, test_mean = helper.get_final_mean(list_of_test_points[:, counter])
        list_of_mean_test.append(test_mean)

    if userinput2 is not 'none':
        for counter, ax in enumerate(list_of_axes):
            ax.plot(xmask1e, list_of_mean_test[counter][1], 'mo')
            ax.plot(xmask1e, list_of_mean_test[counter][1], 'm')

    ax1.set_xlabel('Concentration')
    ax1.set_ylabel('OD')
    ax2.set_ylabel('OD')
    ax4.set_ylabel('OD')
    ax6.set_ylabel('OD')
    ax8.set_ylabel('OD')

    for counter, value in enumerate(list_of_axes):
        value.set_xlabel('%s ug/mL' % list_of_conc[counter])

    # Coeffs of variance
    for counter, value in enumerate(list_of_final_means):
        list_of_cv.append((list_of_sd[counter] /
                           value) * 100)

    # Prints where there is a point outside 2 or 3 SD
    for counter, item in enumerate(list_of_means):
        helper.print_outside_sd(printable, item, list_of_final_means[counter],
                                list_of_mean_test[counter], userinput2,
                                list_of_sd[counter], list_of_conc[counter])

    # Figure plotting
    fig1.tight_layout()
    fig1.subplots_adjust(wspace=2.5, hspace=1)
    plt.show()
    fig1.savefig('Control charts.tiff', dpi=600)

    # File saving
    filename = 'ELISASTATS.csv'
    header = ['Concentration', 'Mean OD', 'SD', 'CV']
    rows = map( None, list_of_conc, list_of_final_means, list_of_sd, list_of_cv)
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def popup():
    messagebox.showinfo(
        "Help",
        "Tag must appear immediately prior to the .csv \n Example: if the included tag is 'good', and test tag is 'test' \n appropriate file naming could be Plate1good.csv and Plate1test.csv \n For more help, see user manual")


Button(master, text='Run', command=graphs).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Tags help', command=popup).grid(row=5, column=4, sticky=W, pady=4)

mainloop()
