import os

# removing files
os.system("[ -e lus_project1 ] && rm transducer_global.txt transducer_unk.txt")

# generating global transducer
input_file_probs = open('probabilities_wc.txt', 'r')
output_file_global = open('transducer_global.txt','w')

for line in input_file_probs:
	line = line.replace("\n", "")
	line_list = line.split('\t')
	output_file_global.write('0' + '\t' + '0' + '\t' + str(line_list[0]) + '\t' + str(line_list[1]) + '\t' + str(line_list[2]) + '\n')

input_file_probs.close()

# collecting number of concepts
input_file_concepts = open('distinct_concepts.txt', 'r')

nr_of_concepts = 0

for line in input_file_concepts:
	line = line.replace("\n", "")
	nr_of_concepts += 1

input_file_concepts.close()

# handling unknown words
input_file_concepts = open('distinct_concepts.txt', 'r')
unk_probability = 1 / float(nr_of_concepts)
for concept in input_file_concepts:
	output_file_global.write('0' + '\t' + '0' + '\t' + '<unk>' + '\t' + str(concept.rstrip()) + '\t' + str(unk_probability) + '\n')

output_file_global.write('0')
output_file_global.close()
input_file_concepts.close()








