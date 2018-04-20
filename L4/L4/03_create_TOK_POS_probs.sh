[ -e 03_create_TOK_POS_probs ] && rm -r 03_create_TOK_POS_probs

mkdir 03_create_TOK_POS_probs

python3 01_create_POS_counts.py data_pos/train.pos.txt 03_create_TOK_POS_probs/POS.counts
python3 02_create_TOK_POS_counts.py data_pos/train.pos.txt 03_create_TOK_POS_probs/TOK_POS.counts
python3 03_create_TOK_POS_probs.py 03_create_TOK_POS_probs/POS.counts 03_create_TOK_POS_probs/TOK_POS.counts 03_create_TOK_POS_probs/TOK_POS.probs