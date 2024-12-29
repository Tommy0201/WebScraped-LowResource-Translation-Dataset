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
    


if __name__ == "__main__":
    file_igbo= ["web_data_processing/processed_bbc_igbo.txt","web_data_processing/processed_igbo.gov.txt","web_data_processing/processed_ted_talk_igbo.txt"]
    file_pidgin = ["web_data_processing/processed_bbc_pidgin.txt", "web_data_processing/processed_naijalingo.txt"]
    words_pid, sent_pid = processing_file(file_pidgin)
    words_igbo, sent_igbo = processing_file(file_igbo)
    
    print("TOTAL WORDS PER SENT BOTH SOURCE: ", (words_pid+words_igbo)/(sent_pid+sent_igbo))