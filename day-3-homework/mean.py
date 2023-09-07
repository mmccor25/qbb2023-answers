#! /usr/bin/env python

myNumbers = [42, 13, 39, 256, 3, 95]

def mean_fn(my_list):
	assert type(my_list) == list, "must be a list"
	for i in my_list:
		assert type(i) == int, "must use integers"
	average = sum(my_list)/len(my_list)
	return average

print(mean_fn(myNumbers))

