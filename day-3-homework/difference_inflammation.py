#!/usr/bin/env python

def mean_inflammation(patient1_row, patient2_row, data_file_name):
	data = open(data_file_name, "r")
	data = data.readlines()
	

	patient1 = data[patient1_row]
	patient1 = patient1.rstrip()
	patient1 = patient1.split(",")
	int_patient1 = []
	for day in patient1:
		day = int(day)
		int_patient1.append(day)

	patient2 = data[patient2_row]
	patient2 = patient2.rstrip()
	patient2 = patient2.split(",")
	int_patient2 = []
	for day in patient2:
		day = int(day)
		int_patient2.append(day)

	
	#Differences
	diffs = []
	for i in range(len(int_patient1)):
		diff = abs((int_patient1[i])-(int_patient2[i]))
		diffs.append(diff)
	print(diffs)

mean_inflammation(12, 13, "../inflammation-01.csv")