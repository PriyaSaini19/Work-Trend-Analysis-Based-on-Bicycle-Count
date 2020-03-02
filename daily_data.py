# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:23:51 2019

@author: Priya
"""
#file to convert hourly data to daily data
import csv

write_row = []
eb_count = 0
wb_count = 0
tb_count = 0
ebm_count = 0
wbm_count = 0
tbm_count = 0
final_data = []

c = 0
with open('updated.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = True
    row_count = 0
    for row in csv_reader:
        if(i):
            i = False
            continue
        
#        print(row)
        row_count += 1
        c += 1
#        temp = row.split(",")
        temp = row
        eb_count += int(temp[3])
        wb_count += int(temp[4])
        tb_count += int(temp[5])
        ebm_count += int(temp[6])
        wbm_count += int(temp[7])
        tbm_count += int(temp[8])
        
        if(row_count == 24):
            row_count = 0
            temp_data = []
            temp_data.append(temp[1])
            temp_data.append(eb_count)
            temp_data.append(wb_count)
            temp_data.append(tb_count)
            temp_data.append(ebm_count)
            temp_data.append(wbm_count)
            temp_data.append(tbm_count)
            
            final_data.append(temp_data)
            
            eb_count = 0
            wb_count = 0
            tb_count = 0
            ebm_count = 0
            wbm_count = 0
            tbm_count = 0
            
        
        
#        if(c == 75):
#            break

#print(final_data)
with open('daily_data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["Date","EBH","WBH","TH","EBM","WBM","TM"])
    for row in final_data:
        spamwriter.writerow(row)

print("ddd")
    