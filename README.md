# nouns-finder
This is a little python script that uses NLTK to find Nouns. Used for preprocessing a requirements document.

# Usage
Input a text file. It is set to translate a portuguese text to english text using Goslate. If it does not work properly, a error message will warn will and ask to a english input. If success, a colored terminal output will highligh all the found nouns, alogside its context.

Simple example:
$ python3 script.py < text.in

# Changing the context radius:
You can specify a extra command-line argument, telling the radius of the context will want alogside the nouns. If the radius is R, then the noun will be printed between R word-tokens to its left plus R word-tokens to its right. The R value is 8 by default, which means if you specify a invalid radius (R < 0) or no radius at all, then 8 word-tokens will be printed for each side of all the found nouns in the input text.

Simple example:
$ python3 script.py 3 < text.in
Simple output:
(...) this is a DOG eating a colorful (...)

# For non-english input
Note: the package NLTK work properly only with english text. If Goslate does not cooperate with the input translation, you will need to input the text in english directly.