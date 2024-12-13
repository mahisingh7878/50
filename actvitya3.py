#Write a Python program to remove lines of a file starting with prefix - Coding and store the contents in a new file
#and store the contents in anew file

file1=open('mahi.txt','r')
file2=open('upmahi.txt','w')


for line in file1:
    if not(line.startswith('nature')):
        file2.write(line)


file1.close()
file2.close()