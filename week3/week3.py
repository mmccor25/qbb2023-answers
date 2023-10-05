#!/usr/bin/env python

from fasta import readFASTA

# EXERCISE 1

# arguments: fasta_file, scoring_matrix.txt, gap_penalty, file path

import sys
import pandas as pd
import numpy as np

gap_penalty = float(sys.argv[3])

matrix = pd.read_csv(sys.argv[2], delim_whitespace=True)

input_sequences = readFASTA(open(sys.argv[1]))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
traceback_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1), dtype=str)


# 1.3
for i in range(len(sequence1)+1):
	F_matrix[i,0] = i * gap_penalty
for j in range(len(sequence2)+1):
	F_matrix[0,j] = j * gap_penalty

for i in range(1, len(sequence1)+1):
	traceback_matrix[i, 0] = "v"
for j in range(1, len(sequence2)+1):
	traceback_matrix[0, j] = "h"



for i in range(1, len(sequence1)+1):
	for j in range(1, len(sequence2)+1):
		score = matrix.loc[sequence1[i-1], sequence2[j-1]]
		d = F_matrix[i-1, j-1] + score
		h = F_matrix[i, j-1] + gap_penalty
		v = F_matrix[i-1, j] + gap_penalty

		F_matrix[i,j] = max(d, h, v)

		if max(d, h, v) == d:
			traceback_matrix[i,j] = "d"
		elif max(d, h, v) == h:
			traceback_matrix[i,j] = "h"
		elif max(d, h, v) == v:
			traceback_matrix[i,j] = "v"

print(F_matrix)
print(traceback_matrix)


# 1.4
sequence1_alignment = []
sequence2_alignment = []

i, j = len(sequence1), len(sequence2)
while i >= 0 and j >= 0:
	if traceback_matrix[i,j] == "d":
		sequence1_alignment.insert(0, sequence1[i-1])
		sequence2_alignment.insert(0, sequence2[j-1])
		i -= 1
		j -= 1
	elif traceback_matrix[i,j] == "h":
		sequence1_alignment.insert(0,"-")
		sequence2_alignment.insert(0, sequence2[j-1])
		j -= 1
	elif traceback_matrix[i,j] == "v":
		sequence1_alignment.insert(0, sequence1[i-1])
		sequence2_alignment.insert(0,"-")
		i -= 1
	else:
		i -= 1
		j -= 1

sequence1_string = ''.join(sequence1_alignment)
sequence2_string = ''.join(sequence2_alignment)

print(sequence1_string)
print(sequence2_string)

	