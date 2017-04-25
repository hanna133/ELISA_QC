
#use this to split one .xlsx file into multiple. I wrote this because my lab was routinetly running three standard curves on one plate.
import pandas as pd
#file name to be split
file = 'original file name.xlsx'
#Name of the tab
xl = pd.ExcelFile(file)
df1 = xl.parse('03.06.2017 Plate 1 Comp. of Old')

#the row numbers where you want to split the file
s1=df1.loc[21:44]
s2=df1.loc[49:72]
s3=df1.loc[77:100]

#the names of the three resulting files 
writer = pd.ExcelWriter('new file name1.xlsx', engine='xlsxwriter')
s1.to_excel(writer, 'Sheet1')
writer.save()

writer = pd.ExcelWriter('new file name 2.xlsx', engine='xlsxwriter')
s2.to_excel(writer, 'Sheet1')
writer.save()

writer = pd.ExcelWriter('new file name 3.xlsx', engine='xlsxwriter')
s3.to_excel(writer, 'Sheet1')
writer.save()