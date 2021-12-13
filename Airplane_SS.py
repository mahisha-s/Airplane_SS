# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:11:47 2021

@author: Mahi
"""
#Given input is taken in the form of 2D array
seat = [[3,2], [4,3], [2,3], [3,4]] 
passenger = 30
#entire_record variable holds the all the data where the cell is either A or M or W
entire_record = []
#Initializing other variables
index=0
total_column = 0
total_row = 0
final_seat = []
for element in seat:
    #Assigning Col and row variables 
    col = element[0]
    row = element[1]
    #Finding the maximum column
    max_column = total_column + col
    for row_ele in range(1,row+1):
        #Adding the Aisle and window seats first using if-elif-else
        if(index==0):
            entire_record.append([row_ele, col, "1-A"])
            entire_record.append([row_ele, 1, "2-W"])
        elif index == (len(seat) - 1):
            entire_record.append([row_ele, (total_column + 1), "1-A"])
            entire_record.append([row_ele, max_column, "2-W"])
        else:
            entire_record.append([row_ele, max_column, "1-A"])
            entire_record.append([row_ele, (total_column + 1), "1-A"])
    #Adding the middle seats 
    if (col > 2):
        for row_ele in range(1,row+1):
            for column in range((total_column + 2),(max_column)):
                entire_record.append([row_ele,column, "3-M"])
    total_column += col
    index = index + 1
# First, Sort it according to row and then according to the seating arrangement
entire_record = sorted(entire_record,key=lambda x: x[0])
entire_record = sorted(entire_record,key=lambda x: x[2])
#entire_record has the seating arrangement of all the seats
#final_seat has the seat arrangement only for the given number of passengers
#To display it in a proper format
print ("NO \t ROW \t COLUMN \t SEAT ALLOCATED")
for i in range(passenger):
    final_seat.append(entire_record[i])
    print(str(i+1)+"\t  "+str(entire_record[i][0])+"\t\t\t"+str(entire_record[i][1])+"\t\t\t"+str(entire_record[i][2]))



 







