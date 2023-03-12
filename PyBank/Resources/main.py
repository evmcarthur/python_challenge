import os
import csv

# Set path for file
csv_path =os.path.join("resources","budget_data.csv")

# Initialize variables
total_months = 0
total_profit_loss = 0
prev_row = None
total_change = 0
num_changes = 0
profit_loss_changes = []
greatest_increase_profit = ["", 0]
greatest_decrease_profit = ["", 0]

# Open the CSV
with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    csv_header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Count the total number of months
        total_months += 1

        # Calculate the total profit/loss
        total_profit_loss += int(row[1])

        # Extract the value from the second column of the current row
        current_value = int(row[1])

        # If this isn't the first row, calculate the change and add it to the total
        if prev_row is not None:
            prev_value = int(prev_row[1])
            change = current_value - prev_value
            total_change += change
            num_changes += 1

            # Store the change in profit/loss
            profit_loss_changes.append(change)

            # Calculate the greatest increase and decrease in profits
            if change > greatest_increase_profit[1]:
                greatest_increase_profit[0] = row[0]
                greatest_increase_profit[1] = change 
            if change < greatest_decrease_profit[1]:
                greatest_decrease_profit[0] = row[0]
                greatest_decrease_profit[1] = change

        prev_row = row

# Calculate the average profit/loss changes
if num_changes != 0:
    average_change = total_change / num_changes
else:
    average_change = 0

# Format the output
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit/Loss: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_profit[0]} (${greatest_increase_profit[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_profit[0]} (${greatest_decrease_profit[1]})\n"
)

# Print the output to the terminal
print(output)

# Export the output to a text file
with open("Analysis.txt", "w") as txt_file:
    txt_file.write(output)
