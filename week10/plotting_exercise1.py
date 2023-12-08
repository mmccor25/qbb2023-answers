#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)


# 1.1
nonzeros = []
for i in counts_df_logged.loc["GTEX-113JC",:]:
	if i != 0:
		nonzeros.append(i)

# Histogram
fig, ax = plt.subplots()
ax.hist(nonzeros, bins=20, range=(0, 20))
ax.set_title("Distribution of expression across genes")
ax.set_xlabel("Expression")
fig.savefig("1.1_expression_distribution.png")


# 1.2

males = full_design_df.loc[full_design_df['SEX']== 1]
females = full_design_df.loc[full_design_df['SEX']== 2]

fig, ax = plt.subplots()
ax.hist(males.loc[:, "MXD4"], bins=20, range=(8, 15), color="blue", alpha = 0.5)
ax.hist(females.loc[:,"MXD4"], bins=20, range=(8, 15), color="red", alpha = 0.5)
ax.set_title("MXD4 expression")
ax.set_xlabel("Expression")
fig.savefig("1.2_MXD4_distribution.png")


# 1.3
age_counts = full_design_df["AGE"].value_counts()
age_labels = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]

age_distribution, ax = plt.subplots()
plt.bar(age_labels, age_counts.loc[age_labels])
ax.set_title("Distribution of subject ages")
age_distribution.savefig("age_distribution.png")


# 1.4
lpxn_males = males.loc[:, ["AGE", "LPXN"]]
male_medians = []
for i in age_labels:
	age_rows = lpxn_males.loc[:, "AGE"] == i
	age_values = lpxn_males[age_rows]
	median = np.median(age_values["LPXN"])
	male_medians.append(median)


lpxn_females = females.loc[:, ["AGE", "LPXN"]]
female_medians = []
for i in age_labels:
	age_rows = lpxn_females.loc[:, "AGE"] == i
	age_values = lpxn_females[age_rows]
	median = np.median(age_values["LPXN"])
	female_medians.append(median)


over_time, ax = plt.subplots()
plt.scatter(age_labels, male_medians)
plt.scatter(age_labels, female_medians)
ax.set_title("LPXN expression over time")
over_time.savefig("over_time.png")









