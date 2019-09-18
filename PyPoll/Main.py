#Importing my path
import os
import csv

#define my path to the file
filecsv=os.path.join("..","PythonChallenge","PyPoll","Election_data.csv")

#setting the variables
votes = 0
candidatelist = []
candidatename = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(filecsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # define the information
    for row in csvreader:
        # Count the total number of votes
        votes = votes + 1
        # Set the candidate names to list
        candidatelist.append(row[2])
        # Create a list the names
    for x in list(candidatelist):
        candidatename.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/votes)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    
# output to a text file
#file = open("PollResults.txt","w")
#file.write("Election Results" + "\n")
#file.write("...................................................................................." + "\n")
#file.write(f"Total votes:(Votes)"+ "\n")
#file.write("...................................................................................." + "\n")
#file.write()
#file.close()
