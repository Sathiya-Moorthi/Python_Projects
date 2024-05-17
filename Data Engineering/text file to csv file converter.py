import csv

file_name = r"C:\Users\pc1\PycharmProjects\pythonProject1\Climate_result.txt"

# Open text file in read mode
with open(file_name, 'r') as text_file:
    # Create a CSV writer object
    csv_writer = csv.writer(open('Climate_result.csv', 'w'))#, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Read each line from the text file
    for line in text_file:
        # Split the line into values based on the delimiter
        values = line.strip().split(',')  # Change ',' to your delimiter

        # Write the values to the CSV file
        csv_writer.writerow(values)


# the below link contains all the errors that I have faced while running this program and other convo reg pandas, must visit to learn more

"""------------------------------------ chatgpt : https://chatgpt.com/share/a89c4f8d-cddc-4a74-9a8b-c0879e2af324 ------------------------------------------ """