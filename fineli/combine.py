import glob

# Find all output text files in the current directory
file_list = glob.glob('.\outputs\output*.txt')

# Sort the file list (optional)
file_list.sort()

# Combine the contents of all files into a single string
combined_content = ''
for file_path in file_list:
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        combined_content += file_content + '\n'

# Write the combined content to a new file
with open('.\outputs\combined_output.txt', 'w', encoding='utf-8') as file:
    file.write(combined_content)
