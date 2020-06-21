import os
import csv

csvpath = os.path.join('python-challenge','PyPoll','Resource', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    header = next(csvreader)
    votes = 0
    candidate = []
    count = {}

    for row in csvreader:
        votes += 1
        candidate_list = row[2]
        
        if candidate_list not in candidate:
            candidate.append(candidate_list)
            count[(candidate_list)] = 1
        else: 
            count[candidate_list] += 1

winner = max(count, key=count.get)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")
print("khan: " + str(count["Khan"]/votes*100) + "%" + "(" + str(count["Khan"]) +")")
print("Correy: " + str(count["Correy"]/votes*100) + "%" + "(" + str(count["Correy"]) +")")
print("Li: " + str(count["Li"]/votes*100) + "%" + "(" + str(count["Li"]) +")")
print("O'Tooley: " + str(count["O'Tooley"]/votes*100) + "%" + "(" + str(count["O'Tooley"]) +")")
print("-------------------------")
print("Winner: " + str(winner))    

file = open("output.txt","w")
file.write("Election Results" + '\n')
file.write("-------------------------" + '\n')
file.write("Total Votes: " + str(votes))
file.write("khan: " + str(count["Khan"]/votes*100) + "%" + "(" + str(count["Khan"]) +")" + '\n')
file.write("Correy: " + str(count["Correy"]/votes*100) + "%" + "(" + str(count["Correy"]) +")" + '\n')
file.write("Li: " + str(count["Li"]/votes*100) + "%" + "(" + str(count["Li"]) +")" + '\n')
file.write("O'Tooley: " + str(count["O'Tooley"]/votes*100) + "%" + "(" + str(count["O'Tooley"]) +")" + '\n')
file.write("-------------------------" + '\n')
file.write("Winner: " + str(winner) + '\n')
file.close()

