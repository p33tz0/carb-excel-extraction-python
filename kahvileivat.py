import pandas as pd

# Read the Excel sheet
df = pd.read_excel(r'.\hhtiedot\kahvileivat.xlsx')
print(df.columns)
# Create a list to store the formatted data
formatted_data = []

# Iterate over the rows and format the data
for i in range(len(df)):
    food_name = df['Ruoka-aine'][i]
    serving_size = df['Annos'][i]
    carbs_per = df['HH g'][i]
    serving_number = ''
    serving_measurement = ''
    category_name = df.columns[0]  # Assuming the category name is in the first column

    if isinstance(serving_size, str):
        serving_split = serving_size.split(' ')
        serving_number = serving_split[0]
        serving_measurement = ' '.join(serving_split[1:]) if len(serving_split) > 1 else ''

    if isinstance(carbs_per, str) and carbs_per.startswith('n.'):
        carbs_per = carbs_per[2:]  # Remove the 'n.' prefix

    # Create the formatted string
    formatted_string = f"Food(\n" \
                       f"    name: '{food_name}',\n" \
                       f"    carbsPer: {carbs_per} ,\n" \
                       f"    defaultServingSize: {serving_number},\n" \
                       f"    servingSizeMeasurement: '{serving_measurement}',\n" \
                       f"    category: Category(\n" \
                       f"        name: 'Leivonnaiset',\n" \
                        f"       image: 'assets/images/baked.png')),\n" \
                       f")"

    # Add the formatted string to the list
    formatted_data.append(formatted_string)

# Print the formatted data
with open('.\outputs\outputkahvileivat.txt', 'w', encoding='utf-8') as file:
    file.writelines('\n'.join(formatted_data))