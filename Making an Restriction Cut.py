#gonna cut out a part of the sequence, first to store the sequence
Sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#Then, going to find the ECORI sequence, and store the position number
Restriction_Motif_Position = Sequence.find('GAATTC')

#cool, now we are going to give the cut position: all this is, is the motif position, plus one
Restriction_Motif_Cut = Restriction_Motif_Position + 1

#now we will print from the restriction site, in the forwards and backward direction
print("The enzyme will cleave here: " + Sequence[0:Restriction_Motif_Cut] + " (cut) " + Sequence[Restriction_Motif_Cut:]) 
