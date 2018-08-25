import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import glob
import csv
from tkinter import *
from tkinter import messagebox
from itertools import repeat
import helper

font_size=6
matplotlib.rc('font', size=font_size)


#set up the GUI labels
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
    global fig2
    #set up the figures
    fig1 = plt.figure(1)
    ax1 = plt.subplot2grid((6,6), (0,0), colspan=4, rowspan=2)
    ax2 = plt.subplot2grid((6,6), (2,0), colspan=2)
    ax3 = plt.subplot2grid((6,6), (2,2), colspan=2)
    ax4 = plt.subplot2grid((6,6), (3,0), colspan=2)
    ax5 = plt.subplot2grid((6,6), (3,2), colspan=2)
    ax6 = plt.subplot2grid((6,6), (4,0), colspan=2)
    ax7 = plt.subplot2grid((6,6), (4,2), colspan=2)
    ax8 = plt.subplot2grid((6,6), (5,0), colspan=2)
    ax9 = plt.subplot2grid((6,6), (5,2), colspan=2)

    #create empty lists to be filled in the loops
    count = 0 
    counte = 0
    fnames = fnamese = []
    
    y11 = y22 = y33 = y44 = y55 = y66 = y77 = y88 = []
    list_of_superior_y = [y11, y22, y33, y44, y55, y66, y77, y88]
    y11e = y22e = y33e = y44e = y55e = y66e = y77e = y88e = []
    meanind1 = meanind2 = meanind3 = meanind4 = meanind5 = meanind6 = meanind7 = meanind8 = []
    list_of_meanind = [meanind1 , meanind2 , meanind3 , meanind4 , meanind5 , meanind6 , meanind7 , meanind8]
    meanind1e = []
    meanind2e = []
    meanind3e = []
    meanind4e = []
    meanind5e = []
    meanind6e = []
    meanind7e = []
    meanind8e = []

    #convert the userinputs to integers
    userinput1 = e1.get()
    userinput2 = e2.get()
    userinput3 = int(e3.get())
    userinput4 = int(e4.get())
    userinput5 = int(e5.get())
    
    # standards loop
    for files in glob.glob("*%s.csv"%(userinput1)) :
        count=count+1
        fnames.append(files)
        array=np.genfromtxt(files, delimiter=',', skip_header=userinput3-1, usecols=(userinput4-1,userinput5-1))
        
        list_of_slices = [array[0:3], array[3:6], array[6:9], array[9:12],
                          array[12:15], array[15:18], array[18:21], array[21:24]]
        list_of_x = []
        list_of_y = []
        
        for elements in list_of_slices:
            index = 0
            x, y , mean = helper.get_means(elements)
            
            list_of_x.append(x)
            list_of_y.append(y)
            list_of_superior_y[index].append(y)
            list_of_meanind[index].append(mean)
            index += 1
        
        ax1.plot(list_of_x, list_of_y, 'ko', markersize=5)

    # test loop
    if userinput2 is'none':
        print('no test group')
    else:
        for files in glob.glob("*%s.csv"%(userinput2)) :
            counte=counte+1
            fnamese.append(files)
            arraye=np.genfromtxt(files, delimiter=',', skip_header=7, usecols=(1,4))

            array1e=arraye[0:3]
            conc1e=array1e[:,0]
            conc1e = conc1e[np.logical_not(np.isnan(conc1e))]
            inds1e=np.where(np.isnan(array1e))
            array1e[inds1e]=np.take(conc1e, inds1e[1])
            mean1e=np.mean(array1e, axis=0)
            x1e=array1e[:,0]
            y1e=array1e[:,1]    
            y11e.append(y1e)
            meanind1e.append(mean1e)

            array2e=arraye[3:6]
            conc2e=array2e[:,0]
            conc2e = conc2e[np.logical_not(np.isnan(conc2e))]
            inds2e=np.where(np.isnan(array2e))
            array2e[inds2e]=np.take(conc2e, inds2e[1])
            mean2e=np.mean(array2e, axis=0)
            x2e=array2e[:,0]
            y2e=array2e[:,1]    
            y22e.append(y2e)
            meanind2e.append(mean2e)

            array3e=arraye[6:9]
            conc3e=array3e[:,0]
            conc3e = conc3e[np.logical_not(np.isnan(conc3e))]
            inds3e=np.where(np.isnan(array3e))
            array3e[inds3e]=np.take(conc3e, inds3e[1])
            mean3e=np.mean(array3e, axis=0)
            x3e=array3e[:,0]
            y3e=array3e[:,1]    
            y33e.append(y3e)
            meanind3e.append(mean3e)

            array4e=arraye[9:12]
            conc4e=array4e[:,0]
            conc4e = conc4e[np.logical_not(np.isnan(conc4e))]
            inds4e=np.where(np.isnan(array4e))
            array4e[inds4e]=np.take(conc4e, inds4e[1])
            mean4e=np.mean(array4e, axis=0)
            x4e=array4e[:,0]
            y4e=array4e[:,1]    
            y44e.append(y4e)
            meanind4e.append(mean4e)

            array5e=arraye[12:15]
            conc5e=array5e[:,0]
            conc5e = conc5e[np.logical_not(np.isnan(conc5e))]
            inds5e=np.where(np.isnan(array5e))
            array5e[inds5e]=np.take(conc5e, inds5e[1])
            mean5e=np.mean(array5e, axis=0)
            x5e=array5e[:,0]
            y5e=array5e[:,1]    
            y55e.append(y5e)
            meanind5e.append(mean5e)

            array6e=arraye[15:18]
            conc6e=array6e[:,0]
            conc6e = conc6e[np.logical_not(np.isnan(conc6e))]
            inds6e=np.where(np.isnan(array6e))
            array6e[inds6e]=np.take(conc6e, inds6e[1])
            mean6e=np.mean(array6e, axis=0)
            x6e=array6e[:,0]
            y6e=array6e[:,1]    
            y66e.append(y6e)
            meanind6e.append(mean6e)

            array7e=arraye[18:21]
            conc7e=array7e[:,0]
            conc7e = conc7e[np.logical_not(np.isnan(conc7e))]
            inds7e=np.where(np.isnan(array7e))
            array7e[inds7e]=np.take(conc7e, inds7e[1])
            mean7e=np.mean(array7e, axis=0)
            x7e=array7e[:,0]
            y7e=array7e[:,1]    
            y77e.append(y7e)
            meanind7e.append(mean7e)

            array8e=arraye[21:24]
            conc8e=array8e[:,0]
            conc8e = conc8e[np.logical_not(np.isnan(conc8e))]
            inds8e=np.where(np.isnan(array8e))
            array8e[inds8e]=np.take(conc8e, inds8e[1])
            mean8e=np.mean(array8e, axis=0)
            x8e=array8e[:,0]
            y8e=array8e[:,1]    
            y88e.append(y8e)
            meanind8e.append(mean8e)
            
            x=np.concatenate((x1e, x2e, x3e, x4e, x5e, x6e, x7e, x8e))
            y=np.concatenate((y1e, y2e, y3e, y4e, y5e, y6e, y7e, y8e))
            ax1.plot(x,y, 'mo', markersize=5)

    #format the file names for printing in the terminal, and create a count for the x axis of the control charts
    fnames=[x for item in fnames for x in repeat(item, 3)]
    length=len(fnames)
    xmask1=list(range(length/3))
    labels=[fnames]
    printable=np.array(fnames[0::3])
    printcount=np.array(list(range(len(printable))))
    key=np.column_stack((printcount, printable))
    print('Standards Key')
    print(key)

    fnamese=[x for item in fnamese for x in repeat(item, 3)]
    lengthe=len(fnamese)
    xmask1e=list(range(lengthe/3))
    labelse=[fnamese]
    printablee=np.array(fnamese[0::3])
    printcounte=np.array(list(range(len(printablee))))
    keye=np.column_stack((printcounte, printablee))
    print('Test Key')
    print(keye)

    #take the final means, then plot everything
    mean1tot=np.mean(y11)
    y11=np.array(y11)
    SD1=np.std(y11)
    y11=y11.reshape(length,)
    meanind1=np.array(meanind1)
    meanind1=meanind1[ :,1]
    ax2.plot(xmask1, meanind1, 'ko', markersize=7)
    ax2.plot(xmask1, meanind1, 'k')
    ax2.axhline(y=mean1tot)
    ax2.axhline(y=(mean1tot+SD1*2), color='g', linewidth=2)
    ax2.axhline(y=(mean1tot-SD1*2), color='g', linewidth=2)
    ax2.axhline(y=(mean1tot+SD1*3), color='r', linewidth=2)
    ax2.axhline(y=(mean1tot-SD1*3), color='r', linewidth=2)

    mean1tote=np.mean(y11e)
    y11e=np.array(y11e)
    y11e=y11e.reshape(lengthe,)
    meanind1e=np.array(meanind1e)

    if userinput2 =='none':
        pass
    else:
        ax2.plot(xmask1e, meanind1e[ :,1], 'mo')
        ax2.plot(xmask1e, meanind1e[ :,1], 'm')

    mean2tot=np.mean(y22)
    y22=np.array(y22)
    SD2=np.std(y22)
    y22=y22.reshape(length,)
    meanind2=np.array(meanind2)
    meanind2=meanind2[ :,1]
    ax3.plot(xmask1, meanind2, 'ko', markersize=7)
    ax3.plot(xmask1, meanind2, 'k')
    ax3.axhline(y=mean2tot)
    ax3.axhline(y=(mean2tot+SD2*2), color='g', linewidth=2)
    ax3.axhline(y=(mean2tot-SD2*2), color='g', linewidth=2)
    ax3.axhline(y=(mean2tot+SD2*3), color='r', linewidth=2)
    ax3.axhline(y=(mean2tot-SD2*3), color='r', linewidth=2)

    mean2tote=np.mean(y22e)
    y22e=np.array(y22e)
    y22e=y22e.reshape(lengthe,)
    meanind2e=np.array(meanind2e)
    if userinput2 =='none':
        pass
    else:
        ax3.plot(xmask1e, meanind2e[ :,1], 'm')
        ax3.plot(xmask1e, meanind2e[ :,1], 'mo')

    mean3tot=np.mean(y33)
    y33=np.array(y33)
    SD3=np.std(y33)
    y33=y33.reshape(length,)
    meanind3=np.array(meanind3)
    meanind3=meanind3[ :,1]
    ax4.plot(xmask1, meanind3, 'ko', markersize=7)
    ax4.plot(xmask1, meanind3, 'k', linewidth=2)
    ax4.axhline(y=mean3tot)
    ax4.axhline(y=(mean3tot+SD3*2), color='g', linewidth=2)
    ax4.axhline(y=(mean3tot-SD3*2), color='g', linewidth=2)
    ax4.axhline(y=(mean3tot+SD3*3), color='r', linewidth=2)
    ax4.axhline(y=(mean3tot-SD3*3), color='r', linewidth=2)

    mean3tote=np.mean(y33e)
    y33e=np.array(y33e)
    y33e=y33e.reshape(lengthe,)
    meanind3e=np.array(meanind3e)
    if userinput2 =='none':
        pass
    else:
        ax4.plot(xmask1e, meanind3e[ :,1], 'mo')
        ax4.plot(xmask1e, meanind3e[ :,1], 'm')

    mean4tot=np.mean(y44)
    y44=np.array(y44)
    SD4=np.std(y44)
    y44=y44.reshape(length,)
    meanind4=np.array(meanind4)
    meanind4=meanind4[ :,1]
    ax5.plot(xmask1, meanind4, 'ko', markersize=7)
    ax5.plot(xmask1, meanind4, 'k', linewidth=2)
    ax5.axhline(y=mean4tot)
    ax5.axhline(y=(mean4tot+SD4*2), color='g', linewidth=2)
    ax5.axhline(y=(mean4tot-SD4*2), color='g', linewidth=2)
    ax5.axhline(y=(mean4tot+SD4*3), color='r', linewidth=2)
    ax5.axhline(y=(mean4tot-SD4*3), color='r', linewidth=2)

    mean4tote=np.mean(y44e)
    y44e=np.array(y44e)
    y44e=y44e.reshape(lengthe,)
    meanind4e=np.array(meanind4e)
    if userinput2 =='none':
        pass
    else:
        ax5.plot(xmask1e, meanind4e[ :,1], 'mo')
        ax5.plot(xmask1e, meanind4e[ :,1], 'm')

    mean5tot=np.mean(y55)
    y55=np.array(y55)
    SD5=np.std(y55)
    y55=y55.reshape(length,)
    meanind5=np.array(meanind5)
    meanind5=meanind5[ :,1]
    ax6.plot(xmask1, meanind5, 'ko', markersize=7)
    ax6.plot(xmask1, meanind5, 'k')
    ax6.axhline(y=mean5tot)
    ax6.axhline(y=(mean5tot+SD5*2), color='g', linewidth=2)
    ax6.axhline(y=(mean5tot-SD5*2), color='g', linewidth=2)
    ax6.axhline(y=(mean5tot+SD5*3), color='r', linewidth=2)
    ax6.axhline(y=(mean5tot-SD5*3), color='r', linewidth=2)

    mean5tote=np.mean(y55e)
    y55e=np.array(y55e)
    y55e=y55e.reshape(lengthe,)
    meanind5e=np.array(meanind5e)
    if userinput2 =='none':
        pass
    else:
        ax6.plot(xmask1e, meanind5e[ :,1], 'mo')
        ax6.plot(xmask1e, meanind5e[ :,1], 'm')

    mean6tot=np.mean(y66)
    y66=np.array(y66)
    SD6=np.std(y66)
    y66=y66.reshape(length,)
    meanind6=np.array(meanind6)
    meanind6=meanind6[ :,1]
    ax7.plot(xmask1, meanind6, 'ko', markersize=7)
    ax7.plot(xmask1, meanind6, 'k')
    ax7.axhline(y=mean6tot)
    ax7.axhline(y=(mean6tot+SD6*2), color='g', linewidth=2)
    ax7.axhline(y=(mean6tot-SD6*2), color='g', linewidth=2)
    ax7.axhline(y=(mean6tot+SD6*3), color='r', linewidth=2)
    ax7.axhline(y=(mean6tot-SD6*3), color='r', linewidth=2)

    mean6tote=np.mean(y66e)
    y66e=np.array(y66e)
    y66e=y66e.reshape(lengthe,)
    meanind6e=np.array(meanind6e)
    if userinput2 =='none':
        pass
    else:
        ax7.plot(xmask1e, meanind6e[ :,1], 'mo')
        ax7.plot(xmask1e, meanind6e[ :,1], 'm')

    mean7tot=np.mean(y77)
    y77=np.array(y77)
    SD7=np.std(y77)
    y77=y77.reshape(length,)
    meanind7=np.array(meanind7)
    meanind7=meanind7[ :,1]
    ax8.plot(xmask1, meanind7, 'ko', markersize=7)
    ax8.plot(xmask1, meanind7, 'k')
    ax8.axhline(y=mean7tot)
    ax8.axhline(y=(mean7tot+SD7*2), color='g', linewidth=2)
    ax8.axhline(y=(mean7tot-SD7*2), color='g', linewidth=2)
    ax8.axhline(y=(mean7tot+SD7*3), color='r', linewidth=2)
    ax8.axhline(y=(mean7tot-SD7*3), color='r', linewidth=2)

    mean7tote=np.mean(y77e)
    y77e=np.array(y77e)
    y77e=y77e.reshape(lengthe,)
    meanind7e=np.array(meanind7e)
    if userinput2 =='none':
        pass
    else:
        ax8.plot(xmask1e, meanind7e[ :,1], 'mo')
        ax8.plot(xmask1e, meanind7e[ :,1], 'm')

    mean8tot=np.mean(y88)
    y88=np.array(y88)
    SD8=np.std(y88)
    y88=y88.reshape(length,)
    meanind8=np.array(meanind8)
    meanind8=meanind8[ :,1]
    ax9.plot(xmask1, meanind8, 'ko', markersize=7)
    ax9.plot(xmask1, meanind8, 'k')
    ax9.axhline(y=mean8tot)
    ax9.axhline(y=(mean8tot+SD8*2), color='g', linewidth=2)
    ax9.axhline(y=(mean8tot-SD8*2), color='g', linewidth=2)
    ax9.axhline(y=(mean8tot+SD8*3), color='r', linewidth=2)
    ax9.axhline(y=(mean8tot-SD8*3), color='r', linewidth=2)

    mean8tote=np.mean(y88e)
    y88e=np.array(y88e)
    y88e=y88e.reshape(lengthe,)
    meanind8e=np.array(meanind8e)
    if userinput2 =='none':
        pass
    else:
        ax9.plot(xmask1e, meanind8e[ :,1], 'mo')
        ax9.plot(xmask1e, meanind8e[ :,1], 'm')

    ax1.set_xlabel('Concentration')
    ax1.set_ylabel('OD')
    ax2.set_ylabel('OD')
    ax4.set_ylabel('OD')
    ax6.set_ylabel('OD')
    ax8.set_ylabel('OD')
    ax2.set_xlabel('%s ug/mL' %conc1)
    ax3.set_xlabel('%s ug/mL'%conc2)
    ax4.set_xlabel('%s ug/mL'%conc3)
    ax5.set_xlabel('%s ug/mL'%conc4)
    ax6.set_xlabel('%s ug/mL'%conc5)
    ax7.set_xlabel('%s ug/mL'%conc6)
    ax8.set_xlabel('%s ug/mL'%conc7)
    ax9.set_xlabel('%s ug/mL'%conc8)

    out21=[np.where(np.logical_or(meanind1>mean1tot+SD1*2, meanind1<mean1tot-SD1*2))]
    out31=[np.where(np.logical_or(meanind1>mean1tot+SD1*3, meanind1<mean1tot-SD1*3))]
    out21fnames=np.take(printable, out21)
    out31fnames=np.take(printable, out31)
    if userinput2 =='none':
        pass
    else:
        out21e=[np.where(np.logical_or(meanind1e[ :,1]>mean1tot+SD2*2, meanind1e[ :,1]<mean1tot-SD1*2))]
        out21fnamese=np.take(printablee, out21e)
        print("Test set outside 2SD at %s: \n %s"%(conc1, out21fnamese))
        out31e=[np.where(np.logical_or(meanind1e[ :,1]>mean1tot+SD2*3, meanind1e[ :,1]<mean1tot-SD1*3))]
        out31fnamese=np.take(printablee, out31e)
        print("Test set outside 3SD at %s: \n %s"%(conc1, out31fnamese))
    print("Control set outside 2SD at %s: \n %s"%(conc1, out21fnames))
    print("Control set outside 3SD at %s: \n %s"%(conc1, out31fnames))

    out22=[np.where(np.logical_or(meanind2>mean2tot+SD2*2, meanind2<mean2tot-SD2*2))]
    out22fnames=np.take(printable, out22)
    out32=[np.where(np.logical_or(meanind2>mean2tot+SD2*3, meanind2<mean2tot-SD2*3))]
    out32fnames=np.take(printable, out32)
    if userinput2 =='none':
        pass
    else:
        out22e=[np.where(np.logical_or(meanind2e[ :,1]>mean2tot+SD2*2, meanind2e[ :,1]<mean2tot-SD2*2))]
        out22fnamese=np.take(printablee, out22e)
        print("Test set outside 2SD at %s: \n %s"%(conc2, out22fnamese))
        out32e=[np.where(np.logical_or(meanind2e[ :,1]>mean2tot+SD2*3, meanind2e[ :,1]<mean2tot-SD2*3))]
        out32fnamese=np.take(printablee, out32e)
        print("Test set outside 3SD at %s: \n %s"%(conc2, out32fnamese))
    print("Control set outside 2SD at %s: \n %s"%(conc2, out22fnames))
    print("Control set outside 3SD at %s: \n %s"%(conc2, out32fnames))

    out23=[np.where(np.logical_or(meanind3>mean3tot+SD3*2, meanind3<mean3tot-SD3*2))]
    out23fnames=np.take(printable, out23)
    out33=[np.where(np.logical_or(meanind3>mean3tot+SD3*3, meanind3<mean3tot-SD3*3))]
    out33fnames=np.take(printable, out33)
    if userinput2 =='none':
        pass
    else:
        out23e=[np.where(np.logical_or(meanind3e[ :,1]>mean3tot+SD3*2, meanind3e[ :,1]<mean3tot-SD3*2))]
        out23fnamese=np.take(printablee, out23e)
        print("Test set outside 2SD at %s: \n %s"%(conc3, out23fnamese))
        out33e=[np.where(np.logical_or(meanind3e[ :,1]>mean3tot+SD3*3, meanind3e[ :,1]<mean3tot-SD3*3))]
        out33fnamese=np.take(printablee, out33e)
        print("Test set outside 3SD at %s: \n %s"%(conc3, out33fnamese))
    print("Control set outside 2SD at %s: \n %s"%(conc3, out23fnames))
    print("Control set outside 3SD at %s: \n %s"%(conc3, out33fnames))

    out24=[np.where(np.logical_or(meanind4>mean4tot+SD4*2, meanind4<mean4tot-SD4*2))]
    out24fnames=np.take(printable, out24)
    out34=[np.where(np.logical_or(meanind4>mean4tot+SD4*3, meanind4<mean4tot-SD4*3))]
    out34fnames=np.take(printable, out34)
    if userinput2 =='none':
        pass
    else:
        out24e=[np.where(np.logical_or(meanind4e[ :,1]>mean4tot+SD4*2, meanind4e[ :,1]<mean4tot-SD4*2))]
        out24fnamese=np.take(printablee, out24e)
        print("Test set outside 2SD at %s: \n %s"%(conc4, out24fnamese))
        out34e=[np.where(np.logical_or(meanind4e[ :,1]>mean4tot+SD4*3, meanind4e[ :,1]<mean4tot-SD4*3))]
        out34fnamese=np.take(printablee, out34e)
        print("Test set outside 3SD at %s: \n %s"%(conc4, out34fnamese))
    print("Control set outside 2SD at %s: \n %s"%(conc4, out24fnames))
    print("Control set outside 3SD at %s: \n %s"%(conc4, out34fnames))

    out25=[np.where(np.logical_or(meanind5>mean5tot+SD5*2, meanind5<mean5tot-SD5*2))]
    out25fnames=np.take(printable, out25)
    out35=[np.where(np.logical_or(meanind5>mean5tot+SD5*3, meanind5<mean5tot-SD5*3))]
    out35fnames=np.take(printable, out35)
    if userinput2 =='none':
        pass
    else:
        out25e=[np.where(np.logical_or(meanind5e[ :,1]>mean5tot+SD5*2, meanind5e[ :,1]<mean5tot-SD5*2))]
        out25fnamese=np.take(printablee, out25e)
        print("Test set outside 2SD at %s: \n %s"%(conc5, out25fnamese))
        out35e=[np.where(np.logical_or(meanind5e[ :,1]>mean5tot+SD5*3, meanind5e[ :,1]<mean5tot-SD5*3))]
        out35fnamese=np.take(printablee, out35e)
        print("Test set outside 3SD at %s: \n %s"%(conc5, out35fnamese))
    print("Control set outside 2SD at %s: \n %s"%(conc5, out25fnames))
    print("Control set outside 3SD at %s: \n %s"%(conc5, out35fnames))

    out26=[np.where(np.logical_or(meanind6>mean6tot+SD6*2, meanind6<mean6tot-SD6*2))]
    out26fnames=np.take(printable, out26)
    out36=[np.where(np.logical_or(meanind6>mean6tot+SD6*3, meanind6<mean6tot-SD6*3))]
    out36fnames=np.take(printable, out36)
    if userinput2 =='none':
        pass
    else:
        out26e=[np.where(np.logical_or(meanind6e[ :,1]>mean6tot+SD6*2, meanind6e[ :,1]<mean6tot-SD6*2))]
        out26fnamese=np.take(printablee, out26e)
        print("Test set outside 2SD at %s: \n %s"%(conc6, out26fnamese))
        out36e=[np.where(np.logical_or(meanind6e[ :,1]>mean6tot+SD6*3, meanind6e[ :,1]<mean6tot-SD6*3))]
        out36fnamese=np.take(printablee, out36e)
        print("Test set outside 3SD at %s: \n %s"%(conc6, out36fnamese))
    print("Control set outside 2SD at %s: \n %s"%(conc6, out26fnames))
    print("Control set outside 3SD at %s: \n %s"%(conc6, out36fnames))

    out27=[np.where(np.logical_or(meanind7>mean7tot+SD7*2, meanind7<mean7tot-SD7*2))]
    out27fnames=np.take(printable, out27)
    out37=[np.where(np.logical_or(meanind7>mean7tot+SD7*3, meanind7<mean7tot-SD7*3))]
    out37fnames=np.take(printable, out37)
    if userinput2 =='none':
        pass
    else:
        out27e=[np.where(np.logical_or(meanind7e[ :,1]>mean7tot+SD7*2, meanind7e[ :,1]<mean7tot-SD7*2))]
        out27fnamese=np.take(printablee, out27e)
        print("Test set outside 2SD at %s: \n %s"%(conc7, out27fnamese))
        out37e=[np.where(np.logical_or(meanind7e[ :,1]>mean7tot+SD7*3, meanind7e[ :,1]<mean7tot-SD7*3))]
        out37fnamese=np.take(printablee, out37e)
        print("Test set outside 3SD at %s: \n %s"%(conc7, out37fnamese))
    print("Control set outside 2SD at %s: \n %s"%(conc7, out27fnames))
    print("Control set outside 3SD at %s: \n %s"%(conc7, out37fnames))

    out28=[np.where(np.logical_or(meanind8>mean8tot+SD8*2, meanind8<mean8tot-SD8*2))]
    out28fnames=np.take(printable, out28)
    out38=[np.where(np.logical_or(meanind8>mean8tot+SD8*3, meanind8<mean8tot-SD8*3))]
    out38fnames=np.take(printable, out38)
    if userinput2 =='none':
        pass
    else:
        out28e=[np.where(np.logical_or(meanind8e[ :,1]>mean8tot+SD8*2, meanind8e[ :,1]<mean8tot-SD8*2))]
        out28fnamese=np.take(printablee, out28e)
        print("Test set outside 2SD at %s: \n %s"%(conc8, out28fnamese))
        out38e=[np.where(np.logical_or(meanind8e[ :,1]>mean8tot+SD8*3, meanind8e[ :,1]<mean8tot-SD8*3))]
        out38fnamese=np.take(printablee, out38e)
        print("Test set outside 3SD at %s: \n %s"%(conc8, out38fnamese))
    print("Control set outside 2SD at %s: \n %s"%(conc8, out28fnames))
    print("Control set outside 3SD at %s: \n %s"%(conc8, out38fnames))

    fig1.tight_layout()
    fig1.subplots_adjust(wspace=2.5, hspace=1)
    plt.show()
    fig1.savefig('Control charts.tiff', dpi=600)

    #coeffeints of variance
    cv1=(SD1/mean1tot)*100
    cv2=(SD2/mean2tot)*100
    cv3=(SD3/mean3tot)*100
    cv4=(SD4/mean4tot)*100
    cv5=(SD5/mean5tot)*100
    cv6=(SD6/mean6tot)*100
    cv7=(SD7/mean7tot)*100
    cv8=(SD8/mean8tot)*100

    conclist=[conc1, conc2, conc3, conc4, conc5, conc6, conc7, conc8]
    meanlist=[mean1tot, mean2tot,mean3tot,mean4tot,mean5tot,mean6tot,mean7tot,mean8tot]
    sdlist=[SD1,SD2,SD3,SD4,SD5,SD6,SD7,SD8]
    cvlist=[cv1,cv2,cv3,cv4,cv5,cv6,cv7,cv8]

    filename = 'ELISASTATS.csv'
    header = ['Concentration', 'Mean OD', 'SD', 'CV']
    rows = map(None, conclist, meanlist, sdlist, cvlist)
    with open(filename, 'wb') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)

def popup():
    tkMessageBox.showinfo(
        "Help",
        "Tag must appear immediately prior to the .csv \n Example: if the included tag is 'good', and test tag is 'test' \n appropriate file naming could be Plate1good.csv and Plate1test.csv \n For more help, see user manual")


Button(master, text='Run', command=graphs).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Tags help', command=popup).grid(row=5, column=4, sticky=W, pady=4)

mainloop()