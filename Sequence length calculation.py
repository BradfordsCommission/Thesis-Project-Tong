#store the DNA sequence into a variable to calculate, named "Sequence"
Sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#get the sequence length, and store that number into a variable
A_Count = Sequence.count('A')
T_Count = Sequence.count('T')
C_Count = Sequence.count('C')
G_Count = Sequence.count('G')

Sequence_Length = A_Count + T_Count + C_Count + G_Count
#check the length
print(str(Sequence_Length))

#then, grab the %A content, and %T content, store these
A_Content = A_Count/Sequence_Length*100
T_Content = T_Count/Sequence_Length*100

#then read out the %A and T content
print("The percent A content is " + str(A_Content) + "% and the percent T content is " + str(T_Content) + "% !") 
