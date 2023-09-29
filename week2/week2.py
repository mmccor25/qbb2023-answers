#!/usr/bin/env python

# EXERCISE 1


# Making simulation
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def simulate_coverage(coverage, genome_len, read_len, figname):
	coverage_array = np.zeros(genome_len)
	num_reads = int(coverage*genome_len/read_len)
	low = 0
	high = genome_len - read_len

	start_positions = np.random.randint(low = 0, high = high + 1, size = num_reads)
		# High is exclusive

	for start in start_positions:
		coverage_array[start: start + read_len] +=1

	x = np.arange(0, max(coverage_array)+1)
		# creates a range of numbers from thing to thing (from zero to the highest number seen in coverage_array)

	sim_0cov = genome_len - np.count_nonzero(coverage_array)
		# counts number of zeroes

	sim_0cov_pct = 100*sim_0cov / genome_len

	print(f'In the simulation, there are {sim_0cov} bases with zero coverage.')
	print(f'This is {sim_0cov_pct}% of the genome.')


	# compare our histogram with the poisson distribution
	y_poisson = stats.poisson.pmf(x, mu = coverage)*genome_len
		# probability that the distribution produces that number
		# mean coverage is the coverage we are targeting
		# x represents all the possible coverages we can see in our simulation
		# area under curve should be the size of genome


	# normal distribution - can't use 1 number (likleyhood), need to use a range (probability)
	y_normal = stats.norm.pdf(x, loc = coverage, scale = np.sqrt(coverage)) * genome_len # multiply by genome length to get it on the same scale as our graph


	fig, ax = plt.subplots()
	ax.hist(coverage_array, bins = x, label = 'Simulation', align = 'left') # align is just to make it look nice
	ax.plot(x, y_poisson, label = 'Poisson')
	ax.plot(x, y_normal, label = 'Normal')
	ax.set_title("Read frequencies with 3x target coverage")
	ax.set_xlabel('Coverage')
	ax.set_ylabel('Frequency (bp)')
	ax.legend()
	fig.tight_layout()
	fig.savefig(figname)
	

	

	plt.show()
	plt.close()



simulate_coverage(3, 1_000_000, 100, 'ex1_3x_cov.png')



# EXERCISE 2
# 2.1
reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

k = 3
edges = []
for read in reads:
	for i in range(len(read)-k):
		kmer1 = read[i: i+k]
		kmer2 = read[i+1: i+k+1]
		edges.append(str(kmer1 + '->' + kmer2))

print(edges)

# 2.2
# type this in the command line in terminal (in bash)
	# $ conda create -n graphviz -c conda-forge graphviz
	# $ conda activate graphviz
# 2.3
# made a text file and copied list of edges