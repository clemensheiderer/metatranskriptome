#Implement a coverage calculator (based on the Lander-Waterman formula) in the programming language of your choice 



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

positional arguments:
  fastafile

optional arguments:
  -h, --help            show this help message and exit
  -l [READ_LENGTH], --read_length [READ_LENGTH]

                                                                                                            for -l default value is set to 1000,
                                                                                                            or set a value behind the flag -l
                                                                                                            like: filename.py fastafile.fna -o -l 300
                                                                                                            for illumina
  -o [OVERLAP], --overlap [OVERLAP]

                                                                                                        overlap is a float in percentage
                                                                                                        value size should be below 1.0!
                                                                                                        for -o default value is set to 0.35
                                                                                                        or set a value behind the flag -o
                                                                                                        like: filename.py fastafile.fna -l -o 0.45
  -n, --number_of_reads

                            load it with:filename.py fastafile.fna -l -o -n

                            for calculation of number of reads it uses: coverage = length_of_reads • number_of_reads
                                                                                   ─────────────────────────────────
                                                                                       genomesize in bp



  -g, --graph           flag -f
                            load it with: filename.py fastafile.fna -l -o -n -g

                            set a limit for the x-axis:
                                                        for default example with a genome of 1 million bp, set limit to 20

                            plots line with expected islands as y-axis and
                                       coverage as x-axis



  -t, --tag             flag -t
                            load it with: filename.py fastafile.fna -l -o -n -t

                            accession number + tax name

