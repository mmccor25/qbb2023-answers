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
# EXERCISE 2
# 2.1
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

mat_age = merged.loc[:, 'Mother_age']
mat_dnm = merged.loc[:, 'maternal_dnm']

pat_age = merged.loc[:, 'Father_age']
pat_dnm = merged.loc[:, 'paternal_dnm']

fig1, mat = plt.subplots()
mat.scatter(mat_age, mat_dnm)
mat.set_title("Maternal de novo mutations")
mat.set_xlabel("Maternal age (years)")
mat.set_ylabel("Count of maternal de novo mutations")
fig1.savefig( "ex2_a.png" )

fig2, pat = plt.subplots()
pat.scatter(pat_age, pat_dnm)
pat.set_title("Paternal de novo mutations")
pat.set_xlabel("Paternal age (years)")
pat.set_ylabel("Count of paternal de novo mutations")
fig2.savefig( "ex2_b.png" )

# plt.show()
# plt.close()


# 2.2
import statsmodels.formula.api as smf

maternal = smf.ols(formula = "maternal_dnm ~ 1 + Mother_age", data = merged)
m_results = maternal.fit()
print(m_results.summary())

# 2.3
paternal = smf.ols(formula = "paternal_dnm ~ 1 + Father_age", data = merged)
p_results = paternal.fit()
print(p_results.summary())


# 2.5

fig3, both = plt.subplots()
both.hist(mat_dnm, label = "maternal", alpha = 0.5)
both.hist(pat_dnm, label = "paternal", alpha = 0.5)
fig3.savefig( "ex2_c.png" )


# plt.show()
# plt.close()


# 2.6
import scipy.stats as sps
t, p = sps.ttest_rel(mat_dnm, pat_dnm)
print(p)