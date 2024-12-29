import difflib

def compare_text_files(file1, file2):
    # Read the contents of the first file
    with open(file1, 'r',encoding='utf-8') as f1:
        file1_lines = f1.readlines()
    
    # Read the contents of the second file
    with open(file2, 'r',encoding='utf-8') as f2:
        file2_lines = f2.readlines()

    # Compute the differences between the two files
    differ = difflib.Differ()
    diff = list(differ.compare(file1_lines, file2_lines))

    # Print the differences
    print("Differences between", file1, "and", file2, ":")
    for line in diff:
        print(line.strip())

# Usage example
file1 = 'web_GPT_3.5\gpt_bbc_igbo.txt'
file2 = 'web_GPT_3.5\gpt_bbc_igbo-DESKTOP-BGRSKHA.txt'
compare_text_files(file1, file2)
