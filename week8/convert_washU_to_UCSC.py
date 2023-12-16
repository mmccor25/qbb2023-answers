#!/usr/bin/env python
import sys
import pandas as pd

# 2.1
baitmap = sys.argv[1]
washU_results = sys.argv[2]
output_file = sys.argv[3]

baitmap = pd.read_csv(baitmap, delim_whitespace=True, engine='python')
genes = baitmap.iloc[:,3]

bait_chrom = baitmap.iloc[:,0]
bait_start = baitmap.iloc[:,1]
bait_end =  baitmap.iloc[:,2]



# # I tried two different methods of identifying baits, but both of them resulted in "None of <bait index> are in the <fragment index>" when I tried to index
# # identifying fragments Method 2 (use  "output/data/output_washU_text.csv" for this method, and .txt for method 1)
# washu = pd.read_csv(washU_results)

# frag1 = washu.iloc[:, 0]
# frag2 = washu.iloc[:, 1]
# strength = washu.iloc[:, 2]


# baits = []
# for i in range(len(baitmap)):
# 	concat = 'chr'+str(baitmap.iloc[i,0])+','+str(baitmap.iloc[i,1])+','+str(baitmap.iloc[i,2])
# 	baits.append(concat)

# is_bait1 = frag1.loc[baits]
# is_bait2 = frag2.loc[baits]




# identifying fragments Method 1 (use  output/data/output_washU_text.txt)
washu = pd.read_csv(washU_results, sep=",|t")
frag1_chrom = washu.iloc[:, 0]
# frag1_chrom.str.lstrip('chr')
frag1_start = washu.iloc[:, 1]
frag1_end = washu.iloc[:, 2]

frag2_chrom = washu.iloc[:, 3]
frag2_start = washu.iloc[:, 4]
frag2_end = washu.iloc[:, 5]

strength = washu.iloc[:, 6]


# # identifying which are baits
# same_start = frag1_start.loc[bait_start]


# 2.2
max_strength = strength.max()
score = int(strength / max_strength) * 1000


# input to UCSC format
ucsc = pd.DataFrame(columns=['#chrom', 'chromStart', 'chromEnd', 'name', 'score', 'value', 'color', 'sourceChrom', 'sourceStart', 'sourceEnd', 'sourceName', 'sourceStrand', 'targetChrom', 'targetStart', 'targetEnd', 'targetName', 'targetStrand'])
for i in washu.index:
	ucsc.loc[i, '#chrom'] = frag1_chrom[i]
	ucsc.loc[i, 'chromStart'] = frag1_start[i]
	ucsc.loc[i, 'chromEnd'] = frag1_end[i]
	ucsc.loc[i, 'name'] = '.'
	ucsc.loc[i, 'score'] = score[i]
	ucsc.loc[i, 'value'] = '.'
	ucsc.loc[i, 'color'] = '.'

	ucsc.loc[i, 'sourceChrom'] = frag2_chrom[i]
	ucsc.loc[i, 'sourceStart'] = frag2_start[i]
	ucsc.loc[i, 'sourceEnd'] = frag2_end[i]
	ucsc.loc[i, 'sourceName'] = '.'
	ucsc.loc[i, 'sourceStrand'] = '.'

	ucsc.loc[i, 'targetChrom'] = bait_chrom[i]
	ucsc.loc[i, 'targetStart'] = bait_start[i]
	ucsc.loc[i, 'targetEnd'] = bait_end[i]
	ucsc.loc[i, 'targetName'] = '.'
	ucsc.loc[i, 'targetStrand'] = '.'


# Top interactions
strength_promprom = strength.loc[two_baits].sort_values()
top_6_promprom = strength_promprom[-6:]
top_6_promprom_genes = baitmap.loc[top_6_promprom]
print(top_6_promprom_genes)

strength_enhprom = strength.loc[one_bait].sort_values()
top_6_enhprom = strength_promprom[-6:]
top_6_enhprom_genes = baitmap.loc[top_6_enhprom]
print(top_6_enhprom_genes)

# Make bed file
with open(output_file, 'w') as file:
	file.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full')
	file.write(ucsc.to_string(header=False, index=False)

