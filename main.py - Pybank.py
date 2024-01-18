#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:39:19 2024

@author: chalisaoottamakorn
"""

import os
import csv

#define variables
total_months = 0
total_net = 0
net_change = []
month_change = []
total = 0
greatest_increase = ["",99999]
greatest_decrease = ["",0]
previous_net = []

input_file = os.path.join(".", "Resources", "budget_data.csv")
output_file = os.path.join(".", "analysis", "budget_analysis.txt")

#open and read csv
with open(input_file) as input_csv:
    csv_reader = csv.reader(input_csv)
    
    #Read the header row first
    header = next(csv_reader)
    first = next(csv_reader)
    total_months = total_months + 1
    total_net += int(first[1])
    previous = int(first[1])    
  
    
    
    for x in csv_reader:
        total_months = total_months + 1
        total_net += int(x[1])
        change = int(x[1]) - int(previous_net)
        net_change += [change] 
        month = (x[0])
        previous_net = int(x[1])
                  
                                
        
    # find revenue change
    revenue_change = []

    #calculate the greatest increase
    if net_change  > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = net_change
    
    #calculate the greatest decrease
    if net_change < greatest_decrease[1]:
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = net_change
        
average_change = sum(net_change)/len(net_change)

with open(output_file,"w") as output_txt:
        
    output = (
       f"Financial Analysis\n"
       f"--------------------------------------\n"
       f"Total Months: {total_months}\n"
       f"Total: {total_net}\n"
       f"Average Change: ${average_change}\n"
       f"Greatest Increase in Profits: {greatest_increase[0]} {greatest_increase[1]}\n"
       f"Greatest Decrease in Profits: {greatest_increase[0]} {greatest_increase[1]}\n"
       )
    print(output)
    output_txt.write(output)
    
    #Find the total number of months included in the dataset
    #Find the net total amount of "Profit/Losses" over the entire period
    #Find the changes in "Profit/Losses" over the entire period, and then the average of those changes
    #Find the greatest increase in profits (date and amount) over the entire period
    #Find the greatest decrease in profits (date and amount) over the entire period
    
#     Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)