import sys
# IMPORT: Perceptron
import nltk
# IMPORT: Google Translator
import goslate
# IMPORT: Colored terminal print
from termcolor import colored

# Start of the script
# Get the input text
textIn = input()

# Create a Goslate (Google Translator related object) instance
gs = goslate.Goslate()

# Translate the input Portuguese text into a english text
try:
    textEng = gs.translate(textIn, 'en', 'pt')
except:
    print (colored('Google API Goslate is not responding. I\'ll use your input text.','red'))
    print (colored('Please give me your text already in english.\n', 'red'))
    textEng = textIn
# Create the translated text tokens (the Nltk Perceptron uses it)
tokens = nltk.word_tokenize(textEng)

# Produce the perceptron results
result = nltk.pos_tag(tokens)

# Filter the Nouns in the result
nouns = [i[0] for i in result if i[1] == 'NN']

# Remove the repeated nouns and sort it alphabetically
nouns = sorted(list(set(nouns)))

# Create a empty matrix. Each line of the matrix will be
# a list that keeps the indexes of the occurrences of each noun.
# This is needed to print the noun with it context.
indexes = [[] for i in range(len(nouns))]

# Fill the indexes matrix, finding each occurrence of each identified noun.
for i in range(len(nouns)):
    for j in range(len(tokens)):
        if nouns[i] == tokens[j]:
            indexes[i].append(j)

# Print the Nouns (with color) slongside its context
contextRange = int(sys.argv[1]) if (len(sys.argv) >= 1 and int(sys.argv[1]) >= 0) else 8

for i in indexes:
    for j in i:
        print ('>\t', ' '.join(tokens[((j - contextRange) if j >= contextRange else 0):j]), end = ' ')
        print (colored(tokens[j], 'yellow'), end = ' ')
        if j + 1 < len(tokens):
            aux = 1 + j + contextRange
            print (' '.join(tokens[(j + 1):(aux if aux < len(tokens) else len(tokens))]))
# End of the script.
