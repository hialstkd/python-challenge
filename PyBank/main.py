import os
import csv

csvpath = os.path.join('..','python-challenge','Pybank','Resource', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    header = next(csvreader)
    months = []        
    p_l = [] 
    change_rev = []
    for row in csvreader:
        #Total of Profits
        p_l.append(int(row[1]))
        #Total of Months
        months.append(row[0])

        print(row)
    
    for x in range(1,len(p_l)):
        change_rev.append(int(p_l[x])-int(p_l[x-1]))
    
    #The total number of months included in the dataset
    total_months = len(months)

    #The net total amount of "Profit/Losses" over the entire period
    total_p_l = sum(p_l)

    #The average of the changes in "Profit/Losses" over the entire period
    average_rev = sum(change_rev)/ len(change_rev)

    #The greatest increase in profits (date and amount) over the entire period
    max_rev_amount = max(change_rev)
    max_rev_date = months[change_rev.index(max_rev_amount)+1]

    #The greatest decrease in losses (date and amount) over the entire period
    min_rev_amount = min(change_rev)
    min_rev_date = months[change_rev.index(min_rev_amount)+1]

    print(max_rev_date)
    print(min_rev_date)

    print("Financial Analysis")
    print("-------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_p_l))
    print("Average Change: $" + str(average_rev))
    print("Greatest Increase in Profits: " + str(max_rev_date) + "($" + str(max_rev_amount) + ")")
    print("Greatest Decrease in Profits: " + str(min_rev_date) + "($" + str(min_rev_amount) + ")")

    file = open("output.txt","w")
    file.write("Financial Analysis" + '\n')
    file.write("-------------------------------------" + '\n')
    file.write("Total Months: " + str(total_months) + '\n')
    file.write("Total: $" + str(total_p_l) + '\n')
    file.write("Average Change: $" + str(average_rev) + '\n')
    file.write("Greatest Increase in Profits: " + str(max_rev_date) + "($" + str(max_rev_amount) + ")" + '\n')
    file.write("Greatest Decrease in Profits: " + str(min_rev_date) + "($" + str(min_rev_amount) + ")" + '\n')
    file.close()
    


   