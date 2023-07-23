import pandas as pd

def format_line(item_name, hiilihydraatit):
    return f"foodBox.add(Food('Hesburger - {item_name}', {hiilihydraatit}, 'Pikaruoka', 'Hesburger'));\n"

# Define input Excel file path and output file path
input_excel_file = "input_hesburger.xlsx"
output_file = "output_hesburger.txt"

# Read data from Excel into a DataFrame using pandas
df = pd.read_excel(input_excel_file)

# Make sure the column names match the Excel file
if "ITEM NAME" not in df.columns or "HIILIHYDRAATIT" not in df.columns:
    raise ValueError("Column names 'ITEM NAME' and 'HIILIHYDRAATIT' not found in the Excel file.")

with open(output_file, "w", encoding="utf-8") as outfile:
    for index, row in df.iterrows():
        item_name = row["ITEM NAME"]
        hiilihydraatit = float(str(row["HIILIHYDRAATIT"]).replace(',', '.'))  # Handling decimal comma

        if hiilihydraatit > 3:
            formatted_line = format_line(item_name, hiilihydraatit)
            outfile.write(formatted_line)
            print(f"Formatted line: {formatted_line}")

if outfile.closed:
    print("Output file closed.")
else:
    print("Output file not closed.")

print("Formatting completed. Check the 'output_hesburger.txt' file.")
