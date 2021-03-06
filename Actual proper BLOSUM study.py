#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install biopython')


# In[ ]:


from Bio import pairwise2
from Bio import SeqIO
from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")
seq1 = SeqIO.read("alpha.faa","fasta")
seq2 = SeqIO.read("beta.faa","fasta")
alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum62, -10, -0.5)
len(alignments)

