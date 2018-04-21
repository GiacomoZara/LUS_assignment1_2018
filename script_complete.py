import os
import subprocess
import sys

os.system("[ -e lus_project1 ] && rm lexicon.lex transducer.fst transducer_unk.fst transducer_complete.fst encoded_concepts_sequences.far encoded_concepts_sequences.cnt encoded_concepts_sequences.lm")

methods = ["witten_bell", "absolute", "kneser_ney", "katz"]
ngramsizes = [2,3,4,5]

for method in methods:
	for ngramsize in ngramsizes:
		os.system("[ -e 09_all_together ] && rm {0}_{1}_evaluation.txt".format(ngramsize, method))                                                                                                                                                                                           

			
# minimum (ngramsize = 3, method = witten_bell)
ngram_size = 3
method = "witten_bell"
print("Ngram size = " + str(ngram_size) + ", method = " + str(method) + "\n")
subprocess.call("python3 Auxiliary_scripts/compute_probabilities.py LUS.P1/data/P1_data/data/NLSPARQL.train.data", shell = True)
subprocess.call(["python3", "Auxiliary_scripts/generate_transducers.py"])
os.system("ngramsymbols < LUS.P1/data/P1_data/data/NLSPARQL.train.data > lexicon.lex")
os.system("fstcompile --isymbols=lexicon.lex --osymbols=lexicon.lex transducer_global.txt | fstarcsort > transducer_complete.fst")
subprocess.call("python3 Auxiliary_scripts/get_concepts_sequences.py LUS.P1/data/P1_data/data/NLSPARQL.train.data", shell = True)
os.system("farcompilestrings --symbols=lexicon.lex --unknown_symbol='<unk>' concepts_sequences.txt > encoded_concepts_sequences.far")
os.system("ngramcount --order=" + str(ngram_size) + " --require_symbols=false encoded_concepts_sequences.far > encoded_concepts_sequences.cnt")
os.system("ngrammake --method=" + str(method) + " encoded_concepts_sequences.cnt > encoded_concepts_sequences.lm")
subprocess.call("python3 Auxiliary_scripts/generate_output.py LUS.P1/data/P1_data/data/NLSPARQL.test.data", shell = True)
os.system("./LUS.P1/data/P1_data/scripts/conlleval.pl < final_output.txt")

subprocess.call(["python3", "improvement_o_removal.py"])

print("\n")

# with improvement
for method in methods:
	for ngramsize in ngramsizes:
		print("N-gram size = " + str(ngramsize) + ", method = " + str(method) + "\n")
		subprocess.call("python3 Auxiliary_scripts/compute_probabilities.py LUS.P1/data/P1_data/data/train_o_removed.data", shell = True)
		subprocess.call(["python3", "Auxiliary_scripts/generate_transducers.py"])
		os.system("ngramsymbols < LUS.P1/data/P1_data/data/train_o_removed.data > lexicon.lex")
		os.system("fstcompile --isymbols=lexicon.lex --osymbols=lexicon.lex transducer_global.txt | fstarcsort > transducer_complete.fst")
		subprocess.call("python3 Auxiliary_scripts/get_concepts_sequences.py LUS.P1/data/P1_data/data/train_o_removed.data", shell = True)
		os.system("farcompilestrings --symbols=lexicon.lex --unknown_symbol='<unk>' concepts_sequences.txt > encoded_concepts_sequences.far")
		os.system("ngramcount --order=" + str(ngramsize) + " --require_symbols=false encoded_concepts_sequences.far > encoded_concepts_sequences.cnt")
		os.system("ngrammake --method=" + str(method) + " encoded_concepts_sequences.cnt > encoded_concepts_sequences.lm")
		subprocess.call("python3 Auxiliary_scripts/generate_output.py LUS.P1/data/P1_data/data/NLSPARQL.test.data", shell = True)
		os.system("./LUS.P1/data/P1_data/scripts/conlleval.pl < final_output.txt > {0}_{1}_evaluation.txt".format(ngramsize, method))
		print("\n")