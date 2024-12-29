import csv
import pandas as pd
import random
# with open('web_chatGPT/official_ted_talk.txt','r',encoding="utf-8") as f:
#     lines = f.readlines()

# igbo_lines = lines[::2]


# with open('amazon_mechanical_turk/assigned_ted_talk.csv','w',encoding='utf-8',newline='') as g:
#     writer = csv.writer(g)
#     for line in igbo_lines:
#         add = line[6:].strip()
#         print(add)
#         writer.writerow([add])


# df1 = pd.read_csv('amazon_mechanical_turk/assigned_bbc_igbo.csv')
# df2 = pd.read_csv('amazon_mechanical_turk/assigned_igbo_gov.csv')
# df3 = pd.read_csv('amazon_mechanical_turk/assigned_ted_talk.csv')
# df = pd.concat([df1,df2,df3],axis=0,ignore_index=True)

# df.to_csv('amazon_mechanical_turk/assigned_igbo.csv',index=False)


#Function to read and randomly selected lines
def read_select(file_path, num_sentences):
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        lines = [line for line in lines if line.startswith("Pid:")]
        filtered_lines = [line for line in lines if (len(line.split()) > 10 and "video" not in line.lower() and "duration" not in line.lower())] #only lines with more than 5 words
        rand_indices = random.sample(range(len(filtered_lines)), num_sentences)
        selected_lines = [filtered_lines[i] for i in rand_indices]
    return selected_lines

# #Number of allocated sentences for each Igbo sources
# num_sentences_bbc_igbo = 42
# num_sentences_igbo_gov = 6
# num_sentences_ted_talk = 2
# igbo_lines = []
# igbo_lines.extend(read_select("web_chatGPT/official_bbc_igbo.txt", num_sentences_bbc_igbo))
# igbo_lines.extend(read_select("web_chatGPT/official_igbo_gov.txt", num_sentences_igbo_gov))
# igbo_lines.extend(read_select("web_chatGPT/official_ted_talk.txt", num_sentences_ted_talk))

# # Save randomly selected Igbo lines to a text file
# with open('amazon_mechanical_turk/igbo_hitt_test2.txt', 'w', encoding='utf-8') as g:
#     for line in igbo_lines:
#         g.write(line.strip()+'\n')

#Number of allocated sentences for each Pidgin sources
# num_sentences_bbc_igbo = 23842
# num_sentences_igbo_gov= 1119
# num_sentences_ted_talk = 39
# igbo_lines = []
# igbo_lines.extend(read_select("gpt4_bbc_igbo.txt", num_sentences_bbc_igbo))
# igbo_lines.extend(read_select("gpt4_igbo.gov.txt", num_sentences_igbo_gov))
# igbo_lines.extend(read_select("gpt4_ted_talk_igbo.txt", num_sentences_ted_talk))

# with open('off_amazon/igbo_hitt1.txt', 'w', encoding='utf-8') as h:
#     for line in igbo_lines:
#         h.write(line.strip()+'\n')

num_sentences_bbc_pid = 24579
num_sentences_naijalingo= 421
pid_lines = []
pid_lines.extend(read_select("gpt4_bbc_pidgin.txt", num_sentences_bbc_pid))
pid_lines.extend(read_select("gpt4_naijalingo.txt", num_sentences_naijalingo))

with open('off_amazon/pidgin_hitt1.txt', 'w', encoding='utf-8') as g:
    for line in pid_lines:
        g.write(line.strip()+'\n')
        
        
#bbc_pidgin: 119,225
#naijalingo: 2041
# total: 121,266


#bbc_igbo: 106,693
#igbo_gov: 5008
#ted_talk: 175

# total: 111,876

#Thus number of allocated sentences of Pidgin: 24579 / 421
#Thus number of allocated sentences of Igbo: 23842 / 1119 / 39