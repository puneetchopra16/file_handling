#Question1


f=open('file1.txt','r')
file=f.read()
print(file)
f.close()
print()


#Question2


f=open("file1.txt",'r')
data=f.read()
words=data.split()
dict={}
for i in words:
    dict[i]=words.count(i)
print(dict)
print()


#Question3


f=open("file1.txt",'r')
g=open("file2.txt",'w')
for i in f:
    g.write(i)
f.close()
g.close()
print()


#Question4


f1=open("file1.txt",'r')
f2=open("file3.txt",'r')
for i1,i2 in zip(f1,f2):
    f3=open("file5.txt",'a')
    f3.write(i1+i2)
    f3.close()
f2.close()
f1.close()
print()


#Question5


f5=open('file1.txt')
temp=open('file4.txt','w+')
sor=f5.readlines()
sor.sort()
temp.write(str(sor))
temp.seek(0)
output=temp.read()
print(output)
print()
