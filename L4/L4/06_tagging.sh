[ -e 06_tagging ] && rm -r 06_tagging

mkdir 06_tagging

python3 01_create_POS_counts.py data_pos/train.pos.txt 06_tagging/POS.counts
python3 02_create_TOK_POS_counts.py data_pos/train.pos.txt 06_tagging/TOK_POS.counts
python3 03_create_TOK_POS_probs.py 06_tagging/POS.counts 06_tagging/TOK_POS.counts 06_tagging/TOK_POS.probs
python3 05_build_transducer_for_unk.py 06_tagging/TOK_POS.probs 06_tagging/UNK_POS.probs

sed -e 's/^/0	0	/' 06_tagging/TOK_POS.probs > 06_tagging/transducer.txt
echo "0" >> 06_tagging/transducer.txt
sed -e 's/^/0	0	/' 06_tagging/UNK_POS.probs > 06_tagging/unk_transducer.txt
echo "0" >> 06_tagging/unk_transducer.txt

ngramsymbols < data_pos/train.pos.txt > 06_tagging/lexicon.lex

fstcompile --isymbols=06_tagging/lexicon.lex --osymbols=06_tagging/lexicon.lex 06_tagging/transducer.txt | fstarcsort > 06_tagging/transducer.fst

fstdraw --portrait=true --isymbols=06_tagging/lexicon.lex --osymbols=06_tagging/lexicon.lex 06_tagging/transducer.fst | dot -Tpng -Gdpi=300 > 06_tagging/transducer.png

fstcompile --isymbols=06_tagging/lexicon.lex --osymbols=06_tagging/lexicon.lex 06_tagging/unk_transducer.txt | fstarcsort > 06_tagging/unk_transducer.fst

fstdraw --portrait=true --isymbols=06_tagging/lexicon.lex --osymbols=06_tagging/lexicon.lex 06_tagging/unk_transducer.fst | dot -Tpng -Gdpi=300 > 06_tagging/unk_transducer.png

fstunion 06_tagging/transducer.fst 06_tagging/unk_transducer.fst > 06_tagging/transducer_union.fst

fstdraw --portrait=true --isymbols=06_tagging/lexicon.lex --osymbols=06_tagging/lexicon.lex 06_tagging/transducer_union.fst | dot -Tpng -Gdpi=300 > 06_tagging/transducer_union.png

echo "star of thor" | farcompilestrings --symbols=06_tagging/lexicon.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_suffix='.fst'

mv 1.fst 06_tagging/compiled_string.fst

fstdraw --portrait=true --isymbols=06_tagging/lexicon.lex --osymbols=06_tagging/lexicon.lex 06_tagging/compiled_string.fst | dot -Tpng -Gdpi=300 > 06_tagging/compiled_string.png

fstcompose 06_tagging/compiled_string.fst 06_tagging/transducer_union.fst | fstrmepsilon > 06_tagging/transducer_composed.fst

fstdraw --portrait=true --isymbols=06_tagging/lexicon.lex --osymbols=06_tagging/lexicon.lex 06_tagging/transducer_composed.fst | dot -Tpng -Gdpi=300 > 06_tagging/transducer_composed.png

fstshortestpath 06_tagging/transducer_composed.fst | fstrmepsilon > 06_tagging/transducer_shortestpath.fst

fstdraw --portrait=true --isymbols=06_tagging/lexicon.lex --osymbols=06_tagging/lexicon.lex 06_tagging/transducer_shortestpath.fst | dot -Tpng -Gdpi=300 > 06_tagging/transducer_shortestpath.png