#python challenge: pyBank

#set variables and stuff, also import csv library or something so that it'll work
import csv
spreadsheet_path = 'Resources/budget_data.csv'
output_path = 'Analysis/budget_output.txt'

months = []

incomes = []
incomes_changes_list = []

#look at the csv file and get the data all set up, have it skip the first row
with open(spreadsheet_path, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    first_data_row = next(csv_reader)
    months.append(first_data_row[0])
    incomes.append(int(first_data_row[1]))
    previous_value = int(first_data_row[1])

    #find out the numbers for the math, set stuff initially up as the second row, so same math can be used for all of the numbers
    for row in csv_reader:
        months.append(row[0])
        incomes.append(int(row[1]))
        current_value = int(row[1])
        income_difference = current_value - previous_value
        incomes_changes_list.append(income_difference)
        previous_value = int(row[1])

#do some math and set some variables
average_change = round(sum(incomes_changes_list)/len(incomes_changes_list),2)
max_index = incomes_changes_list.index(max(incomes_changes_list))
min_index = incomes_changes_list.index(min(incomes_changes_list))
max_month = months[max_index+1]
min_month = months[min_index+1]

#print the results in the python terminal, in a format that matches the guide on canvas
income_output = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(months)}\n"
f"Total: ${sum(incomes)}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_month} (${max(incomes_changes_list)})\n"
f"Greatest Decrease in Profits: {min_month} (${min(incomes_changes_list)})"
)
print(income_output)

#make a nice lil text file with the same results hooray
with open(output_path, 'w') as output_file:
    output_file.write(income_output)