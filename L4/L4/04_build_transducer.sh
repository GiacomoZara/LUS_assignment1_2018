[ -e 04_build_transducer ] && rm -r 04_build_transducer

mkdir 04_build_transducer

python3 01_create_POS_counts.py data_pos/train.pos.txt 04_build_transducer/POS.counts
python3 02_create_TOK_POS_counts.py data_pos/train.pos.txt 04_build_transducer/TOK_POS.counts
python3 03_create_TOK_POS_probs.py 04_build_transducer/POS.counts 04_build_transducer/TOK_POS.counts 04_build_transducer/TOK_POS.probs

sed -e 's/^/0	0	/' 04_build_transducer/TOK_POS.probs > 04_build_transducer/transducer.txt

ngramsymbols < data_pos/train.pos.txt > 04_build_transducer/lexicon.lex

fstcompile --isymbols=04_build_transducer/lexicon.lex --osymbols=04_build_transducer/lexicon.lex 04_build_transducer/transducer.txt | fstarcsort > 04_build_transducer/transducer.fst

fstdraw --portrait=true --isymbols=04_build_transducer/lexicon.lex --osymbols=04_build_transducer/lexicon.lex 04_build_transducer/transducer.fst | dot -Tpng -Gdpi=300 > 04_build_transducer/transducer.png