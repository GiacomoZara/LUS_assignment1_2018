[ -e 01_create_POS_counts ] && rm -r 01_create_POS_counts

mkdir 01_create_POS_counts

python3 01_create_POS_counts.py data_pos/train.pos.txt 01_create_POS_counts/POS.counts