#python challenge: pyPoll

#set variables and stuff, also import csv library or something so that it'll work
import csv
spreadsheet_path = 'Resources/election_data.csv'
output_path = 'Analysis/election_output.txt'

#make a list for the things to live in
candidates = []
votes = {}

#look at the csv file and get the data all set up, have it skip the header
with open(spreadsheet_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if row[2] not in candidates:
            candidates.append(row[2])
            votes[row[2]] = 0
        votes[row[2]] +=1

#convert the votes to a number and add them up
for key in votes:
    votes[key] = int(votes[key])

total_votes = 0
for value in votes.values():
    total_votes += value

#get some variables together to make the analysis values
charles_votes = votes['Charles Casper Stockham']
diana_votes = votes['Diana DeGette']
raymon_votes = votes['Raymon Anthony Doane']

charles_percentage = round(((charles_votes/total_votes)*100),3)
diana_percentage = round(((diana_votes/total_votes)*100),3)
raymon_percentage = round(((raymon_votes/total_votes)*100),3)

winning_total = max(votes.values())
winner_election = next(key for key, value in votes.items() if value == winning_total)



#print an output in the python terminal
election_output = (
f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {total_votes}\n"
f"-------------------------\n"
f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})\n"
f"Diana DeGette: {diana_percentage}% ({diana_votes})\n"
f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})\n"
f"-------------------------\n"
f"Winner: {winner_election}\n"
f"-------------------------"
)
print(election_output)

#make a nice lil text file with the same results hooray
with open(output_path, 'w') as output_file:
    output_file.write(election_output)

