import csv
import os

# Define the path to the CSV file in the resources folder
csv_path = os.path.join("resources", "election_data.csv")

# Read the CSV file using the csv module
with open(csv_path, 'r') as file:
    data = csv.reader(file)
   
    # skip header row
    header = next(data) 

    # Calculate the total number of votes cast
    total_votes = 0

    # Create a dictionary to store the total number of votes each candidate won
    candidate_votes = {}

    for row in data:
        # Increment the total number of votes
        total_votes += 1

        # Get the candidate name
        candidate = row[2]

        # Update the candidate's vote count in the dictionary
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    # Calculate the percentage of votes each candidate won
    candidate_percentages = {candidate: votes/total_votes*100 for candidate, votes in candidate_votes.items()}

    # Get the winner of the election based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print the analysis to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentages[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Export the analysis to a text file
    with open('Election_Results.txt', 'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        for candidate, votes in candidate_votes.items():
            percentage = candidate_percentages[candidate]
            file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")
