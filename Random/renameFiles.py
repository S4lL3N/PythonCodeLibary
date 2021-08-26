"""
https://docs.python.org/3/library/os.html
https://www.youtube.com/watch?v=ve2pmm5JqmI&list=PLUQrv8O3kWHu49FidJFotE6OafwMECl-F&index=37&t=5s
"""
import os 

#changes the directory
os.chdir(r'C:\Users\S4lL3\Documents\My_VS_Code\Python')

#gets the current directory
currentDir = os.getcwd()
print(currentDir)

#will list all the files in the directory
for file in os.listdir():
    print(file)
    #creates a tuple out of the file seperating the file name from the file extention.
    file_name, file_ext = os.path.splitext(file)
    print(f'file name: {file_name}')

    #splits the file name, and reformats the filename to the format below
    #f_num, f_title, f_course = file_name.split("/")
    #new_name = '{}-{}-{}{}'.format(f_num, f_title, f_course, file_ext)
    #os.rename(f,new_name)

