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
