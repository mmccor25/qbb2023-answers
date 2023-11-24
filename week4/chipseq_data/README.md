command for sample1
	$ python find_peaks.py sample1.fwd.bg sample1.rev.bg 198 sample1
command for sample2
	$ python find_peaks.py sample2.fwd.bg sample2.rev.bg 198 sample2

COUNTS:
	sample1_peaks.bed: 598
	sample2_peaks.bed: 618
	combined_peaks.bed: 624
	Total peaks = 598 + 618 = 1216
	Fraction of peaks in common: 51.3%

STEP 3 Answer:
The peaks are moderately reproducible, since only about half of the peaks were shared by both samples. However, looking at the IGV plot, it seems that there is consistency in the regions of DNA where the peaks cluster. 

The higher peaks have a smaller p-value, since we are less likely to observe peaks of this height by chance. The taller peaks seem to correspond the most across the two samples, so lower p-value correlates with higher reproducibility. However, this pattern is not completely consistent because there are some many small peaks that match between the two samples, as well as some larger peaks that do not. 