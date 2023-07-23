def format_line(line):
    # Split the line by comma and extract the required information
    item_name, hiilihydraatit = line.strip().split(',')
    hiilihydraatit = float(hiilihydraatit.replace(',', '.'))
    
    return f"foodBox.add(Food('McDonalds - {item_name}', {hiilihydraatit}, 'Pikaruoka', 'McDonalds'));\n"

# Define input and output file paths
input_file = "input.txt"
output_file = "output_mcdonalds.txt"

with open(input_file, "r") as infile:
    lines = infile.readlines()

with open(output_file, "w") as outfile:
    for line in lines:
        formatted_line = format_line(line)
        outfile.write(formatted_line)
        print(f"Formatted line: {formatted_line}")

print("Formatting completed. Check the 'output_mcdonalds.txt' file.")
