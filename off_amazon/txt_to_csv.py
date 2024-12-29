import csv

def converter(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        re_lines = []
        for line in lines:
            words = line.strip().split()
            if len(words) > 1:
                line = ' '.join(words[1:])
            # while line.startswith('"') and line.endswith('"'):
            #     line = line[1:-1]
            re_lines.append(line)
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['pid_sent'])  # Write the header
        for line in re_lines:
            writer.writerow([line])

# Specify the input and output file paths
input_file = 'off_amazon/pidgin_hitt.txt'
output_file = 'off_amazon/pidgin_hitt1.csv'

# Convert the txt to csv
converter(input_file, output_file)