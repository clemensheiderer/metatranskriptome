from Bio import Entrez, SeqIO
import regex as re

Entrez.email = "clemensh@yandex.com"
#http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec33
#http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec38


handle = Entrez.efetch(db="nucleotide", id="CP009685", rettype="gb", retmode="text")


readline = handle.read().splitlines()

print("regex from main page: Entrez handle\n")
for read in readline:
    if re.search('Features Annotated', read):
        print(read)
    if re.search('CDS[^\S]+::', read):
        print(read)
    if re.search('Genes[^\S]+::', read):
        print(read)
    if re.search('CRISPR Arrays[^\S]+::', read):
        print(read)
    if re.search('rRNAs[^\S]+::', read):
        print(read)
    if re.search('tRNAs[^\S]+::', read):
        print(read)
    if re.search('ncRNA[^\S]+::', read):
        print(read)

handle = Entrez.efetch(db="nucleotide", id="CP009685", rettype="gbwithparts", retmode="text")
record = SeqIO.read(handle, "genbank")

all_cds = 0
k = 0
counts = {}
for feature in record.features:
    c = feature.type
    if c not in counts:
        counts[c] = 0
    counts[c] +=1

print(f"\n")
print(f"from  record.features: \n")
for k, v in counts.items():
    print(f"{k}: {v}")
print(f"\n")

for feature in record.features:
    if feature.type == "CDS":
        print(f" position: {feature.location} \t  id: {feature.qualifiers['protein_id'][0]} \t {feature.qualifiers['product'][0]} \t bp length: {len(feature.qualifiers['translation'][0])}")
    if feature.type == "rRNA":
        print(f" position: {feature.location} \t \t {feature.qualifiers['product'][0]} ")
    if feature.type == "tRNA":
        print(f" position: {feature.location} \t \t {feature.qualifiers['product'][0]} ")
    if feature.type == "ncRNA":
        print(f" position: {feature.location} \t \t {feature.qualifiers['product'][0]} ")
    if feature.type == "gene":
        print(f" position: {feature.location} \t gene locus tag: {feature.qualifiers['locus_tag'][0]}")


'''
type: gene
location: [4635154:4636426](-)
qualifiers:
    Key: locus_tag, Value: ['EO53_22925']


type: gene
location: [4634120:4635125](+)
qualifiers:
    Key: gene, Value: ['dppF']
    Key: locus_tag, Value: ['EO53_22920']
'''
