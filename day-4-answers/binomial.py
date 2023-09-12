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


print(wright_fisher(452, .3)[1])

import matplotlib.pyplot as plt


function = wright_fisher(452, .3)
fig, ax = plt.subplots()
generation = range(function[1])
allele_freq_list = function[0]
ax.plot(generation, allele_freq_list)
ax.set_title("Allele frequency over time")
ax.set_xlabel("Time (generations)")
ax.set_ylabel("Allele frequency")
fig.savefig( "Allele-freq-over-time")
plt.show() 


def make_plots(pop_size, starting_freq, xy_iterations, hist_iterations):
	# xy plot with multiple iterations
	fig, ax1= plt.subplots()
	for i in range(xy_iterations):
		function = wright_fisher(pop_size, starting_freq)
		generation = range(function[1])
		allele_freq_list = function[0]
		ax1.plot(generation, allele_freq_list)
	ax1.set_title("Allele frequency over time")
	ax1.set_xlabel("Time (generations)")
	ax1.set_ylabel("Allele frequency")
	fig.savefig( "Allele-freq-over-time-multiple" )
	plt.show()

	#Histogram
	final_generations = []
	for i in range(hist_iterations):
		function = wright_fisher(pop_size, starting_freq)
		final = (function[1])
		final_generations.append(final)
	fig, ax2 = plt.subplots() 
	ax2.hist(final_generations)
	ax2.set_title("Times to fixation")
	ax2.set_xlabel("Time to fixation(generations)")
	ax2.set_ylabel("Count")
	fig.savefig( "times-to-fixation")
	plt.show()

make_plots(452, .3, 30, 1000)


#EXERCISE 3

#avg fixation times over 50 iterations for each of 5 population sizes
population_sizes = [52, 84, 3332, 225, 2345]
avg_fix_times = []
for size in population_sizes:
	fixation_times = []
	for i in range(50):
		output = wright_fisher(size, .3)
		generation = output[1]
		fixation_times.append(generation)
	average = sum(fixation_times)/len(fixation_times)
	avg_fix_times.append(average)
fig, ax_pop = plt.subplots()
ax_pop.scatter(population_sizes, avg_fix_times)
ax_pop.set_title("Average fixation time over 50 iterations for each of 5 population sizes")
ax_pop.set_xlabel("Population size")
ax_pop.set_ylabel("Average time to fixation (generations)")
fig.savefig( "pop-size-v-time-to-fixation.png" )


#avg fixation times over 10 iterations for each of 5 allele frequencies
frequencies = [.3, .77, .6, .2, .83]
vfreq_avg_fix_times = []
for frequency in frequencies:
	vfreq_fix_times = []
	for i in range(10):
		vfreq_output = wright_fisher(1001, i)
		vfreq_generation = vfreq_output[1]
		vfreq_fix_times.append(vfreq_generation)
fig, ax_freq = plt.subplots()
ax_freq.scatter(frequencies, avg_fix_times)
ax_freq.set_title("Average fixation time over 10 iterations for each of 5 allele frequencies")
ax_freq.set_xlabel("Frequency")
ax_freq.set_ylabel("Average time to fixation (generations)")
fig.savefig( "allele-freq-v-time-to-fixation.png" )


plt.show()
plt.close()


# please run the first submission/commit on GitHub to see the plot for the first exercise. (sorry)


# 4. QUESTION 1:
# 	PLOT: Frequencies over time, multiple iterations
# 		Each line/color shows the change in allele frequency over generations until the gene disappears from (reaches zero) or becomes fixed in the population (reaches one).
# 	HISTOGRAM:
# 		This histogram shows that lower allele frequency is associated with faster time to elimination or fixation. 

# 4. QUESTION 2: 
# 	ASSUMPTION 1:
# 		The Wright-Fisher model assumes that there is no selection or random mating, which is not true in nature. 
#		Natural selection may prefer one allele (that contributes to survival) and fixation would happen much faster. Most if not all frequencies would end up at one. 
#		If nature selects against an allele (if the allele puts the an individual in danger), this allele is more likely to disappear. Most if not all frequencies would end up at zero. 
# 	