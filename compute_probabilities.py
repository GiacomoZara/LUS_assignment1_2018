import math
import os
import sys

# selecting training file
train_filename = str(sys.argv[1])

# removing files
os.system("[ -e 09_all_together ] && rm probabilities_wc.txt distinct_concepts.txt")

# lists for all words and concepts
words = []
concepts = []


# reading words and tags
training_file = open(train_filename)

for line in training_file:
	line = line.replace("\n", "")
	if(len(line.split()) > 0):
		words.append(line.split()[0])
		concepts.append(line.split()[1])

training_file.close()

# asserting lenghts
assert(len(words) == len(concepts))
length = len(words)


# collecting count of couples (word, concepts)
count_wc = {}

for i in range(length):
	word = words[i]
	concept = concepts[i]
	couple = (word, concept)
	if count_wc.get(couple):
		count_wc[couple] = count_wc[couple] + 1
	else:
		count_wc[couple] = 1

# collecting distinct sentences
sentences = []
concept_sentences = []

sentence_as_list = []
concept_sentence_as_list = []

training_file = open(train_filename)

for line in training_file:
	line = line.replace("\n", "")
	if len(line.split()) > 0:
		sentence_as_list.append(line.split()[0])
		concept_sentence_as_list.append(line.split()[1])
	else:
		sentences.append(sentence_as_list)
		concept_sentences.append(concept_sentence_as_list)
		sentence_as_list = []
		concept_sentence_as_list = []

training_file.close()

# collecting count of concepts
distinct_concepts = list(set(concepts))
count_c = {}

for distinct_concept in distinct_concepts:
	count_c[distinct_concept] = concepts.count(distinct_concept)

# collecting count of concept given previous concept
count_cc = {}

for concept_sentence in concept_sentences:
	for index in range(len(concept_sentence)):
		if index > 0:
			couple = (concept_sentence[index], concept_sentence[index-1])
			if count_cc.get(couple):
				count_cc[couple] = count_cc[couple] + 1
			else:
				count_cc[couple] = 1
		
# collecting probability of couples (word, concept)
probabilities_wc = {}

for item in count_wc:
	probabilities_wc[item] = -math.log(count_wc[item] / count_c[item[1]])

# collecting probability of concept given concept
probabilities_cc = {}

for item in count_cc:
	probabilities_cc[item] = count_cc[item] / count_c[item[1]]

# outputting probabilities
output_file_probs = open('probabilities_wc.txt', 'w')


for item in probabilities_wc:
	output_file_probs.write(str(item[0]) + "\t" + str(item[1]) + "\t" + str(probabilities_wc[item]) + "\n")

output_file_probs.close()

# outputting concepts
output_file_concepts = open('distinct_concepts.txt', 'w')

for dc in distinct_concepts:
	output_file_concepts.write(str(dc) + "\n")

output_file_concepts.close()
