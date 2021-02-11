import numpy as np
import math 
# for reading input text file

f=open("file2.txt", "r")
contents =f.read()

#the below code def is to convert string in text file to an array of elements
def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 
F=Convert(contents)
#converting to ascii numbers
asc = [] 
for i in F: 
    asc.extend(ord(num) for num in i)

print("number of characters ",len(asc))

# below def code is for function to count number of times an alphabet is repeated i.e no of a's in given text likewise.
def counter(s): 
    # starting count
    count=np.zeros(256)
    for i in range(len(s)):
	    if s[i]<=255:
             count[s[i]]=count[s[i]]+1
    # returning emperical frequency 
    return count/len(s)
    
# I have taken help from Chaitanya varun(EE19BTECH11040) in method of computing the below def.
#Below method in comments is mine but it is taking a lot of time.
#def countnew(s): 
 #   snew=[]
 #   for i in range(len(s)-1):
#	    snew+=[(s[i],s[i+1])]  
#    # starting count
#    countnew = np.zeros([256,256])
    # running loop to all iterations
#    for i in range(256):
#        for j in range(256):
 #         countnew[i,j]=snew.count((i,j))
 #   return countnew/len(s)
       
def countnew(s): 
    # starting count
    countnew = np.zeros([256,256])
    # running loop to all iterations
    for i in range(len(s)-1):
        if s[i]<=255 and s[i+1]<=255:
            countnew[s[i],s[i+1]]=countnew[s[i],s[i+1]]+1
            #returning emperical vector
    return countnew/(len(s)-1)
    
    #entropy function
def Entropy(X):
	Y=0
	L= X.flatten()	
	for i in range(len(L)):
		if L[i]==0:
			Y+=0
		else:
			Y+=(L[i]*math.log(L[i],2))
	Entropy = -Y
	return Entropy	 
Fi = len(asc)*Entropy(counter(asc))/8   
Fi2 = len(asc)*(Entropy(countnew(asc))-Entropy(counter(asc))) /8   
print("Entropy is ",Entropy(counter(asc)))
#1.6012295668131133 for inputfile
# 4.430243055846827 is the value for file2
	
print("Joint Entropy is ",Entropy(countnew(asc)))
#3.2017144531397204 for input file
#7.85849078068437 is the value for file2

print("Conditional Entropy is ",Entropy(countnew(asc))-Entropy(counter(asc)))
#1.600484886326607 for input file
# 3.4282497202670417 is the value for file2

print("Optimized file size ideally is",Fi)
#2001.5369585163917 for input file
#1787371.0390541446 for file2

print("Optimized file size ideally using conditional entropy is",Fi2)
#2000.6061079082588 for input file
#1383119.2075486523 for file2
