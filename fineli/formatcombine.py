import os
import shutil

def combine_output_files():
    # Get a list of all the output files in the directory
    output_files = [f for f in os.listdir() if f.endswith('-output.txt')]

    # Open the combined output file
    with open('combined_output.txt', 'w', encoding='utf-8') as combined_file:
        # Iterate over the output files
        for output_file in output_files:
            # Check if the file is not empty
            if os.stat(output_file).st_size != 0:
                # Open the output file
                with open(output_file, 'r', encoding='utf-8') as f:
                    # Iterate over the lines in the output file
                    for line in f:
                        # Skip empty lines
                        if line.strip():
                            # Write the line to the combined output file
                            combined_file.write(line)
                    # Add a newline after each file to separate the data
                    combined_file.write('\n')

# Call the function
combine_output_files()
