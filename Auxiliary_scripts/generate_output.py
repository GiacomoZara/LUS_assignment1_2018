import os
import pickle
import sys

# given a lexicon index, retrieves the corresponding word
def retrieve(lex_index):
	res = -1
	lexicon = open('lexicon.lex', 'r')
	for lex_line in lexicon:
		lex_line = lex_line.replace("\n", "")
		if len(lex_line.split()) > 0:
			if (lex_line.split()[1] == lex_index):
				res = lex_line.split()[0]
				break
	assert(not(res == -1))
	return res

# retrieves the predicted concepts of the sentence
def get_concepts():
	res = []
	myfile = open('result.txt', 'r')
	for line in myfile:
		line = line.replace("\n", "")
		if len(line.split()) > 2:
			res.append(retrieve(line.split()[3]))
	myfile.close()
	assert(len(res) > 0)
	return res
			
		
# removing giles
os.system("[ -e 09_all_together ] && rm final_output.txt compiled_string.fst result.fst result.txt")

# predicts the concepts for a given sentence
def predict(sentence):
	os.system("echo \"" + str(sentence) + "\" | farcompilestrings --symbols=lexicon.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_suffix='.fst'")
	os.system("mv 1.fst compiled_string.fst")
	os.system("fstcompose compiled_string.fst transducer_complete.fst | fstcompose - encoded_concepts_sequences.lm | fstrmepsilon | fstshortestpath | fsttopsort > result.fst")	
	os.system("fstprint result.fst > result.txt")
	result.append(get_concepts())
	os.system("[ -e 09_all_together ] && rm result.fst result.txt")

# test file	
test_filename = str(sys.argv[1])
test_file = open(test_filename, 'r', encoding='utf8')

result = []

sentence = ""

#iteration = 0

# applying prediction
for line in test_file:
	line = line.replace("\n", "")
	#if((iteration % 100) == 0):
		#print("Iteration " + str(iteration))
	#iteration += 1
	if len(line.split()) > 0:
		word = line.split()[0]
		sentence += " " + str(word)
	else:
		predict(sentence.lstrip())
		sentence = ""

test_file.close()

# dumping/loading result
with open('resultlist', 'wb') as fp:
	pickle.dump(result, fp)

predicted_concepts = []

for sublist in result:
	for item in sublist:
		predicted_concepts.append(item)

test_file = open(test_filename)
output_file = open('final_output.txt', 'w')

ind = 0

# writing output file
for line in test_file:
	line = line.replace("\n", "")
	if(len(line.split()) > 0):
		if ((str(predicted_concepts[ind])).startswith("_")):
			predicted_value = "O"
		else:
			predicted_value = str(predicted_concepts[ind])
		output_file.write(str(line.split()[0]))
		output_file.write(" " + str(line.split()[1]))
		output_file.write(" " + predicted_value + "\n")
		ind +=1
	else:
		output_file.write("\n")

output_file.close()
test_file.close()

