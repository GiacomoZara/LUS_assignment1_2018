import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

input_file = open(inputFile, 'r', encoding='utf8')
words_tags_dictionary = {}
for line in input_file:
	if len(line) < 2:
		continue
	line = line.replace("\n", "")
	line_split = line.split("\t")
	assert(len(line_split) == 2)
	word = line_split[0]
	tag = line_split[1]
	word_tag = "{0}\t{1}".format(word, tag)
	if word_tag not in words_tags_dictionary:
		words_tags_dictionary[word_tag] = 1
	else:
		words_tags_dictionary[word_tag] += 1	


output_file = open(outputFile, 'w', encoding='utf8')
for word_tag, word_tag_count in words_tags_dictionary.items():
	output_file.write("{0}\t{1}\n".format(word_tag, word_tag_count))