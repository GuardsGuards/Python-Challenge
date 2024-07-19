import pandas as pd

# Load the data
file_path = 'budget_data.csv'
df = pd.read_csv(file_path)

# Calculate the total number of months
total_months = df['Date'].nunique()

# Calculate the net total amount of "Profit/Losses" over the entire period
total_profit_losses = df['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
df['Profit/Losses Change'] = df['Profit/Losses'].diff()

# Calculate the average of those changes
average_change = df['Profit/Losses Change'].mean()

# Find the greatest increase in profits (date and amount)
greatest_increase = df.loc[df['Profit/Losses Change'].idxmax()]
greatest_increase_date = greatest_increase['Date']
greatest_increase_amount = greatest_increase['Profit/Losses Change']

# Find the greatest decrease in profits (date and amount)
greatest_decrease = df.loc[df['Profit/Losses Change'].idxmin()]
greatest_decrease_date = greatest_decrease['Date']
greatest_decrease_amount = greatest_decrease['Profit/Losses Change']

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount:.2f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount:.2f})")

import pandas as pd

# Load the data
file_path = 'election_data.csv'
df = pd.read_csv(file_path)

# Calculate the total number of votes
total_votes = df['Ballot ID'].nunique()

# Get a complete list of candidates who received votes
candidates = df['Candidate'].unique()

# Calculate the total number of votes each candidate won
vote_counts = df['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
vote_percentages = (vote_counts / total_votes) * 100

# Determine the winner of the election based on popular vote
winner = vote_counts.idxmax()

# Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
