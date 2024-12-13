file=open('mahi.txt','r')
print(file.read())
file.close()


#read only the first 7 lines
file=open('mahi.txt','r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open('mahi.txt','r')
for line in file:
    print(line)


file.close()



