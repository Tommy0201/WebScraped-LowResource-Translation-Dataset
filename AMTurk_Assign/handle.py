import csv

with open('amazon_mechanical_turk/pidgin-igbo_hitt_test.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

new_lines_igbo = []
new_lines_pid = []

for line in lines: 
    if "Pid:" in line:
        n_line = line.split()
        start = n_line.index("Pid:") + 1
        new_lines_pid.append(' '.join(n_line[start:]))
    elif "Igbo:" in line:
        n_line = line.split()
        start = n_line.index("Igbo:") + 1
        new_lines_igbo.append(' '.join(n_line[start:]))

with open('amazon_mechanical_turk/pidgin-off.csv', 'w', newline='', encoding='utf-8') as h:
    writer = csv.writer(h)
    writer.writerow(["Pidgin"])
    writer.writerows([[line] for line in new_lines_pid])

with open('amazon_mechanical_turk/igbo-off.csv', 'w', newline='', encoding='utf-8') as h:
    writer = csv.writer(h)
    writer.writerow(["Igbo"])
    writer.writerows([[line] for line in new_lines_igbo])
