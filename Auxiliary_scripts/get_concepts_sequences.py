import os
import sys

# removing files
os.system("[ -e lus_project1 ] && rm concepts_sequences.txt")

# training file
train_filename = str(sys.argv[1])

# writing sequences
training_file = open(train_filename)
output_file = open('concepts_sequences.txt', 'w')

for line in training_file:
	if len(line.split()) > 0:
		concept = line.split()[1]
		output_file.write(str(concept) + " ")
	else:
		output_file.write("\n")

output_file.close()
training_file.close()
