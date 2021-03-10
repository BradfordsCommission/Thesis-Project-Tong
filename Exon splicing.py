#First define the sequence and store it
Sequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#next, throw in the predefined sequence regions

Exon_One = 63
Exon_Two = 91

#then print out the coding region of the DNA
print("Coding DNA: " + Sequence[0:Exon_One] + " (intron) " + Sequence[Exon_Two:])

#now, let's get the length of the sequence and store it
Sequence_Length = len(Sequence)

#cool, now pump out the % of the sequence that makes up the coding sequence from the overall sequence
Coding_Length = len(Sequence[0:Exon_One] + Sequence[Exon_Two])

CodingODNA = Coding_Length/Sequence_Length*100

print("% coding: " + str(CodingODNA))

#now for something completely different
#going to have to make the coding sequence upper case, and the non coding lower case
#string is already in upper case so that's done.
#now make the non coding lower case

#store non coding into a variable
Non_Coding = Sequence[Exon_One:Exon_Two]

#change it to lower case
Non_Coding_Lower = Non_Coding.lower()

#spit it out, with coding in upper case (which it is)
print(Sequence[0:Exon_One] + Non_Coding_Lower + Sequence[Exon_Two:])

#Going to make a text file to store the coding sequence into, and the non coding sequence into another
Coding_File_Name = "Coding Sequence.txt"
Coding_File = open(Coding_File_Name, "w")
Coding_File.write(Sequence[0:Exon_One] + Sequence[Exon_Two])
Coding_File.close()

Non_Coding_File_Name = "Non_Coding_Sequence.txt"
Non_Coding_File = open(Non_Coding_File_Name, "w")
Non_Coding_File.write(Non_Coding)
Non_Coding_File.close()


#cool, now read them
Coding_File_Name = "Coding Sequence.txt"
Coding_File = open(Coding_File_Name)
Coding_File_Text = Coding_File.read()

Non_Coding_File_Name = "Non_Coding_Sequence.txt"
Non_Coding_File = open(Non_Coding_File_Name)
Non_Coding_File_Text = Non_Coding_File.read()

#print?

print("coding: " + Coding_File_Text + "\n" + "and non coding: " + Non_Coding_File_Text)

Coding_File.close()
Non_Coding_File.close()

