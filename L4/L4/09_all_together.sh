[ -e 09_all_together ] && rm -r 09_all_together

mkdir 09_all_together

python3 01_create_POS_counts.py data_pos/train.pos.txt 09_all_together/POS.counts
python3 02_create_TOK_POS_counts.py data_pos/train.pos.txt 09_all_together/TOK_POS.counts
python3 03_create_TOK_POS_probs.py 09_all_together/POS.counts 09_all_together/TOK_POS.counts 09_all_together/TOK_POS.probs
python3 05_build_transducer_for_unk.py 09_all_together/TOK_POS.probs 09_all_together/UNK_POS.probs

sed -e 's/^/0	0	/' 09_all_together/TOK_POS.probs > 09_all_together/transducer.txt
echo "0" >> 09_all_together/transducer.txt
sed -e 's/^/0	0	/' 09_all_together/UNK_POS.probs > 09_all_together/unk_transducer.txt
echo "0" >> 09_all_together/unk_transducer.txt

# generating global lexicon
ngramsymbols < data_pos/train.pos.txt > 09_all_together/lexicon.lex

# generating global transducer (one state going in itself with each probability for each couple (word, tag)
fstcompile --isymbols=09_all_together/lexicon.lex --osymbols=09_all_together/lexicon.lex 09_all_together/transducer.txt | fstarcsort > 09_all_together/transducer.fst


fstdraw --portrait=true --isymbols=09_all_together/lexicon.lex --osymbols=09_all_together/lexicon.lex 09_all_together/transducer.fst | dot -Tpng -Gdpi=300 > 09_all_together/transducer.png


# generating UNKNOWN transducer (one state going in itself with 1/m probability for each of the m tags)
fstcompile --isymbols=09_all_together/lexicon.lex --osymbols=09_all_together/lexicon.lex 09_all_together/unk_transducer.txt | fstarcsort > 09_all_together/unk_transducer.fst


fstdraw --portrait=true --isymbols=09_all_together/lexicon.lex --osymbols=09_all_together/lexicon.lex 09_all_together/unk_transducer.fst | dot -Tpng -Gdpi=300 > 09_all_together/unk_transducer.png


# uniting global and UNKNOWN transducers 
fstunion 09_all_together/transducer.fst 09_all_together/unk_transducer.fst > 09_all_together/transducer_union.fst


fstdraw --portrait=true --isymbols=09_all_together/lexicon.lex --osymbols=09_all_together/lexicon.lex 09_all_together/transducer_union.fst | dot -Tpng -Gdpi=300 > 09_all_together/transducer_union.png


# encoding string
echo "star of thor" | farcompilestrings --symbols=09_all_together/lexicon.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_suffix='.fst'

mv 1.fst 09_all_together/compiled_string.fst

fstdraw --portrait=true --isymbols=09_all_together/lexicon.lex --osymbols=09_all_together/lexicon.lex 09_all_together/compiled_string.fst | dot -Tpng -Gdpi=300 > 09_all_together/compiled_string.png

# compute sequence of pos tags for each sentence of the training set
python3 07_pos_tag_sentence_per_line.py data_pos/train.pos.txt 09_all_together/post_tag_sentences.txt

# encode sequence of pos tags
farcompilestrings --symbols=09_all_together/lexicon.lex --unknown_symbol='<unk>' 09_all_together/post_tag_sentences.txt > 09_all_together/pos.far

# count ngrams
ngramcount --order=3 --require_symbols=false 09_all_together/pos.far > 09_all_together/pos.cnt

# compute language model for tag given previous tag
ngrammake --method=witten_bell 09_all_together/pos.cnt > 09_all_together/pos.lm

# apply global transducer, remove epsilon and find shortest path for the encoded string
fstcompose 09_all_together/compiled_string.fst 09_all_together/transducer_union.fst | fstcompose - 09_all_together/pos.lm | fstrmepsilon | fstshortestpath > 09_all_together/09_all_together.fst

fstdraw --portrait=true --isymbols=09_all_together/lexicon.lex --osymbols=09_all_together/lexicon.lex 09_all_together/09_all_together.fst | dot -Tpng -Gdpi=300 > 09_all_together/09_all_together.png
