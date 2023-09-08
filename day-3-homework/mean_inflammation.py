#!/usr/bin/env python


def mean_inflammation(patient_row_index, data_file_name):
	data = open(data_file_name, "r")

	i = 0
	for line in data:
		if i == patient_row_index:
			patient = line
		else:
			i = i+1
			
	patient = patient.rstrip()
	patient = patient.split(",")
	
	int_patient = []
	for day in patient:
		day = int(day)
		int_patient.append(day)
	
	mean = sum(int_patient)/len(int_patient)
	return print(mean)

mean_inflammation(12, "../inflammation-01.csv")