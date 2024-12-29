from datasets import Dataset
from huggingface_hub import Repository

with open('M_igbo.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

igbo_sentences = []
eng_sentences = []

for i in range(0, len(lines), 2):
    igbo_sentence = lines[i].strip().replace("Igbo:", "")
    eng_sentence = lines[i + 1].strip().replace("Eng:", "")
    igbo_sentences.append(igbo_sentence)
    eng_sentences.append(eng_sentence)

training_igbo = []
training_eng = []
testing_igbo = []
testing_eng = []
for i in range(len(igbo_sentences)):
    if i % 99 == 0:
        testing_igbo.append(igbo_sentences[i])
        testing_eng.append(eng_sentences[i])
    else:
        training_igbo.append(igbo_sentences[i])
        training_eng.append(eng_sentences[i])

train_dataset = Dataset.from_dict({"igbo": training_igbo, "english": training_eng})
test_dataset = Dataset.from_dict({"igbo": testing_igbo, "english": testing_eng})


# Display the first few samples of the dataset
train_dataset.push_to_hub("igbo_to_english_split",split="train")
test_dataset.push_to_hub("igbo_to_english_split",split="test")
