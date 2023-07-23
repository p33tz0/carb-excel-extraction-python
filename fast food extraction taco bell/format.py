def format_line(line):
    # Split the line by spaces and extract the required information
    parts = line.strip().split(' ')
    item_name = ' '.join(parts[:-9])  # Extract the item name
    hiilihydraatit = float(parts[-4].replace(',', '.'))  # Extract the 4th last number (HIILIHYDRAATIT)

    if "Crispy chicken" in item_name:
        hiilihydraatit /= 2

    return f"foodBox.add(Food('Taco Bell - {item_name}', {hiilihydraatit}, 'Pikaruoka', 'Taco Bell'));\n"

# Define input and output file paths
input_file = "input.txt"
output_file = "output.txt"

# Debug: Print the content of the input file
with open(input_file, "r") as infile:
    input_content = infile.read()
print("Input File Content:")
print(input_content)

with open(input_file, "r") as infile:
    lines = infile.readlines()

# Debug: Print the number of lines read
print("Number of Lines Read:", len(lines))

with open(output_file, "w") as outfile:
    for line in lines:
        formatted_line = format_line(line)
        outfile.write(formatted_line)
        print(f"Formatted line: {formatted_line}")

print("Formatting completed. Check the 'output.txt' file.")
