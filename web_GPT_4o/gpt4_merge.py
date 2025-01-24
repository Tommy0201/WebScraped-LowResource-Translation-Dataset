
import csv 

def merge():
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
    return
            
def csv_format():
    # Step 1: Reformat the file
    input_file = "Pidgin_gpt4_bbc.txt"
    output_file = "gpt4_bbc_pidgin.csv"

    # Initialize variables to hold Pidgin and English sentences
    pid_sentence = ""
    eng_sentence = ""

    with open(input_file, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    # Write to the output CSV file
    with open(output_file, 'w', encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Input_pid", "Output_eng"])  # Write the header

        # Process each line
        for line in lines:
            line = line.strip()  # Remove extra whitespace
            if line.startswith("Pid:"):
                pid_sentence = line[5:].strip()  # Extract Pidgin sentence
                # if pid_sentence.startswith("1. ") or pid_sentence.startswith("2. ") :
                #     pid_sentence = pid_sentence[3:]
                # if pid_sentence[0] == '"' and pid_sentence[-1] == '"':
                #     pid_sentence = pid_sentence[1:-1]

            elif line.startswith("Eng:"):
                eng_sentence = line[5:].strip()  # Extract English sentence
                # if eng_sentence[0] == '"' and eng_sentence[-1] == '"':
                #     eng_sentence = eng_sentence[1:-1]

                # Write the pair into the CSV
                csv_writer.writerow([pid_sentence, eng_sentence])


    # Step 2: Read the CSV and output the number of rows
    with open(output_file, 'r', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        row_count = sum(1 for row in csv_reader) - 1  # Subtract 1 for the header row

    print(f"The CSV file contains {row_count} rows.")

    
    return

if __name__ == "__main__":
    # merge()
    csv_format()