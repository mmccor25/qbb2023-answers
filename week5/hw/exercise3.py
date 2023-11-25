#!/usr/bin/env python

read_depths = []
genotype_qualities = []
allele_frequencies = []
lof_count = 0
nmd_count = 0

for line in open("final.vcf"):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')

    # grab what you need from fields

    for sample in [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
        info = list(fields[sample].split(":"))
        GT = info[0]
        if GT == '1' or GT == '0':
            if len(info) > 1:
               
                DP = info[2] # read depth
                if "," in DP:
                    DP = list(DP.split(","))
                    for i in range(len(DP)):
                        read_depths.append(DP[i])
                else:
                    read_depths.append(DP)

                GQ = info[1] # genotype quality
                if "," in DP:
                    GQ = list(GQ.split(","))
                    for i in range(len(GQ)):
                        genotype_qualities.append(GQ[i])
                else:
                    genotype_qualities.append(GQ)

                # AD
                # RO
                # QR
                # AO
                # QA
                # GL
    # Allele frequencies
    variant_info = fields[7]
    variant_info = list(variant_info.split(";"))
    AF = variant_info[3][3:]
    if "," in AF:
        AF = list(AF.split(","))
        for i in range(len(AF)):
            allele_frequencies.append(float(AF[i]))
    else:
        allele_frequencies.append(float(AF))

    # Loss of function and nonsense mediated decay effects

    for i in variant_info:
        if "LOF" in i:
            lof_count += 1
        if "NMD" in i:
            nmd_count += 1


# Convert strings to numbers
for i in range(len(read_depths)):
    read_depths[i] = int(read_depths[i])

for i in range(len(genotype_qualities)):
    genotype_qualities[i] = float(genotype_qualities[i])

for i in range(len(allele_frequencies)):
    allele_frequencies[i] = float(allele_frequencies[i])



# # PLOTS
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

# histogram of read depth distribution
ax[0,0].hist(read_depths, bins=50, range=(0, 50))
ax[0,0].set_title("Read depth distribution")
ax[0,0].set_xlabel("Read depth")

ax[0,1].hist(genotype_qualities, bins=20, range=(0, 200))
ax[0,1].set_title("Genotype quality distribution")
ax[0,1].set_xlabel("Genotype quality")

ax[1,0].hist(allele_frequencies, bins=20, range=(0, 2))
ax[1,0].set_title("Allele frequency spectrum")
ax[1,0].set_xlabel("Allele frequency")

ax[1,1].bar(['LOF', 'NMD'], [lof_count, nmd_count], color=['red', 'blue'])
ax[1,1].set_title("Effect types")


fig.tight_layout()
fig.savefig( "week5_exercise3.png")

