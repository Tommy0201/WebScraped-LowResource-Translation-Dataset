

# with open('demo.txt','r',encoding='utf-8') as file:
#     lines = file.readlines()
# with open('demo_eng.txt','w',encoding='utf-8') as file:
#     for i in range(len(lines)):
#         if "Eng:" in lines[i]:
#             file.write(lines[i])
    

# DETECTING DIFFERENCES IN LENGTH
# with open('web_data_processing/processed_naijalingo.com.txt','r', encoding='utf-8') as file:
#     pid_lines = file.readlines()

# with open('translated_1_naijalingo_pidgin.txt','r',encoding='utf-8') as file:
#     eng_lines = file.readlines()

# for i, line in enumerate(pid_lines):
#     pid_words = line.lower().split()
#     if 'means' in pid_words:
#         eng_words = eng_lines[i].lower().split()
#         inter = [x for x in pid_words if x in eng_words]
#         if len(inter) <=3:
#             means_index = pid_words.index('means')
#             start = means_index+1
#             eng_lines.insert(i, ' '.join(pid_words[start:]) + '\n')

# with open('translated_2_naijalingo_pidgin.txt','w') as file:
#     for line in eng_lines:
#         file.write(line)

        
# for i in range(len(eng_lines)):
#     pid_words = pid_lines[i].split()
#     eng_words = eng_lines[i].split()
#     if abs(len(pid_words)-len(eng_words)) <=4:
#         with open('demo_naijalingo_2.txt','a') as file:
#             file.write(f'Pid: {pid_lines[i]}')
#             file.write(f'Eng: {eng_lines[i]}')



# MATCHING LINES
with open('web_data_processing/processed_naijalingo.com.txt','r', encoding='utf-8') as file:
    pid_lines = file.readlines()

with open('translated_2_naijalingo_pidgin.txt','r',encoding='utf-8') as file:
    eng_lines = file.readlines()

new_dict ={}
extra_dict={}
for pid_line in pid_lines:
    count = 0
    matched_line = ""
    pid_words = pid_line.split()
    for eng_line in eng_lines:
        eng_words = eng_line.split()
        inter = [x for x in pid_words if x in eng_words]
        if len(inter) > count:
            count = len(inter)
            matched_line = eng_line
    if count >= 4:
        new_dict[pid_line] = matched_line
        if matched_line in eng_lines:
            eng_lines.remove(matched_line) 
    else:
        extra_dict[pid_line] = matched_line
        if matched_line in eng_lines:
            eng_lines.remove(matched_line)

with open('demo_naijalingo_4.txt','w', encoding='utf-8') as file:
    for key in new_dict:
        file.write(f"Pid: {key}")
        file.write(f"Eng: {new_dict[key]}")
    file.write("---------------END OF MATCHED LINE ------------------")
    for keyy in extra_dict:
        file.write(f"Pid: {keyy}")
        file.write(f"Eng: {extra_dict[keyy]}")



