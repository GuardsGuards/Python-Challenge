# Load the data
import csv

data = csv.DictReader(open('Resources/election_data.csv'))
my_report = open('Analysis/Poll_Analysis.txt','w')

total = 0
Candidates = {}

for row in data : 
    total += 1

    Candidate = row["Candidate"]

    if Candidate not in Candidates.keys():
        Candidates[Candidate] = 0

    Candidates[Candidate] += 1

output = f'''
Election Results
-------------------------
Total Votes: {total:,}
-------------------------
'''
win_votes = 0


for Can in Candidates.keys():
    votes = Candidates[Can]

    if votes > win_votes:
        win_votes = votes
        winner = Can

    output += f'{Can}: {votes/total*100:.3f}% ({votes:,})\n'

output +=  f'-----------------\nWinner: {winner} \n-----------------'

print(output)
my_report.write(output)