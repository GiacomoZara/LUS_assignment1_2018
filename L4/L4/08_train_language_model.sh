[ -e 08_train_language_model ] && rm -r 08_train_language_model

mkdir 08_train_language_model

python3 07_pos_tag_sentence_per_line.py data_pos/train.pos.txt 08_train_language_model/post_tag_sentences.txt

ngramsymbols < data_pos/train.pos.txt > 08_train_language_model/lexicon.lex

farcompilestrings --symbols=08_train_language_model/lexicon.lex --unknown_symbol='<unk>' 08_train_language_model/post_tag_sentences.txt > 08_train_language_model/pos.far

ngramcount --order=3 --require_symbols=false 08_train_language_model/pos.far > 08_train_language_model/pos.cnt

ngrammake --method=witten_bell 08_train_language_model/pos.cnt > 08_train_language_model/pos.lm