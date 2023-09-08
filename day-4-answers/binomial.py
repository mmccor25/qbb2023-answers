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

def make_plots(pop_size, starting_freq):
	import matplotlib.pyplot as plt

	# xy plot with multiple iterations
	fig, (ax1, ax2 )= plt.subplots(1, 2)
	for i in range(30):
		function = wright_fisher(pop_size, starting_freq)
		generation = range(function[1])
		allele_freq_list = function[0]
		ax1.plot(generation, allele_freq_list)

	#Histogram
	final_generations = []
	for i in range(1000):
		function = wright_fisher(pop_size, starting_freq)
		final = (function[1])
		final_generations.append(final)
	ax2.hist(final_generations)

	plt.show()

make_plots(452, .3)