import numpy as np
import argparse

parser = argparse.ArgumentParser(description='N50         L50',
                                 usage="""
                                 
                                 
                                 use "%(prog)s --help" for more information
                                 
                                 
                                    libraries needed:
                                                    numpy
                                                    argparse
                                                    

                                     terminal example:n50.py n50example.fna -N -L


                                     """,
                                 formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('fastafile')

parser.add_argument("-N", "--N50", help="""
    load it with:filename.py multiple_fasta_file.fna -N

    Calculates N50
                      """, action="store_true")
parser.add_argument("-L", "--L50", help="""
    load it with: filename.py multiple_fasta_file.fna -L

    Calculates L50
                      """, action="store_true")
parser.add_argument("-s", "--sequence_lengths_list", help="""
    load it with: filename.py multiple_fasta_file.fna -s

    Output of list with sorted sequence lengths

                      """, action="store_true")

args = parser.parse_args()

fasta_seq_list = [f.strip() for f in open(args.fastafile).readlines()]

#fasta_seq_list = [f.strip() for f in open(sys.argv[1]).readlines()]





if args.N50:
    multiple_fasta_dict = {}
    for line in fasta_seq_list:
        # if not line:
        # continue
        if line[0] == '>':
            reads = line
            if reads not in multiple_fasta_dict:
                multiple_fasta_dict[line] = ''
            continue
        multiple_fasta_dict[reads] += line

    len_multiple_fasta_dict = {}

    for k, v in multiple_fasta_dict.items():
        len_multiple_fasta_dict[k] = int(len(v))

    best_list = np.fromiter(len_multiple_fasta_dict.values(), dtype=int)

    fasta_len_sorted = np.sort(best_list)[::-1]


    #print(fasta_len_sorted)
    tag = len(fasta_len_sorted)
    #print(tag)

    nldk = fasta_len_sorted[fasta_len_sorted >= np.sum(fasta_len_sorted / 2)]

    nldk = np.array([])

    for a in fasta_len_sorted:
        nldk = np.append(nldk, a)
        if np.sum(nldk) >= np.sum(fasta_len_sorted / 2):
            break

    n50 = nldk[-1]



    print(f"N50: {n50}")
    if args.L50:
        l50 = len(nldk)
        print(f"L50: {l50}")
    if args.sequence_lengths_list:
        print(f"sequences numbers for L50: {nldk}")




