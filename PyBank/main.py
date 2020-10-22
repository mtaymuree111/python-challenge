#first import the dependencies 
import os

import csv
#find the file and open it; as we will move this to a text file, create that path as well

csvpath = 'Resources/budget_data.csv' 
file_to_output = '../PyBank/PyBank_output.txt'

#read the file that you have created a path to and read the file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    

    csv_header = next(csvreader)
    

#need to look at the data after the header thus asking to go to next row

    first_row = next(csvreader)
    
#defining our key variables

    total_months = 1
    total_difference = 0
    initial_profit = int(first_row[1])
    greatest_increase = 0
    greatest_increase_month= ""
    greatest_decrease = 0
    greatest_decrease_month= ""
    count_net_difference = 0
    total =  int(first_row[1])
    

    
#loop thru the csv file with our key variables looking at the rows in pairs to compare the greatest increase and decrease
    for row in csvreader:
      
        total_months += 1
        total += int(row[1])
        
 
        net_difference = int(row[1]) - initial_profit
        count_net_difference += 1 
        total_difference = total_difference + net_difference

        initial_profit = int(row[1])

        if net_difference > greatest_increase: 
            greatest_increase = net_difference
            greatest_increase_month = row[0]
        if net_difference < greatest_decrease:
            greatest_decrease =  net_difference 
            greatest_decrease_month = row[0]
#basic math to caculate the change
    average_change = total_difference / count_net_difference


#print out final analysis using print function
    
    print("Financial Analysis")
    print("--------------------------------------")

    print("Total Months: " + str(total_months))
    print("Total: $" + str(total))
    print("Average Change: $" + str(round(average_change,2)))
    print("Greatest Increase in Profits:"  +  str(greatest_increase_month) + "($" + str(greatest_increase) + ")" ) 
    print("Greatest Decrease in Profits:" + str(greatest_decrease_month) +  "($" + str(greatest_decrease) + ")" )

#send to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis")

    txt_file.write("\n")
    txt_file.write("--------------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total: $" + str(total))
    txt_file.write("\n")
    txt_file.write("Average Change: $" + str(round(average_change,2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits:"  +  str(greatest_increase_month) + "($" + str(greatest_increase) + ")" )
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits:" + str(greatest_decrease_month) +  "($" + str(greatest_decrease) + ")")



