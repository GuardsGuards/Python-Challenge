# Load the data
import csv

data = csv.DictReader(open('Resources/budget_data.csv'))
my_report = open('Analysis/Budget_Analysis.txt','w')

total = 0
months = 0
pre_rev = 0
total_ch = 0

for row in data:
    months += 1

    rev = int(row['Profit/Losses'])
    total += rev

    ch = rev-pre_rev

    if pre_rev == 0:
        ch = 0

    total_ch += ch

    pre_rev = rev


output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''

print(output)
my_report.write(output)
