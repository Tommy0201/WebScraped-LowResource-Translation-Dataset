def find_tokens(sent):
    sents = sent.split()
    return (len(sents)-1)
eng_tokens = 0
igbo_tokens = 0
pid_tokens = 0 

with open("web_GPT_4/official_bbc_igbo.txt","r",encoding='utf-8') as f:
    lines = f.readlines()
igbo_lines = lines[::2]
eng_lines = lines[1::2]
for igbo in igbo_lines:
    igbo_tokens += find_tokens(igbo)
for eng in eng_lines:
    eng_tokens += find_tokens(eng)

with open("web_GPT_4/official_igbo_gov.txt","r",encoding='utf-8') as g:
    lines1 = g.readlines()
igbo_lines1 = lines1[::2]
eng_lines1 = lines1[1::2]
print(f"Igbo_Tokens: {igbo_tokens}")
print(f"Pid_Tokens: {pid_tokens}")
print(f"Eng_Tokens: {eng_tokens}")
print(igbo_lines1[0])
print(eng_lines1[-1])
print("""


""")
for igbo in igbo_lines1:
    igbo_tokens += find_tokens(igbo)
for eng in eng_lines1:
    eng_tokens += find_tokens(eng)


with open("web_GPT_4/official_ted_talk.txt","r",encoding='utf-8') as g:
    lines2 = g.readlines()
igbo_lines2 = lines2[::2]
eng_lines2 = lines2[1::2]
for igbo in igbo_lines2:
    igbo_tokens += find_tokens(igbo)
for eng in eng_lines2:
    eng_tokens += find_tokens(eng)
print(f"Igbo_Tokens: {igbo_tokens}")
print(f"Pid_Tokens: {pid_tokens}")
print(f"Eng_Tokens: {eng_tokens}")
print(igbo_lines2[0])
print(eng_lines2[-1])
print("""


""")

with open("web_GPT_4/official_bbc_pidgin.txt","r",encoding='utf-8') as g:
    lines3 = g.readlines()
igbo_lines3 = lines3[::2]
eng_lines3 = lines3[1::2]
for igbo in igbo_lines3:
    pid_tokens += find_tokens(igbo)
for eng in eng_lines3:
    eng_tokens += find_tokens(eng)
print(f"Igbo_Tokens: {igbo_tokens}")
print(f"Pid_Tokens: {pid_tokens}")
print(f"Eng_Tokens: {eng_tokens}")
print(igbo_lines3[0])
print(eng_lines3[-1])
print("""


""")

with open("web_GPT_4/official_naijalingo.txt","r",encoding='utf-8') as g:
    lines4 = g.readlines()
igbo_lines4 = lines4[::2]
eng_lines4 = lines4[1::2]
for igbo in igbo_lines4:
    pid_tokens += find_tokens(igbo)
for eng in eng_lines4:
    eng_tokens += find_tokens(eng)
print(f"Igbo_Tokens: {igbo_tokens}")
print(f"Pid_Tokens: {pid_tokens}")
print(f"Eng_Tokens: {eng_tokens}")    
print(igbo_lines4[0])
print(eng_lines4[-1])
print("""


""")
# input = (igbo_tokens+pid_tokens) *  0.0005 / 1000
# output = eng_tokens * 0.0015 / 1000
# print(f"Cost for input:{input}")
# print(f"Cost for output:{output}")
# print(f"Total cost {input+output}")

# print("Assuming:")
# input = (igbo_tokens+pid_tokens) *  0.06 / 1000
# output = eng_tokens * 0.06 / 1000
# print(f"Cost for input:{input}")
# print(f"Cost for output:{output}")
# print(f"Total cost {input+output}")
