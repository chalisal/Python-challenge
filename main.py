#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:18:29 2024

@author: chalisaoottamakorn
"""#add our dependencies. 
import os
import csv

#Assign a variable to laod a file from a path
input_file = os.path.join(".", "Resources", "election_data.csv")
# Assign a variable to save the file to a path
output_file = os.path.join(".", "analysis", "election_analysis.txt")

#Initialize a total vote counter. 
total_votes = 0

# Candidate Options
candidate_options = []

#Declare a dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = []
winning_candidate_summary = []
winning_count = 0
winning_percentage = 0
election_results = []
candidate_results = []

#Open the election results and read the file. 
with open(input_file) as election_data:

    #To do: read and analyze data here
    #Read the file object with reader function. 
    file_reader = csv.reader(election_data)


#open and read csv
with open(input_file) as input_csv:
    csv_reader = csv.reader(input_csv)
    


    #Read the header row first
    header = next(csv_reader)
    first = next(csv_reader)
    total_votes = total_votes + 1
    
    #Print each row in the CSV file. 
    for row in csv_reader:
        #Add to the total vote count. 
        total_votes += 1
        
        #Print the candidate name from each row. 
        candidate_name = row[2]

        #If the candidate does not match any existing candidate. 
        if candidate_name not in candidate_options: 
            #Add it to the list of candidates. 
            candidate_options.append(candidate_name)
            #Begin tracking that candidates vote count. 
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1
        #Print each candidates voter count & % to terminal. 
        print(candidate_results)

        

    print(election_results, end="")


    for candidate_name in candidate_votes: 
        #Retrieve vote count of a candidate. 
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes. 
        vote_percentage = float(votes) / float(total_votes) * 100
 
     

        #Determine if the votes is greater than winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            #If true then set winning_count = votes & winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #And, set the winning_cand equal to the candidate's name. 
            winning_candidate = candidate_name

     

    print(winning_candidate_summary)

with open(output_file,"w") as output_txt:
        
        
        
        
#Print Output and Add to Output
    output = (
        f"Election Results\n"
        f"-----------------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------------------------------\n"
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------------------------\n")
        
    
    print(output)
    output_txt.write(output)


    
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote


# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------