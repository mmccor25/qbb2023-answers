#!/usr/bin/env python

import sys

from model_peaks import load_bedgraph, bin_array
import numpy
import scipy.stats
import matplotlib.pyplot as plt


def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, frag_width, out_fname = sys.argv[1:5]
    frag_width = int(frag_width)
    wig_name = out_fname + "_peaks.wig"
    bd_name = out_fname + "_peaks.bed"

    # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart


    # Load the sample bedgraph data, reusing the function we already wrote
    forward = load_bedgraph(forward_fname, chrom, chromstart, chromend)
    reverse = load_bedgraph(reverse_fname, chrom, chromstart, chromend)

    # Combine tag densities, shifting
    combined = numpy.zeros(chromlen, int) # array saved in sample
    combined[:-frag_width//2] = reverse[frag_width//2:] 
    combined[frag_width//2:] += forward[:-frag_width//2]

    # Load the control bedgraph data, reusing the function we already wrote
    fwd_control = load_bedgraph("control.fwd.bg", chrom, 0, chromlen)
    rev_control = load_bedgraph("control.rev.bg", chrom, 0, chromlen)

    # Combine tag densities
    # fwd_control = fwd_control[99:]
    # rev_control = rev_control[:-99]
    combined_control = fwd_control + rev_control

    # Adjust the control to have the same coverage as our sample
    norm_factor = numpy.sum(combined)/numpy.sum(combined_control)
    combined_control = combined_control*norm_factor

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base
    background_scores = bin_array(combined_control, 1000)/1000
    background_mean = numpy.mean(background_scores)

    # Find the mean tags/bp and make each background position the higher of 
    # the binned score and global background score
    background_scores = numpy.maximum(background_scores, background_mean)

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote
    scores = bin_array(combined, 2*frag_width)

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background
    background_scores = background_scores*2*frag_width
    
    cdf = scipy.stats.poisson.cdf(scores, background_scores)
    p_values = 1 - cdf

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    p_values = numpy.maximum(1e-250, p_values)
    p_values = -(numpy.log(p_values))

    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"
    write_wiggle(p_values,chrom, chromstart, wig_name)

    # Write bed file with non-overlapping peaks defined by high-scoring regions 
    write_bed(p_values, chrom, chromstart, chromend, frag_width, bd_name)



def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()