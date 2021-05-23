import csv
import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)
# Assign a variable for the file to load and the path 
file_to_load = os.path.join('/Users/narda/Desktop/election_analysis/Resources/election_results.csv')
# Open the election results and read the file
with open(file_to_load,'r') as election_data:

     # To do: perform analysis.
     print(election_data)
# Close the file
#election_data.close()

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:
    # write some data to the file. 
    #txt_file.write("Hello World")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('/Users/narda/Desktop/election_analysis/analysis/election_analysis.txt')
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Print each row in the CSV file.
    # for row in file_reader:
       # print(row)
      # Print the header row.
    headers = next(file_reader)
    print(headers)