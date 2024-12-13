#read its contents
file=open('mahi.txt','r')
print(file.read())
file.close()


#read only the first 17 characters
file=open('mahi.txt','r')
print(file.read(17))
file.close()



#appened name to the file
file=open('mahi.txt','a')
file.write('mahi')
file.close()


file=open('mahi.txt','r')
print(file.read())
file.close()