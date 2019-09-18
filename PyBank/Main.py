#Importing my path
import os
import csv

#define my path to the file
filecsv=os.path.join("..","PythonChallenge","PyBank","PyBank_Resources_budget_data.csv")
#Setting variables
Total_Months=[]
Total_Profits=[]
Average_Change=[]
greatest_decrease=0
greatest_dec_date=" "
greatest_inc_date=" "
greatest_increase=0

#Givin access to read the CSV
with open(filecsv, newline='') as filecsv:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(filecsv, delimiter=',')
       # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header and find our values of interest
    for row in csvreader:
         Total_Months.append(row[0])
         Total_Profits.append(int(float(row[1])))
    # find average change
    for x in range(1, len(Total_Profits)):
        Average_Change.append((int(Total_Profits[x]) - int(Total_Profits[x-1])))
        greatest_decrease=min(Average_Change)
        greatest_increase=max(Average_Change)
    # calculate average revenue change
        changebymonths = sum(Average_Change) / len(Average_Change)

# greatest increase in revenue
#greatest_increase = max([changebymonths])
# greatest decrease in revenue
#greatest_decrease = min([changebymonths])

 #aquí si le quito los corchetes me sale un error de "float is not iterable", pero no me corre el max y el min


print(f"Total Months:{len(Total_Months)}")
print(f"Total Profits:{sum(Total_Profits)}")
print("Average change: " + "$" + str(changebymonths))
print(f"The greatest decrease is {greatest_decrease}")
print(f"The greatest increase is {greatest_increase}")


# output to a text file
file = open("Financial Analysis.txt","w")
file.write("Financial Analysis" + "\n")
file.write("...................................................................................." + "\n")
file.write(f"Total Months:{len(Total_Months)}"+ "\n")
file.write(f"Total Profits:{sum(Total_Profits)}"+ "\n")
file.write("Average change: " + "$" + str(changebymonths)+ "\n")
file.write(f"The greatest decrease is {greatest_decrease}"+ "\n")
file.write(f"The greatest increase is {greatest_increase}"+ "\n")
