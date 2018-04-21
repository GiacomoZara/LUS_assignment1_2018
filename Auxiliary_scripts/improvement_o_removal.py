import os

# removing files
os.system("[ -e lus_project1 ] && rm LUS.P1/data/P1_data/data/train_o_removed.data")

# writing new training file
original_training_file = open('LUS.P1/data/P1_data/data/NLSPARQL.train.data' , 'r')
new_training_file = open('LUS.P1/data/P1_data/data/train_o_removed.data', 'w')

for line in original_training_file:
	split_line = line.split()
	if len(split_line) > 0:
		new_training_file.write(str(split_line[0]))
		new_training_file.write('\t')
		if split_line[1] == 'O':
			new_training_file.write("_" + str(split_line[0]) + "_")
		else:
			new_training_file.write(str(split_line[1]))
		new_training_file.write('\n')
	else:
		new_training_file.write('\n')

original_training_file.close()
new_training_file.close()