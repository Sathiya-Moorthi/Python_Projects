# 1 --> this below code will work for normal txt files
import csv

# Open the text file for reading
with open('sample2.txt', 'r') as txt_file:
    # Specify the delimiter used in the text file
    reader = csv.reader(txt_file, delimiter='\t')  # Adjust delimiter as needed

    # Open the CSV file for writing
    with open('sample2.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write the rows from the text file to the CSV file
        writer.writerows(reader)

# 2 --> this below code will work for all txt files
import csv

# Open the input text file containing the audit queries
with open('a.txt', 'r') as input_file:
    lines = input_file.readlines()

# Extract values from the lines (assuming values are separated by a specific character like ':')
values = [line.split(':')[-1].strip() for line in lines]

# Write the extracted values to a CSV file
with open('a.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    for value in values:
        csv_writer.writerow([value])

print("CSV file with extracted values has been created successfully.")