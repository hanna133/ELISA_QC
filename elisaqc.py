import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import csv
from tkinter import *
from tkinter import messagebox
from itertools import repeat
import helper

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
    count, counte = 0, 0
    fnames = []
    fnamese = []
    
    y11 = []
    y22 = []
    y33 = []
    y44 = []
    y55 = []
    y66 = []
    y77 = []
    y88 = []

    list_of_superior_y = [y11, y22, y33, y44, y55, y66, y77, y88]
    
    meanind1 = []
    meanind2 = []
    meanind3 = []
    meanind4 = []
    meanind5 = []
    meanind6 = []
    meanind7 = []
    meanind8 = []
    
    list_of_meanind = [meanind1, meanind2, meanind3, meanind4,
                       meanind5, meanind6, meanind7, meanind8]
    
    meanind1e = []
    meanind2e = []
    meanind3e = []
    meanind4e = []
    meanind5e = []
    meanind6e = []
    meanind7e = []
    meanind8e = []

    list_of_meaninde = [meanind1e, meanind2e, meanind3e, meanind4e,
                        meanind5e, meanind6e, meanind7e, meanind8e]
    conc1, conc2, conc3, conc4, conc5, conc6, conc7, conc8 = 0, 0, 0, 0, 0, 0, 0, 0
    list_of_conc = [conc1, conc2, conc3, conc4, conc5, conc6, conc7, conc8]

    print(type(list_of_conc))

    # convert the userinputs to integers

    userinput1 = e1.get()
    userinput2 = e2.get()
    userinput3 = e3.get()
    userinput3 = int(userinput3)
    userinput4 = e4.get()
    userinput4 = int(userinput4)
    userinput5 = e5.get()
    userinput5 = int(userinput5)
    
    # standards loop
    for files in glob.glob("*%s.csv" % userinput1):
        count = count+1
        fnames.append(files)
        array = np.genfromtxt(files, delimiter=';', skip_header=userinput3-1,
                              usecols=(userinput4-1, userinput5-1))
        list_of_slices = [array[0:3], array[3:6], array[6:9], array[9:12],
                          array[12:15], array[15:18], array[18:21], array[21:24]]
        list_of_x = []
        list_of_y = []
        index = 0
        print(type(list_of_conc))
        for elements in list_of_slices:            
            x, y, mean, concentrations = helper.get_means(elements)
            list_of_x.append(x)
            list_of_y.append(y)
            list_of_superior_y[index].append(y)
            list_of_meanind[index].append(mean)
            list_of_conc[index] = np.mean(concentrations)
            index += 1
        ax1.plot(list_of_x, list_of_y, 'ko', markersize=5)

    # test loop
    if userinput2 is'none':
        print('no test group')
    else:
        for files in glob.glob("*%s.csv" % userinput2):
            counte = counte+1
            fnamese.append(files)
            array = np.genfromtxt(files, delimiter=';', skip_header=userinput3-1,
                                  usecols=(userinput4-1, userinput5-1))

            list_of_slices = [array[0:3], array[3:6], array[6:9], array[9:12],
                              array[12:15], array[15:18], array[18:21], array[21:24]]
            list_of_x = []
            list_of_y = []
            index = 0

            for elements in list_of_slices:
                x, y, mean, concentrations = helper.get_means(elements)
                list_of_x.append(x)
                list_of_y.append(y)
                list_of_meaninde[index].append(mean)
                index += 1

            ax1.plot(list_of_x, list_of_y, 'mo', markersize=5)

    # format the file names for printing in the terminal,
    # and create a count for the x axis of the control charts
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
    SD1, mean1tot, meanind1 = helper.plot_everything(ax2, y11, xmask1, meanind1)
    SD2, mean2tot, meanind2 = helper.plot_everything(ax3, y22, xmask1, meanind2)
    SD3, mean3tot, meanind3 = helper.plot_everything(ax4, y33, xmask1, meanind3)
    SD4, mean4tot, meanind4 = helper.plot_everything(ax5, y44, xmask1, meanind4)
    SD5, mean5tot, meanind5 = helper.plot_everything(ax6, y55, xmask1, meanind5)
    SD6, mean6tot, meanind6 = helper.plot_everything(ax7, y66, xmask1, meanind6)
    SD7, mean7tot, meanind7 = helper.plot_everything(ax8, y77, xmask1, meanind7)
    SD8, mean8tot, meanind8 = helper.plot_everything(ax9, y88, xmask1, meanind8)

    list_of_meantot = [mean1tot, mean2tot, mean3tot, mean4tot, mean5tot,
                       mean6tot, mean7tot, mean8tot]

    meanind1e = np.array(meanind1e)
    meanind2e = np.array(meanind2e)
    meanind3e = np.array(meanind3e)
    meanind4e = np.array(meanind4e)
    meanind5e = np.array(meanind5e)
    meanind6e = np.array(meanind6e)
    meanind7e = np.array(meanind7e)
    meanind8e = np.array(meanind8e)

    list_of_axes = [ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]
    if userinput2 == 'none':
        pass
    else:
        for ax in list_of_axes:
            ax.plot(xmask1e, meanind1e[:, 1], 'mo')
            ax.plot(xmask1e, meanind1e[:, 1], 'm')

    ax1.set_xlabel('Concentration')
    ax1.set_ylabel('OD')
    ax2.set_ylabel('OD')
    ax4.set_ylabel('OD')
    ax6.set_ylabel('OD')
    ax8.set_ylabel('OD')

    # coeffeints of variance
    cv1 = (SD1 / mean1tot) * 100
    cv2 = (SD2 / mean2tot) * 100
    cv3 = (SD3 / mean3tot) * 100
    cv4 = (SD4 / mean4tot) * 100
    cv5 = (SD5 / mean5tot) * 100
    cv6 = (SD6 / mean6tot) * 100
    cv7 = (SD7 / mean7tot) * 100
    cv8 = (SD8 / mean8tot) * 100

    meanlist = [mean1tot, mean2tot, mean3tot, mean4tot,
                mean5tot, mean6tot, mean7tot, mean8tot]
    sdlist = [SD1, SD2, SD3, SD4, SD5, SD6, SD7, SD8]
    cvlist = [cv1, cv2, cv3, cv4, cv5, cv6, cv7, cv8]

    for counter, value in enumerate(list_of_axes):
        value.set_xlabel('%s ug/mL' % list_of_conc[counter])

    for counter, item in enumerate(list_of_meanind):
        helper.print_outside_SD(printable, item, list_of_meantot[counter],
                                list_of_meaninde[counter], userinput2,
                                sdlist[counter], list_of_conc[counter])

    # Figure plotting
    fig1.tight_layout()
    fig1.subplots_adjust(wspace=2.5, hspace=1)
    plt.show()
    fig1.savefig('Control charts.tiff', dpi=600)

    filename = 'ELISASTATS.csv'
    header = ['Concentration', 'Mean OD', 'SD', 'CV']
    rows = map( None, list_of_conc, meanlist, sdlist, cvlist)
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
