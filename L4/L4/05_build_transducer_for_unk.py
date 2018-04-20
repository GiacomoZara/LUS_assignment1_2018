import sys
import math

tokPosProbsFile = sys.argv[1]
outputFile = sys.argv[2]

unk_prob = -math.log(1/38)

tok_pos_probs_file = open(tokPosProbsFile, 'r', encoding='utf8')
unk_pos_probs_dictionary = {}
for line in tok_pos_probs_file:
	assert(len(line) > 0)
	line = line.replace("\n", "")
	line_split = line.split("\t")
	assert(len(line_split) == 3)
	pos = line_split[1]
	unkpos = "{0}\t{1}".format("<unk>", pos) 
	unk_pos_probs_dictionary[unkpos] = unk_prob

output_file = open(outputFile, 'w', encoding='utf8')
for unkpos, unkpos_prob in unk_pos_probs_dictionary.items():
	unkpos = unkpos.split("\t")
	assert(len(unkpos) == 2)
	unk = unkpos[0]
	pos = unkpos[1]
	output_file.write("{0}\t{1}\t{2}\n".format(unk, pos, unkpos_prob))	