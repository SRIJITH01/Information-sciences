import numpy as np

# for reading input text file

f=open("inputfile.txt", "r+")
contents =f.read()


#the below code def is to convert string in text file to an array of elements
def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 
F=Convert(contents)


#defining alphabet set X
X = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z] = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



# below def code is for function to count number of times an alphabet is repeated i.e no of a's in given text likewise.
def count(s,a): 
  
    # starting count
    count = 0 
  
    # running loop to all iterations
    for i in range(len(s)): 
        if  s[i]==a:
           count = count +1
        else :
          count = count
  
    # returning emperical frequency 
    return count/len(s)  
       
 # now counting all alphabets and sending their emperical frequency to 26-length vector
Out=[]
for i in range(len(X)):
	Out+=[count(F,X[i])]

print("Emperical PMF vector is",Out)

# output that will be obtained for given input  PMF of emperical frequency is [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2201, 0.0, 0.0266, 0.0, 0.1264, 0.0, 0.595, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0319, 0.0, 0.0]

