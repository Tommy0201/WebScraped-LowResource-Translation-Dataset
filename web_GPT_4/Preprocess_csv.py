import csv
with open('web_chatGPT/official_ted_talk.txt','r',encoding="UTF-8") as file:
    lines = file.readlines()

igbo_lines = lines[::2]
eng_lines = lines[1::2]

data = list(zip(igbo_lines,eng_lines))

with open('demo_ted_talk.csv','w',newline='',encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Igbo','Engl'])
    writer.writerows(data)