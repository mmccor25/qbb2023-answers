#!/usr/bin/env python

#EXERCISE 1
data = open("data/inflammation-01.csv", "r")
each_line = data.readlines()
patients = []

for line in each_line:
	line = line.rstrip()
	line = line.split(",")
	patients.append(line)
	
print("Answer 1:", patients[4][0], patients[4][9], patients[4][-1])


#EXERCISE 2
int_patients = []

for individual in patients:
	int_patient =[]
	for day in individual:
		day = int(day)
		int_patient.append(day)
	int_patients.append(int_patient)
#made a list of all patient data, in integers

import numpy as np

avg_first_10 = []
for patient in range(10):
	patient = np.mean(int_patients[patient])
	avg_first_10.append(patient)
print("Answer 2:", avg_first_10)


#EXERCISE 3
print("Answer 3:", np.max(avg_first_10), np.min(avg_first_10))


#EXERCISE 4
diffs = []
for i in range(len(int_patients[0])):
	diff = (int_patients[0][i])-(int_patients[4][i])

	diffs.append(diff)
print("Answer 4:", diffs)

#OPTIONAL EXERCISE
# for patient in range(len(int_patients)):

daily_avgs = []
for patient in int_patients:
	oneday = []
	day = 0
	oneday.append(patient[day])
	print(oneday, len(oneday))
# print("Bonus Answer:", np.max(daily_avgs))
	

	# #incomplete