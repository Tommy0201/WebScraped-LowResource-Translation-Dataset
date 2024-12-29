with open("gpt4_bbc_igbo.txt",'r',encoding='utf-8') as f:
    bbc_ig_lines = f.readlines()
    
with open("gpt4_ted_talk_igbo.txt",'r',encoding='utf-8') as g:
    ted_ig_lines = g.readlines()
    
with open("gpt4_igbo.gov.txt",'r',encoding='utf-8') as h:
    gov_ig_lines = h.readlines()
    
merge = [] 
merge = bbc_ig_lines + ted_ig_lines + gov_ig_lines
merge_ig = []
merge_eng = []
for i in range(0,len(merge),2):
    ig_sent = merge[i].strip().replace("Igbo:","")
    eng_sent = merge[i+1].strip().replace("Eng:","")
    merge_ig.append(ig_sent)
    merge_eng.append(eng_sent)
    
    
with open("gpt4_merge_igbo.txt",'w',encoding='utf-8') as file:
    for line in merge_ig:
        file.write(line+"\n")
        
    
with open("gpt4_merge_eng.txt",'w',encoding='utf-8') as gile:
    for line in merge_eng:
        gile.write(line+"\n")