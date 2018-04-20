[ -e 05_build_transducer_with_unk ] && rm -r 05_build_transducer_with_unk

mkdir 05_build_transducer_with_unk

python3 01_create_POS_counts.py data_pos/train.pos.txt 05_build_transducer_with_unk/POS.counts
python3 02_create_TOK_POS_counts.py data_pos/train.pos.txt 05_build_transducer_with_unk/TOK_POS.counts
python3 03_create_TOK_POS_probs.py 05_build_transducer_with_unk/POS.counts 05_build_transducer_with_unk/TOK_POS.counts 05_build_transducer_with_unk/TOK_POS.probs
python3 05_build_transducer_for_unk.py 05_build_transducer_with_unk/TOK_POS.probs 05_build_transducer_with_unk/UNK_POS.probs

sed -e 's/^/0	0	/' 05_build_transducer_with_unk/TOK_POS.probs > 05_build_transducer_with_unk/transducer.txt
echo "0" >> 05_build_transducer_with_unk/transducer.txt
sed -e 's/^/0	0	/' 05_build_transducer_with_unk/UNK_POS.probs > 05_build_transducer_with_unk/unk_transducer.txt
echo "0" >> 05_build_transducer_with_unk/unk_transducer.txt
ngramsymbols < data_pos/train.pos.txt > 05_build_transducer_with_unk/lexicon.lex

fstcompile --isymbols=05_build_transducer_with_unk/lexicon.lex --osymbols=05_build_transducer_with_unk/lexicon.lex 05_build_transducer_with_unk/transducer.txt | fstarcsort > 05_build_transducer_with_unk/transducer.fst

fstdraw --portrait=true --isymbols=05_build_transducer_with_unk/lexicon.lex --osymbols=05_build_transducer_with_unk/lexicon.lex 05_build_transducer_with_unk/transducer.fst | dot -Tpng -Gdpi=300 > 05_build_transducer_with_unk/transducer.png

fstcompile --isymbols=05_build_transducer_with_unk/lexicon.lex --osymbols=05_build_transducer_with_unk/lexicon.lex 05_build_transducer_with_unk/unk_transducer.txt | fstarcsort > 05_build_transducer_with_unk/unk_transducer.fst

fstdraw --portrait=true --isymbols=05_build_transducer_with_unk/lexicon.lex --osymbols=05_build_transducer_with_unk/lexicon.lex 05_build_transducer_with_unk/unk_transducer.fst | dot -Tpng -Gdpi=300 > 05_build_transducer_with_unk/unk_transducer.png

fstunion 05_build_transducer_with_unk/transducer.fst 05_build_transducer_with_unk/unk_transducer.fst > 05_build_transducer_with_unk/transducer_union.fst

fstdraw --portrait=true --isymbols=05_build_transducer_with_unk/lexicon.lex --osymbols=05_build_transducer_with_unk/lexicon.lex 05_build_transducer_with_unk/transducer_union.fst | dot -Tpng -Gdpi=300 > 05_build_transducer_with_unk/transducer_union.png