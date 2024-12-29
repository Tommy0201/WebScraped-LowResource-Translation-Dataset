



if __name__ == "__main__":
    with open("web_scraping/scrape_bbc_igbo.txt", 'r') as f:
        bbc_igbo = f.readlines()
        
    with open("web_scraping/scrape_igbo.von.gov.ng.txt",'r') as g:
        igbo_gov = g.readlines()
    with open("web_scraping/scrape_ted_talk_igbo.txt",'r') as h:
        ted_talk = h.readlines()
    print("Og lenth bbc Igbo: ", len(bbc_igbo))
    print("Og lenth igbo gov: ", len(igbo_gov))
    print("Og lenth ted talk: ", len(ted_talk))
    print("Total Igbo: ", len(bbc_igbo)+len(igbo_gov)+len(ted_talk))
    
    igbo = 0
    sent_num = 0
    lst = [bbc_igbo, igbo_gov, ted_talk]
    for file in lst:
        sent_num+= len(file)
        for line in file:
            words = line.split()
            igbo += len(words)
    
    print("IGBO WORDS: ",igbo)
    print("AVG Igbo words: ",igbo/sent_num)
    
    # bbc_igbo_new = []
    # redunt = []
    # for line in bbc_igbo:
    #     if len(line.strip())>1:
    #         bbc_igbo_new.append(line)
    #     else:
    #         redunt.append(line)
    # print(redunt)
        
    # bbc_igbo_new = [x.strip() for x in bbc_igbo]
    
    with open("web_scraping/scrape_bbc_pidgin.txt", 'r') as f:
        bbc_pid = f.readlines()
        
    with open("web_scraping/scrape_naijalingo.com.txt",'r') as g:
        naija = g.readlines()

    print("Og lenth bbc pidgin: ", len(bbc_pid))
    print("Og lenth naijalingo: ", len(naija))
    print("Total: ", len(bbc_pid)+len(naija))
    
    
    pid = 0
    sent_pid = 0
    lst = [bbc_pid, naija]
    for file in lst:
        sent_pid+= len(file)
        for line in file:
            words = line.split()
            pid += len(words)
    
    print("PID WORDS: ",pid)
    print("AVG Pid words: ",pid/sent_pid)
    
    print("total avg words/sent: ", (pid+igbo)/(sent_pid+sent_num))
        
    