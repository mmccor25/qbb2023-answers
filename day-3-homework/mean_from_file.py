#! /usr/bin/env python

import sys

data = open(sys.argv[1], "r")
lines = data.readlines()
numbers = []


for i in lines:
	i = int(i.strip())
	numbers.append(i)


def mean_fn(my_list):
	assert type(my_list) == list, "must be a list"
	for i in my_list:
		assert type(i) == int, "must use integers"
	average = sum(my_list)/len(my_list)
	return average

print(mean_fn(numbers))
