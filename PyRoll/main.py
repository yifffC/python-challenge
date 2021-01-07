#import csv file
import os
import csv

#Open csv file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    print("Election Results")
    print("----------------------------------------------------")

# The total number of votes cast
    content = []
    votes = []
    candidate = []
    for row in csvreader:
        content.append(row)
        votes.append(row[0])
        candidate.append(row[2])
    names = list(set(candidate))
    counts = [0]*len(names)
#A complete list of candidates who received votes
    for i in range(len(names)):

#The total number of votes each candidate won
        for j in candidate:
            if j == names[i]:
                counts[i] += 1


#The percentage of votes each candidate won
    percentage = []
    for i in counts:
        percentage.append(f"{round(i/len(votes)*100, 3)}%")
    
    maximum = counts[0]
    winner = names[0]
#The winner of the election based on popular vote.
    for i in range(len(counts) - 1):
        if counts[i+1] > maximum:
            maximum = counts[i+1]
            winner = names[i+1]
       
#print results
    roster = zip(names, percentage, counts)
    print(f"Total Votes: {len(votes)}")
    print("----------------------------------------------------")
    lines = []
    for i in roster:
        print(f"{i[0]}: {i[1]} ({i[2]})")
        lines.append(f"{i[0]}: {i[1]} ({i[2]})")
    print("----------------------------------------------------")
    print(f"Winner: {winner}")
    print("----------------------------------------------------")

#export text file
    with open("Analysis/results.txt", 'w') as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("----------------------------------------------------\n")
        txtfile.write(f"Total Votes: {len(votes)}\n")
        txtfile.write("----------------------------------------------------\n")
        for i in lines:
            txtfile.write(i + '\n')
        txtfile.write("----------------------------------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("----------------------------------------------------\n")