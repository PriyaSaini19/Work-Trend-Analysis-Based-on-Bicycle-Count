# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:16:45 2019

@author: Priya
"""

#file used to combine 15 minute data to hourly basis
import csv

write_row = []
with open('bicycle_data.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    row_count = 0
    index = 0
    write_count = 0
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0
    t6 = 0
    for row in csv_reader:
        row_count += 1
        if( row_count > 5):
           
#            print(row)
            flag = 0
            for i in row: 
#                print(i)
                if(flag):
                    t_row = i.split(",")
#                    print("t_row")
#                    print(t_row)
                    if(t_row[1] != ""):
                        t1 += int(t_row[1])
#                    print(t1)
                    if(t_row[2] != ""):
                        t2 += int(t_row[2])
                    if(t_row[3] != ""):
                        t3 += int(t_row[3])
                    if(t_row[4] != ""):
                        t4 += int(t_row[4])
                    if(t_row[5] != ""):
                        t5 += int(t_row[5])
                    if(t_row[6] != ""):
                        t6 += int(t_row[6])
                else:
                    date = i.split(",")[1]
                flag = 1
            
            if(index == 3):
                index = 0
                
                temp_row = []
                temp_row.append(write_count)
                temp_row.append(date)
                temp_row.append(write_count%24)
                temp_row.append(t1)
                temp_row.append(t2)
                temp_row.append(t3)
                temp_row.append(t4)
                temp_row.append(t5)
                temp_row.append(t6)
                
                write_row.append(temp_row)
#                print(temp_row)
                write_count += 1
                t1 = 0
                t2 = 0
                t3 = 0
                t4 = 0
                t5 = 0
                t6 = 0
            else:
                index += 1
                    
with open('updated.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["S.No","Date","Time","EBH","WBH","TH","EBM","WBM","TM"])
    for row in write_row:
        spamwriter.writerow(row)

print("ddd")