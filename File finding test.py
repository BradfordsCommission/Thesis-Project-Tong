#This is for finding a file on your computer
My_File_Name = "Find Me.txt"
My_File = open("C:/Users/Robert/Robert Bradford/At University/2020-university fourth year second semester/Bioinformatics/Primary project/Thesis Project Files/Python Files Thesis/Find Me.txt", "w")
My_File_Contents = My_File.read()

print(My_File_Contents)
My_File.close()
