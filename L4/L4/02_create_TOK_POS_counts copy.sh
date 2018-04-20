[ -e 02_create_TOK_POS_counts ] && rm -r 02_create_TOK_POS_counts

mkdir 02_create_TOK_POS_counts

python3 02_create_TOK_POS_counts.py data_pos/train.pos.txt 02_create_TOK_POS_counts/TOK_POS.counts