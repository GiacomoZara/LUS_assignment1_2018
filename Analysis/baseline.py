import random
import os

os.system("[ -e lus_project1 ] && rm baseline_random.txt baseline_majority.txt baseline_chance.txt")

training_file = open('LUS.P1/data/P1_data/data/NLSPARQL.train.data', 'r')

test_file = open('LUS.P1/data/P1_data/data/NLSPARQL.test.data', 'r')
output_file_random = open('baseline_random.txt', 'w')

concepts = []

for line_tr in training_file:
	split_line = line_tr.split()
	if len(split_line) > 0:
		concept = split_line[1]
		if concept not in concepts:
			concepts.append(concept)

training_file.close()

training_file = open('LUS.P1/data/P1_data/data/NLSPARQL.train.data', 'r')

concepts_repeated = []

for line_tr in training_file:
	split_line = line_tr.split()
	if len(split_line) > 0:
		concept = split_line[1]
		concepts_repeated.append(concept)

training_file.close()

for line_te in test_file:
	line_te = line_te.replace("\n", "")
	if(len(line_te.split()) > 0):
		output_file_random.write(str(line_te.split()[0]))
		output_file_random.write(" " + str(line_te.split()[1]))
		output_file_random.write(" " + str(random.choice(concepts)) + "\n")
	else:
		output_file_random.write("\n")

test_file.close()
output_file_random.close()

test_file = open('LUS.P1/data/P1_data/data/NLSPARQL.test.data', 'r')
output_file_majority = open('baseline_majority.txt','w')

for line_te in test_file:
	line_te = line_te.replace("\n", "")
	if(len(line_te.split()) > 0):
		output_file_majority.write(str(line_te.split()[0]))
		output_file_majority.write(" " + str(line_te.split()[1]))
		output_file_majority.write(" " + "O" + "\n")
	else:
		output_file_majority.write("\n")

test_file.close()
output_file_majority.close()

test_file = open('LUS.P1/data/P1_data/data/NLSPARQL.test.data', 'r')
output_file_chance = open('baseline_chance.txt','w')

for line_te in test_file:
	line_te = line_te.replace("\n", "")
	if(len(line_te.split()) > 0):
		output_file_chance.write(str(line_te.split()[0]))
		output_file_chance.write(" " + str(line_te.split()[1]))
		output_file_chance.write(" " + str(random.choice(concepts_repeated)) + "\n")
	else:
		output_file_chance.write("\n")

test_file.close()
output_file_chance.close()