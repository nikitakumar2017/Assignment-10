#Q.1- Write a Python program to read n lines of a file.
f=open('file1.txt','r')
n=int(input("Enter n less than equal 5"))
for i in range(0,n):
    lines=f.readline()
    print(lines)
f.close()

#Q.2- Write a Python program to count the frequency of words in a file.
f=open('file1.txt','r')
words=(f.read()).split()
count=1
i=0
checklist=[]
for j in range(0,len(words)):
    count=1
    word=words[i]
    if word in checklist:
            pass
    else:
        for l in range(0,len(words)):
            if (i==l):
                pass
            elif (word==words[l]):
                count+=1
        print("Frequency of",word,"is",count)
        checklist.append(word)     
    i+=1
f.close()

#Q.3- Write a Python program to copy the contents of a file to another file.
f1=open('file1.txt','r')
data=f1.read()
f2=open('file2.txt','w')
f2.write(data)
f1.close()
f2.close()


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
f3=open('file3.txt','r+')
f1=open('file1.txt','r')
f2=open('file2.txt','r')
for line1, line2 in zip(f1, f2):
        print(line1+line2)


#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
temp=0
f3=open('file3.txt','r+')
for i in range(10):
    num=random.random()
    f3.write(str(num))
    f3.write('\n')
numbers=f3.readlines()
for i in range(0,10,1):
    for j in range(0,9-i,1):
        if(numbers[j]>numbers[j+1]):
            temp=numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]=temp
f4=open('file4.txt','w')
for i in numbers:
    f4.write(i)
    f4.write('\n')
f4.close()
f3.close()


