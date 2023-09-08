#!/usr/bin/env python


def wright_fisher(pop_size, starting_freq):
	# Get a starting frequency and pop size

	import numpy as np
	
	# n = 2*pop size, p = frequency in allele

	# Make a list to store allele frequencies
	allele_freq = [starting_freq]
	pop = 2*pop_size
	freq = starting_freq

	while 0 < freq < 1:
		# Get the new allele frequency for next generation by drawing from the binomial distribution
		no_successes= np.random.binomial(pop, freq)
		freq = no_successes/pop
		# Store our allele frequency in an allele frequency list
		allele_freq.append(freq)

		
	return allele_freq, len(allele_freq)

import matplotlib.pyplot as plt

# xy plot with multiple iterations
# fig, ax = plt.subplots()
# for i in range(30):
# 	function = wright_fisher(452, .3)
# 	generation = range(len(function[1]))
# 	allele_freq_list = function[0]
# 	ax.plot(generation, allele_freq_list)
# plt.show()

#Histogram
final_generations = []
for i in range(1000):
	function = wright_fisher(452, .3)
	final = (function[1])
	final_generations.append(final)
fig = plt.hist(final_generations)

plt.show()