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
greatest_decrease = 0

# I need to calculate total row for the entire csv file
# open csv
# read the csv
# count rows ? remove header
financial_data = os.path.join("Resources","budget_data.csv")

with open(financial_data) as budget_data:
    budget_data_reader = csv.DictReader(budget_data)

    count = 0
    for r in budget_data_reader:
        count +=1
        print(r['Revenue'], count)

    
#find total number of months included in the dataset


#find total net amount of "Profit/Losses" over the entire period
#set total revenue = 0 
# greatest_inc = revenue[0]
# greatest_dec = revenue[0]
# total_revenue = 0

# #loop through revenue indices and compare # to find greatest inc and dec
# #also add each revenue to total revenue
# for r in range(len(revenue)):
#     if revenue[r] >= greatest_inc:
#         greatest_inc = revenue[r]
#         great_inc_month = months[r]
#     elif revenue[r] <= greatest_dec:
#         greatest_dec = revenue[r]
#         great_dec_month = months[r]
#     total_revenue += revenue[r]

# #Calculate average change in "Profit/Losses" between months over the entire period
# average_change = round(total_revenue/total_months, 2)

# #sets path for output file
# output_dest = os.path.join('Output','pybank_output_' + str(file_num) + '.txt')

# # opens the output destination in write mode and prints the summary
# with open(output_dest, 'w') as writefile:
#     writefile.writelines('Financial Analysis\n')
#     writefile.writelines('----------------------------' + '\n')
#     writefile.writelines('Total Months: ' + str(total_months) + '\n')
#     writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
#     writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
#     writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
#     writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

# #opens the output file in r mode and prints to terminal
# with open(output_dest, 'r') as readfile:
#     print(readfile.read())

