#import csv file
import os
import csv

#Open csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    print("Final Analysis")
    print("----------------------------------------------------")

#The total number of months included in the dataset
    months = []
    date = []
    profit = 0
    change = []
    delta = 0
    for row in csvreader:
        months.append(row[1])
        date.append(row[0])
#The net total amount of "Profit/Losses" over the entire period
        profit += int(row[1])

#The average of the changes in "Profit/Losses" over the entire period
    for i in range(len(months) - 1):
        change.append(int(months[i+1]) - int(months[i]))
    for i in change:
        delta += i
    maximum = change[0]
    minimum = change[0]
#The greatest increase in profits (date and amount) over the entire period
    for i in range(len(change) - 1):
        if int(change[i+1]) >= maximum:
            maximum = change[i+1]
            max_date = date[i+2]
#The greatest decrease in losses (date and amount) over the entire period
        if int(change[i+1]) <= minimum:
            minimum = change[i+1]
            min_date = date[i+2]


#print results
    average = round(delta/len(change), 2)
    print(f"Total Months: {len(months)}")
    print(f"Total: ${profit}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {max_date} ({maximum})")
    print(f"Greatest Decrease in Profits: {min_date} ({minimum})")

#export text file
    with open("Analysis/results.txt", 'w') as txtfile:
        txtfile.write("Final Analysis\n")
        txtfile.write("----------------------------------------------------\n")
        txtfile.write(f"Total Months: {len(months)}\n")
        txtfile.write(f"Total: ${profit}\n")
        txtfile.write(f"Average Change: ${average}\n")
        txtfile.write(f"Greatest Increase in Profits: {max_date} ({maximum})\n")
        txtfile.write(f"Greatest Decrease in Profits: {min_date} ({minimum})\n")