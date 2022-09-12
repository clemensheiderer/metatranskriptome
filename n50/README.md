#implement a N50/L50 calculator in the programming language of your choice. The input for the program is a multiple-FASTA file of the contig sequences 
                                 use "n50.py --help" for more information


                                    libraries needed:
                                                    numpy
                                                    argparse


                                     terminal example:n50.py n50example.fna -N -L



N50         L50

positional arguments:
  fastafile

optional arguments:
  -h, --help            show this help message and exit
  -N, --N50
                            load it with:filename.py multiple_fasta_file.fna -N

                            Calculates N50

  -L, --L50
                            load it with: filename.py multiple_fasta_file.fna -L

                            Calculates L50

  -s, --sequence_lengths_list

                            load it with: filename.py multiple_fasta_file.fna -s

                            Output of list with sorted sequence lengths

