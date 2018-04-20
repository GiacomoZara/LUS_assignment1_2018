import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

input_file = open(inputFile, 'r', encoding='utf8')
tags_dictionary = {}
for line in input_file:
	if len(line) < 2:
		continue
	line = line.replace("\n", "")
	line_split = line.split("\t")
	assert(len(line_split) == 2)
	tag = line_split[1]
	if tag not in tags_dictionary:
		tags_dictionary[tag] = 1
	else:
		tags_dictionary[tag] += 1	


output_file = open(outputFile, 'w', encoding='utf8')
for tag, tag_count in tags_dictionary.items():
	output_file.write("{0}\t{1}\n".format(tag, tag_count))