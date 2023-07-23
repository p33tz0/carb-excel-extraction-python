import os

def format_data(input_file):
    # Check if the file is empty
    if os.stat(input_file).st_size == 0:
        return

    # Open the file and read the lines
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Initialize an empty list to hold the food items
    foods = []

    # Extract the category and subcategory from the input file name
    base_name = os.path.basename(input_file)
    category, subcategory = os.path.splitext(base_name)[0].split('_')

    # Iterate over the lines in the file
    for i in range(0, len(lines), 3):
        # Get the food name and carbs per 100g
        name = lines[i].strip()
        carbs_per_100 = float(lines[i+2].strip().split(' ')[0])  # Assumes the format is always "xx g"

        # Only include items with 1g or more of carbs per 100g
        if carbs_per_100 >= 1:
            # Format the data
            food = f"""
            foodBox.add(Food('{name}', {carbs_per_100}, '{category}', '{subcategory}'));
            """

            # Add the food to the list
            foods.append(food)

    # Join the foods into a single string
    output = '\n'.join(foods)

    # Generate the output file name
    output_file = category + '_' + subcategory + '-output.txt'

    # Write the output to a text file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

# Get a list of all the text files in the directory
text_files = [f for f in os.listdir() if f.endswith('.txt') and not f.endswith('-output.txt')]

# Call the function with each text file
for text_file in text_files:
    print(text_file)
    format_data(text_file)
  
#format_data('Vilja ja leivontatuotteet_Leivonnainen suola.txt')
