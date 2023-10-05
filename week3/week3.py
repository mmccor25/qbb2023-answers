#!/usr/bin/env python

from fasta import readFASTA

# EXERCISE 1

# arguments: fasta_file, scoring_matrix.txt, gap_penalty, file_path

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

file_path = sys.argv[4]

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


# 1.4
sequence1_alignment = ""
sequence2_alignment = ""

i, j = len(sequence1), len(sequence2)
while i >= 0 and j >= 0:
	if traceback_matrix[i,j] == "d":
		sequence1_alignment = sequence1[i-1] + sequence1_alignment
		sequence2_alignment = sequence2[j-1] + sequence2_alignment
		i -= 1
		j -= 1
	elif traceback_matrix[i,j] == "h":
		sequence1_alignment = "-" + sequence1_alignment
		sequence2_alignment = sequence2[j-1] + sequence2_alignment
		j -= 1
	elif traceback_matrix[i,j] == "v":
		sequence1_alignment = sequence1[i-1] + sequence1_alignment
		sequence2_alignment = "-" + sequence2_alignment
		i -= 1
	else:
		i -= 1
		j -= 1

# count gaps
gaps_1 = 0
for i in range(len(sequence1_alignment)):
	if sequence1_alignment[i] == "-":
		gaps_1 += 1

gaps_2 = 0
for i in range(len(sequence2_alignment)):
	if sequence2_alignment[i] == "-":
		gaps_2 += 1

# score alignment
alignment_score = F_matrix[F_matrix.shape[0]-1, F_matrix.shape[1]-1]

alignment1_output = "Sequence 1 alignment: " + sequence1_alignment + "\n"
alignment2_output = "Sequence 2 alignment: " + sequence2_alignment + "\n"
gaps1_output = "Gaps in sequence 1: " + str(gaps_1) + "\n"
gaps2_output = "Gaps in sequence 2: " + str(gaps_2) + "\n"
score_output = "Sequence alignment score: " + str(alignment_score)


# 1.5
output_file = open(file_path, "w")
output_file.write(
	alignment1_output + alignment2_output + gaps1_output + gaps2_output + score_output)


	