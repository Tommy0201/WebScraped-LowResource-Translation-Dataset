import openai
import time
import requests
import concurrent.futures
import os
from openai import OpenAI
from datasets import load_dataset

openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

def trans_text(sent):
    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a professional translator in Nigeria languages. You need to translate Igbo and Nigerian Pidgin sentences to English"},
                {"role": "user", "content": f'Translate this sentence to English: {sent}, only includes the translated sentence in the answer'},
            ],
            max_tokens=100,
            temperature=0,
            n=1,
            stop=None,
        )
        translation = response.choices[0].message.content.strip().split('\n')
        return sent, translation
    # except openai.error.ServiceUnavailableError as e:
    #     time.sleep(5)
    #     return trans_text(sent)
    # except openai.error.Timeout as e:
    #     time.sleep(5)
    #     return trans_text(sent)
    # except openai.error.APIError as e:
    #     if "Request failed due to server shutdown" in str(e):
    #         time.sleep(5)
    #         return trans_text(sent)
    #     else:
    #         time.sleep(5)
    #         return trans_text(sent)
    except requests.exceptions.ConnectionError as ce:
        print(f"Connection Error: {ce}")
        time.sleep(5)
        return trans_text(sent)
def translate_batch(sentences):
    translated_text = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(trans_text, sent) for sent in sentences[98000:106693]]
        count = 0
        for future in concurrent.futures.as_completed(futures):
            sentence, translation = future.result()
            if translation:
                translated_text.append((sentence, translation))
                count+=1
                if count%100 == 0:
                    time.sleep(6)
    return translated_text

# # EDIT THIS FILE BEFORE RUNNING CODE
# source_file = 'web_data_processing/processed_bbc_igbo.txt'
# translated_file = 'gpt4_bbc_igbo.txt'

# with open(source_file,'r', encoding='utf-8') as f:
#     igbo_text = f.read()
# sentences = igbo_text.split('\n')
# translated_text = translate_batch(sentences)

# # DO NOT MAKE MISTAKE BETWEEN 'W' AND 'A' 
# mode = "w"
# if os.path.isfile(translated_file):
#     mode = "a"
# with open(translated_file, mode, encoding='utf-8') as file:
#     for original, translation in translated_text:
#         file.write(f"Igbo: {original}\n")
#         file.write(f"Eng: {' '.join(translation)}\n")

if __name__ =="__main__":
    dataset = load_dataset("Tommy0201/Igbo_To_Eng_Amazon_Translator", split='test')  # Adjust the split as necessary
    sentences = dataset['igbo_input']
    # Translate sentences using GPT-4
    translated_text = translate_batch(sentences)
    
    # Output paths
    out_path = "val_gpt.en"
    # DO NOT MAKE MISTAKE BETWEEN 'W' AND 'A' 
    mode = "w"
    if os.path.isfile(translated_file):
        mode = "a"
    with open(translated_file, mode, encoding='utf-8') as file:
        for original, translation in translated_text:
            file.write(f"Igbo: {original}\n")
            file.write(f"Eng: {' '.join(translation)}\n")



# THE % OF THE DATASET for GPT 4.0 preview 1106
# igbo.gov:  5008 (100%) out of 5008
# ted_talk_igbo: 175 (100%) out of 175
# bbc_igbo:  106,693 (100%) out of 106,693
# total igbo: 111,876

# naijalingo:  2041 (100%) out of 2,041
# bbc_pidgin: 119,225 (100%) out of 119,225

#total pidgin: 121,266


# THE % OF THE DATASET for GPT 3.5
# igbo.gov:  5008(%) out of 5008
# ted_talk_igbo: 175 (100%) out of 175
# bbc_igbo: 104523 (98%) out of 106,693


# naijalingo: 2041 (100%) out of 2,041
# bbc_pidgin: 114289 (96%) out of 119,225


