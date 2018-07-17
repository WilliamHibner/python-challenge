import csv
import os

#Requirements:
    #The total number of months included in the dataset
    #The total net amount of "Profit/Losses" over the entire period
    #The average change in "Profit/Losses" between months over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

#Open and read csv
# with open(budget_data_csv, newline="") as csvfile:
#     csvreader = csv.reader(csvfile, delimeter=",")


total_months = 0
total_net = 0
average_change = 0
greatest_increase = 0
greatest_increase_date = 0
greatest_decrease = 0
greatest_decrease_date = 0
prevRev = 0

# I need to calculate total row for the entire csv file
# open csv
# read the csv
# count rows ? remove header
financial_data = os.path.join("Resources","budget_data.csv")

with open(financial_data) as budget_data:
    budget_data_reader = csv.DictReader(budget_data)

    count = 0
    total_net = 0
    Average = []
    for row in budget_data_reader:
        #number of months
        count += 1
        #total revenue
        total_net = total_net + int(row['Revenue'])
        #average Change
        Change = int(row['Revenue']) - prevRev
        Average.append(Change)
        prevRev = int(row['Revenue'])
        #greatest increase
        if greatest_increase < Change:
            greatest_increase = Change
            greatest_increase_date = row["Date"]
        #greatest decrease
        if greatest_decrease > Change:
            greatest_decrease = Change
            greatest_decrease_date = row["Date"]
      
        

    
#find total number of months included in the dataset
total_months = count

#find total net amount of "Profit/Losses" over the entire period

#calc average change
average_change = sum(Average)/len(Average)

print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(total_months))
print("Total: $"+str(total_net))
print("Average  Change: $"+str(average_change))
print("Greatest Increase in Profits: "+ greatest_increase_date + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: "+ greatest_decrease_date + " ($" + str(greatest_decrease) + ")")


