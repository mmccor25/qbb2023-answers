#!/usr/bin/env python
import sys
import pandas as pd

# 2.1
baitmap = sys.argv[1]
washU_results = sys.argv[2]
output_file = sys.argv[3]

baitmap = pd.read_csv(baitmap, delim_whitespace=True, index_col=0)
genes = baitmap.iloc[:,3]

washu = pd.read_csv(washU_results, sep=",|\t", engine='python')

# identifying fragments
frag_1 = washu.iloc[:,:3]
frag_2 = washu.iloc[:,3:6]


start_same = frag_1.loc[frag_1.loc[baitmap]]

print(len(start_same))

# frag_1_lists = frag_1.apply(lambda row: row.tolist(), axis=1)

# for row in frag_1_lists:
# 	row = row()

# frag_1_bait = frag_1.loc[frag_1.loc[str(frag_1_lists).strip('\n*')]]






with open(output_file, 'w') as file:
	file.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full')