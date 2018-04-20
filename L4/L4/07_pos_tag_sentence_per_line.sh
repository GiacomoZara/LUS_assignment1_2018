[ -e 07_pos_tag_sentence_per_line ] && rm -r 07_pos_tag_sentence_per_line

mkdir 07_pos_tag_sentence_per_line

python3 07_pos_tag_sentence_per_line.py data_pos/train.pos.txt 07_pos_tag_sentence_per_line/post_tag_sentences.txt