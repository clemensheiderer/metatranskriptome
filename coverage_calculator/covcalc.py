import argparse
import math
import numpy as np
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="""

⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆

coverage calculator based on Lander-Waterman


generates coverage values as x-axis with 0.1 steps
generates expected islands as contigs as y-axis

for calculation of y-values it uses:

                                                                      (-1-theta) coverage
                                    genome_size  • coverage  •  euler 
                                    ─────────────────────────────────
                                            read_length

                                    interpolation: estimates a new coverage-data point 
                                                   assumes a contig of 1 ➺ output wanted coverage


⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆⑆      

""",
                                 usage="""use "%(prog)s --help" for more information

                                 python version 3.8 or higher
                                 
                                 arguments -o -l are minimum

                                 libraries needed: 
                                                    argparse
                                                    math
                                                    numpy
                                                    scipy
                                                    pandas
                                                    matplotlib
                                                    seaborn

                                     terminal examples: covcalc.py 1million.fna -o -l
                                                        covcalc.py 1million.fna -o 0.4 -l -o
                                                        covcalc.py 1million.fna -o -l -g
                                                                set x-axis limit: 20


                                     fastafile.fna is needed!


                                     """,
                                 formatter_class=argparse.RawTextHelpFormatter)

# parser.add_argument("-g", "--genomesize", nargs="?", const=1000000, type=int)
parser.add_argument("-l", "--read_length", nargs="?", const=1000, type=int, help="""
                                                                                    for -l default value is set to 1000, 
                                                                                    or set a value behind the flag -l
                                                                                    like: filename.py fastafile.fna -o -l 300
                                                                                    for illumina""")
parser.add_argument("-o", "--overlap", nargs="?", const=0.35, type=float, help="""
                                                                                overlap is a float in percentage
                                                                                value size should be below 1.0!
                                                                                for -o default value is set to 0.35
                                                                                or set a value behind the flag -o
                                                                                like: filename.py fastafile.fna -l -o 0.45""")

parser.add_argument("-n", "--number_of_reads", help="""
    load it with:filename.py fastafile.fna -l -o -n

    for calculation of number of reads it uses: coverage = length_of_reads • number_of_reads
                                                           ─────────────────────────────────
                                                               genomesize in bp


                      """, action="store_true")

parser.add_argument("-g", "--graph", help="""flag -f
    load it with: filename.py fastafile.fna -l -o -n -g

    set a limit for the x-axis: 
                                for default example with a genome of 1 million bp, set limit to 20

    plots line with expected islands as y-axis and
               coverage as x-axis


                      """, action="store_true")
parser.add_argument("-t", "--tag", help="""flag -t
    load it with: filename.py fastafile.fna -l -o -n -t
    
    accession number + tax name


                      """, action="store_true")




parser.add_argument('fastafile')
# fasta_file = int(fasta_file)
args = parser.parse_args()

# genome = args.genomesize

fasta_file = args.fastafile
read_length = args.read_length
theta = args.overlap
tag = args.tag



if args.read_length and args.overlap and args.fastafile:
    for_genome = ''
    tag = ''
    with open(fasta_file, 'r') as f:
        for line in f:
            if not line[0] == ">":
                for_genome += line.rstrip()
            if line[0] == ">":
                tag += line.rstrip()

    genome = len(for_genome)
    if args.tag:
        tag = tag.split()[0:3]
        tag = " ".join(tag)
        print(f"{tag}")


    coverage = []
    for ai in np.arange(0, 140.1, 0.1):
        coverage.append(ai)
    contigs = []
    for cov in coverage:
        contigs_reads = float(genome / read_length * cov * math.e ** (-(1 - theta) * cov))
        contigs.append(contigs_reads)
    import numpy as np
    from scipy import interpolate
    import matplotlib.pyplot as plt

    # Decreasing array
    x = coverage
    x = np.array(x)
    # print(x)
    y = contigs
    y = np.array(y)
    # print(y)

    f = interpolate.interp1d(y, x, assume_sorted=False)
    ynew = 1.0
    xnew = f(ynew)
    print(f"coverage: {xnew}")

    if args.number_of_reads:
        contig = xnew

        number_of_reads = contig * genome / read_length
        # print(number_of_reads)
        print(f"number of reads: {round(number_of_reads + 0.5)}")
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_theme(style="darkgrid")

    # if args.graph:

    if args.graph:
        df = pd.DataFrame(dict(coverage=x,
                               expected_islands=y))
        g = sns.relplot(x="coverage", y="expected_islands", kind="line", data=df)
        g.figure.autofmt_xdate()
        coverage_input = float(input(f"set x-axis limit: \n"))
        g.set(xlim=(0, coverage_input))
        plt.annotate("•", (xnew, ynew), color='purple')

        plt.show()









