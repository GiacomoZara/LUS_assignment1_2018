import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

input_file = open(inputFile, 'r', encoding='utf8')
sentences_list = []
sentence = ""
for line in input_file:
	if len(line) < 2:
		sentences_list.append(sentence[:-1])
		sentence = ""
		continue
	line = line.replace("\n", "")
	line_split = line.split("\t")
	assert(len(line_split) == 2)
	tag = line_split[1]
	sentence += tag + " "

output_file = open(outputFile, 'w', encoding='utf8')
for sentence in sentences_list:
	output_file.write("{0}\n".format(sentence))