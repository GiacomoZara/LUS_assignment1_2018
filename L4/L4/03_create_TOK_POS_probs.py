import sys
import math

posCountsFile = sys.argv[1]
tokPosCountsFile = sys.argv[2]
outputFile = sys.argv[3]

pos_counts_file = open(posCountsFile, 'r', encoding='utf8')
pos_counts_dictionary = {}
for line in pos_counts_file:
	if len(line) < 2:
		continue
	line = line.replace("\n", "")
	line_split = line.split("\t")
	assert(len(line_split) == 2)
	pos = line_split[0]
	count = line_split[1]
	pos_counts_dictionary[pos] = count

tok_pos_counts_file = open(tokPosCountsFile, 'r', encoding='utf8')
tok_pos_counts_dictionary = {}
for line in tok_pos_counts_file:
	if len(line) < 2:
		continue
	line = line.replace("\n", "")
	line_split = line.split("\t")
	assert(len(line_split) == 3)
	tok = line_split[0]
	pos = line_split[1]
	count = line_split[2]
	tokpos = "{0}\t{1}".format(tok,pos)
	tok_pos_counts_dictionary[tokpos] = count	

output_file = open(outputFile, 'w', encoding='utf8')
for tokpos, tokpos_count in tok_pos_counts_dictionary.items():
	tokpos_split = tokpos.split("\t")
	assert(len(tokpos_split) == 2)
	tok = tokpos_split[0]
	pos = tokpos_split[1]
	probab = -math.log(float(tokpos_count) / float(pos_counts_dictionary[pos]))
	output_file.write("{0}\t{1}\t{2}\n".format(tok, pos, probab))