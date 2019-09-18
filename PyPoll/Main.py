#setting my environment
import csv
import os

#defining the path
PyPollcsv =os.path.join("..","PythonChallenge","PyPoll","Election_data.csv")

"setting my variable"
count = 0
candidatename = []
candidate = []
vote_count = []
vote_percent = []

# giving access to my file

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # reading the information by row
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatename
        candidatename.append(row[2])
        # Create a set from the candidatename to get the unique candidate names
    for x in set(candidatename):
        candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatename.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = candidate[vote_count.index(winning_vote_count)]
    

# Printing the results
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(candidate)):
            print(candidate[i] + ": " + str(round(vote_percent[i])) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#sending to a file 
with open("PollResults.txt", "w") as file:
    file.write("-------------------------")
    file.write("Election Results")   
    file.write("-------------------------")
    file.write("Total Votes :" + str(count))    
    file.write("-------------------------")
    for i in range(len(candidate)):
            file.write(candidate[i] + ": " + str(round(vote_percent[i])) +"% (" + str(vote_count[i])+ ")")
    file.write("-------------------------")
    file.write("The winner is: " + winner)
    file.write("-------------------------")
    

