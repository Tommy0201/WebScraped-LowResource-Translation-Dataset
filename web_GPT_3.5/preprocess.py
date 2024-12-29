file_path = 'web_GPT_3.5/gpt_ted_talk_igbo.txt'
new_file_path = 'web_GPT_3.5/M_gpt_ted_talk_igbo.txt'


with open(file_path, 'r', encoding="utf-8") as f:
    lines = f.readlines()

# Open the new file for writing
with open(new_file_path, 'w', encoding="utf-8") as new_file:
    for line in lines:
        n_line = line.split()
        if "means:" in n_line:
            i = n_line.index("means:")
            out = n_line[0] + " ".join(n_line[i + 1:])
            new_file.write(out + "\n")
        elif "Translation:" in n_line:
            i = n_line.index("Translation:")
            out = n_line[0] + " ".join(n_line[i + 1:])
            new_file.write(out + "\n")
        elif "translation:" in n_line:
            i = n_line.index("translation:")
            out = n_line[0] + " ".join(n_line[i + 1:])
            new_file.write(out + "\n")
        elif "English:" in n_line:
            i = n_line.index("English:")
            out = n_line[0] + " ".join(n_line[i + 1:])
            new_file.write(out + "\n")
        elif "to:" in n_line:
            i = n_line.index("to:")
            out = n_line[0] + " ".join(n_line[i + 1:])
            new_file.write(out + "\n")
        elif "is:" in n_line:
            i = n_line.index("is:")
            out = n_line[0] + " ".join(n_line[i + 1:])
            new_file.write(out + "\n")
        else:
            new_file.write(line)

print("File saved successfully.")
