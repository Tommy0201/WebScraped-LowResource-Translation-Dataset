import os


# Code to delete lines with x number of length
# for idx, line in enumerate(lines):
#     if len(line) !=1:
#         new_input += (line + "\n")

# print(new_input)


# with open('web_scraping/bbc_igbo.txt', 'r',encoding='utf-8') as file:
#     input = file.read()
# lines = input.splitlines()


#Code to delete 
# start,end = 0,0
# for idx,line in enumerate(lines):
#     words = line.split()
#     if len(words)>0:
#         if start == 0:
#             if "require.config({" in words or "function" in words or "$(function" in words:
#                     start = idx
#         if start != 0 and "});" in words:
#             end = idx 
#         if start != 0 and end != 0:
#             for i in range(start,end+1):
#                 lines[i] =''
#             start = 0
#             end = 0
# with open('web_data_processing/demo-processing.txt', 'w') as file:
#     for line in lines:
#         file.write(line + "\n")





# file_name = "processed4_bbc_igbo.txt"

# directory = os.path.dirname(os.path.abspath(__file__))
# os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
# if os.path.exists(file_name):
#     mode = "a"
# else:
#     mode = "w"
# with open(file_name, "w", encoding="utf-8") as file:
#         for line in lines:
#             file.write(line + "\n")



# Eliminate coding lines that still exist through identifing those contain "{", "function", ...etc in a sentence
# with open("processed3_bbc_igbo.txt", 'r',encoding='utf-8') as file:
#     input = file.read()
# lines = input.splitlines()

# for idx,line in enumerate(lines):
#     # sentences = line.split(". ")
#     sentences = line.split()
#     for word in sentences:
#         if "}" in word or "{" in word:
#     # if len(sentences) <=2:
#          lines[idx]=''
# with open(file_name, "w", encoding="utf-8") as file:
#     for line in lines:
#         if len(line)>0:
#             file.write(line+ "\n")


# CONVERT TO SET
# set_lines = set()
# for line in lines:
#     set_lines.add(line)

# with open("processed3_bbc_igbo.txt","w",encoding="utf-8") as file:
#     for line in set_lines:
#         file.write(line+"\n")

total_words = 0

#COUNT THE AVERAGE NUMBER OF WORDS PER TRANSLATED SENTENCE
with open("web_chatGPT/official_bbc_pidgin.txt","r", encoding="utf-8") as file:
    input = file.read()
lines = input.splitlines()
for i in range(0,len(lines),2):
# for i in range(1,len(lines),2):
    words = lines[i].split()
    total_words += len(words)


with open("web_chatGPT/official_naijalingo.txt","r", encoding="utf-8") as file:
    input2 = file.read()
lines2 = input2.splitlines()
for i in range(0,len(lines2),2):
    words = lines2[i].split()
    total_words += len(words)

print(total_words/(len(lines)+len(lines2))*2)



