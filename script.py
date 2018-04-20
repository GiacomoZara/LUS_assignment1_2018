import os
import subprocess
import sys

ngram_size = 4

# removing files
os.system("[ -e 09_all_together ] && rm lexicon.lex transducer.fst transducer_unk.fst transducer_complete.fst encoded_concepts_sequences.far encoded_concepts_sequences.cnt encoded_concepts_sequences.lm")

# handling training and test sets
subprocess.call(["python3", "improvement_o_removal.py"])

# generating probabilities
subprocess.call("python3 compute_probabilities.py LUS.P1/data/P1_data/data/train_o_removed.data", shell = True)

# generating transducers
subprocess.call(["python3", "generate_transducers.py"])

# generating lexicon
os.system("ngramsymbols < LUS.P1/data/P1_data/data/train_o_removed.data > lexicon.lex")

# encoding global transducer
os.system("fstcompile --isymbols=lexicon.lex --osymbols=lexicon.lex transducer_global.txt | fstarcsort > transducer_complete.fst")

# generating concepts sequences
subprocess.call("python3 get_concepts_sequences.py LUS.P1/data/P1_data/data/train_o_removed.data", shell = True)

# encoding concepts sequences
os.system("farcompilestrings --symbols=lexicon.lex --unknown_symbol='<unk>' concepts_sequences.txt > encoded_concepts_sequences.far")

# count ngrams
os.system("ngramcount --order=" + str(ngram_size) + " --require_symbols=false encoded_concepts_sequences.far > encoded_concepts_sequences.cnt")

# compute language model
os.system("ngrammake --method=kneser_ney encoded_concepts_sequences.cnt > encoded_concepts_sequences.lm")

# output
subprocess.call("python3 generate_output.py LUS.P1/data/P1_data/data/NLSPARQL.test.data", shell = True)

# evaluation
os.system("./LUS.P1/data/P1_data/scripts/conlleval.pl < final_output.txt")
