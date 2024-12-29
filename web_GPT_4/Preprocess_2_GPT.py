import re

string1 = "How far naw? E don tey wey i see you o! Means: What's up? It's been a while!"
string2 = "Oh boy, I wan go kaka. meaning: I want to poop." 

# Define the regular expression pattern to match different variations of "means"
pattern = r"(?i)\b(Mean[s]?|Meaning[:]?|means[:]?|meaning[s]?:)\b"

# Split the string using the regular expression pattern as the separator
lines = re.split(pattern, string1)

# Remove any empty strings resulting from the split and trim leading/trailing whitespace
lines = [line.strip() for line in lines if line.strip()]

print("line1:", lines[0])
print("line2:", lines[1])



