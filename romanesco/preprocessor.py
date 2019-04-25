import re
with open('iliad.txt') as iliad, open('iliad_lines.txt', 'w', encoding='utf-8') as iliad_lines:
	punctuation = ['.','!','?',':',';']
	for line in iliad:
		for char in line:
			if char in punctuation:
				iliad_lines.write(char+'\n')
			if char != '\n':
				iliad_lines.write(char)