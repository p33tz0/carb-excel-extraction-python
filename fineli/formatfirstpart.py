import os

def extract_categories():
    # Get a list of all the text files in the directory
    text_files = [f for f in os.listdir() if f.endswith('.txt')]

    # Initialize an empty set to hold the categories
    categories = set()

    # Iterate over the text files
    for text_file in text_files:
        # Split the file name on the underscore and get the first part
        category = text_file.split('_')[0]
        # Add the category to the set (this automatically removes duplicates)
        categories.add(category)

    # Open the output file
    with open('categories.txt', 'w', encoding='utf-8') as f:
        # Iterate over the categories
        for category in categories:
            # Format the category and write it to the output file
            f.write(f"Category(name: '{category}', icon: Icons.local_drink, color: Colors.blue),\n")

# Call the function
extract_categories()
