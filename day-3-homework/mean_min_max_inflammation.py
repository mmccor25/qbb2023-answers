#!/usr/bin/env python

def mean_inflammation(listy_list):
	mean = sum(listy_list)/len(listy_list)
	return print(mean)


def maximum(listy_list):
	maximum = listy_list[0]
	for i in listy_list:
		if maximum < i:
			maximum = i
	return maximum


def minimum(listy_list):
	minimum = listy_list[0] 
	for i in listy_list:
		if minimum > i:
			minimum = i
	return minimum

def mean_max_min(patient_row_index, data_file_name):
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

	mean = mean_inflammation(int_patient)
	minimum_ = minimum(int_patient)
	maximum_ = maximum(int_patient)


	mean_min_max_inflammation = {"mean": mean, "min": minimum_, "max": maximum_ }
	return mean_min_max_inflammation

print(mean_max_min(12, "../inflammation-01.csv"))