#fetching the file from my computer, and telling the file that i'd like to write something in it
DNA_File_Name = "DNA.txt"
DNA_File = open(DNA_File_Name, "w")

#the text I'm filling the file with
DNA_File.write("Writing code is not hard")
DNA_File.close()
