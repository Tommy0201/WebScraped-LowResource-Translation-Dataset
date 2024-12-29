#PREPROCESSING THE COLLECTED DATA
# web_data_processing/processed_1_igbo.von.gov.ng.txt
# 'web_data_processing/processed4_bbc_igbo.txt'

with open('web_data_processing/processed_bbc_pidgin.txt','r',encoding='utf-8') as file:
    lines = file.readlines()


new_liness = []
deleted_lines=[]
# for i in range(1,len(lines),2):
#     if len(lines[i].split()) <=2:
#         deleted_lines.append(lines[i-1])
#         deleted_lines.append(lines[i])
#     else: 
#         new_liness.append(lines[i-1])
#         new_liness.append(lines[i])

        
# def split_sentences(line):
#     sentences = line.strip().split(';')
#     sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
#     return sentences

# with open('demo6.txt','w',encoding='utf-8') as file:
#     for line in lines:
#         sentences = split_sentences(line)
#         for sentence in sentences:
#             file.write(sentence.strip() + '.\n')



# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False

# new_liness = []
# deleted_lines = []
for line in lines:
    words = line.split()
    if words:
        if "Posted" in words[0] and "at" in words[1]:
            deleted_lines.append(line)
        else:
            new_liness.append(line)



# # # Delete all empty lines
# #     new_lines = [line for line in lines if line.strip()]
# # Delete all lines with 1 character/word


# def split_lines(text):
#     result = []
#     for line in lines:
#             parts = line.split("2.")
#             result.append(parts[0].strip())
#             if len(parts) > 1:
#                 result.append("2. " + parts[1].strip())
#     return "\n".join(result)

# Test the function

# new_liness = [line for line in lines if not ";" in line.split()[-1]]
# # # # # #     # new_liness = [line for line in lines if len(line.split())<=4 and ")" not in line.split()[0]]
# deleted_lines = [line for line in lines if ";" in line.split()[-1]]
# new_liness = [line for line in lines if not line.split() or not "Informate" in line.split()]
# deleted_lines = [line for line in lines if line.split() and "Informate" in line.split()]


with open('processed_2_bbc_pidgin.txt','w',encoding='utf-8') as file:
    file.writelines(new_liness)
    file.write("__________DELETED LINES_______")
    file.writelines(deleted_lines)






# def delete_extra_spaces(line):
#     words = line.strip().split()
#     result = []
#     current_word = ''

#     for word in words:
#         if len(word) > 1:
#             if current_word:
#                 result.append(current_word)
#                 current_word = ''
#             result.append(word)
#         else:
#             if current_word:
#                 current_word += ' '
#             current_word += word

#     if current_word:
#         result.append(current_word)

#     return ' '.join(result)
# split_lines = []
# for line in lines:
#     cleaned_sentence = delete_extra_spaces(line)
#     split_lines.append(cleaned_sentence)


# with open('translated_1_bbc_pidgin.txt','r', encoding='utf-8') as file:
#     lines = file.readlines()
#     new_lines = []
#     for line in lines:
#         if len(line.split()) <= 3:
#             new_lines.append(line)
#     print(len(new_lines))
#     for line in new_lines:
#         print(line)



