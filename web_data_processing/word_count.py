import csv

def open_and_count_word(file_name):
    with open(file_name, 'r') as f:
        sentences =f.readlines()
    print(file_name)    
    n = len(sentences)
    count_token = 0
    for sent in sentences:
        sent_token = sent.split()
        count_token += len(sent_token)
    word_per = count_token/n
    print("# word per sentence: ",round(word_per,2))
    print("total sent: ",n)
    return (count_token,n)

def processing_file(files):
    sent_pid = 0
    words_pid = 0
    for file in files:
        print("_____________")
        print("PREPROCESSED")
        val1, val2 = open_and_count_word(file)
        sent_pid += val2
        words_pid += val1
    out_pid = round(words_pid/sent_pid,2)
    print("TOTAL WORDS PER SENT BY SOURCE: ",out_pid)
    return (words_pid, sent_pid)
    
def reformat_file_single():
    # Step 1: Reformat the file
    input_file = "Pidgin_bbc.txt"
    output_file = "scraped_bbc_pidgin.csv"

    with open(input_file, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    # Write to the output CSV file
    with open(output_file, 'w', encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Pid_Sent"])  # Write the header

        # Write each line from the text file as a new row in the CSV
        for line in lines:
            
            add = line.strip()
            if line[0] == '"' and line[-1] == '"':
                print(add)
                line = line[1:-1] 
                print(line)
            csv_writer.writerow([add])  # Strip removes extra whitespace

    print(f"File '{output_file}' has been created successfully!")

    # Step 2: Read the CSV and output the number of rows
    with open(output_file, 'r', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        row_count = sum(1 for row in csv_reader) - 1  # Subtract 1 for the header row

    print(f"The CSV file contains {row_count} rows.")

    
def reformat_file_double():
    # Step 1: Reformat the file
    input_file = "gpt_naijalingo.txt"
    output_file = "gpt3.5_naijalingo.csv"

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
            elif line.startswith("Eng:"):
                eng_sentence = line[5:].strip()  # Extract English sentence
                # Write the pair into the CSV
                csv_writer.writerow([pid_sentence, eng_sentence])


    # Step 2: Read the CSV and output the number of rows
    with open(output_file, 'r', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        row_count = sum(1 for row in csv_reader) - 1  # Subtract 1 for the header row

    print(f"The CSV file contains {row_count} rows.")

if __name__ == "__main__":
    # file_igbo= ["web_data_processing/processed_bbc_igbo.txt","web_data_processing/processed_igbo.gov.txt","web_data_processing/processed_ted_talk_igbo.txt"]
    # file_pidgin = ["web_data_processing/processed_bbc_pidgin.txt", "web_data_processing/processed_naijalingo.txt"]
    # words_pid, sent_pid = processing_file(file_pidgin)
    # words_igbo, sent_igbo = processing_file(file_igbo)
    
    # print("TOTAL WORDS PER SENT BOTH SOURCE: ", (words_pid+words_igbo)/(sent_pid+sent_igbo))
    reformat_file_single()