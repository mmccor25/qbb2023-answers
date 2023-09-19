#!/usr/bin/env python


# 1.1
import pandas as pd

dnm = pd.read_csv("aau1043_dnm.csv")


# 1.2
deNovoCount = {}

for i in range(len(dnm)):
	proband_id = dnm.loc[i, "Proband_id"]
	parent = dnm.loc[i, "Phase_combined"]

	if proband_id not in deNovoCount:
		deNovoCount[proband_id] = [0,0]
		#adds new proband_id to dictionary with "proband_id: []
	if parent == "mother":
		deNovoCount[proband_id][0] += 1
	elif parent == "father":
		deNovoCount[proband_id][1] += 1


# 1.3
deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])


# 1.4
age = pd.read_csv("aau1043_parental_age.csv", index_col = "Proband_id")


#1.5
merged = pd.concat([deNovoCountDF, age], axis = 1, join = 'inner')

print(merged)