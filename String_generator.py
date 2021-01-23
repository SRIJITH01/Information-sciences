import numpy as np
import sys

# first we will generate num_trial samples
num_trial = int(input("Enter num_trial:"))

X = np.random.rand(num_trial)
#defining strings a,b,c,d.
[a,b,c,d]=["a","b","c","d"]

pa = 0.010239712433255
#pa= float(input("Enter probability of a:")) we can also use this to input our pa from terminal
print(" Probability of a:",pa)
pb= 0.330838389686104

print(" Probability of b:",pb)
pc= 0.62480072865356

print("Probability of c:",pc)
pd= 0.034121169227081

print("Probability of d:",pd)

#the below loop maps uniform random numbers to a,b,c,d with their respective probability and generates output string
F=""
for i in range(num_trial):
	if X[i] <= pa:
		F+=a
	elif	pa<X[i]<=(pb+pa):
		F+=b
	elif (pa+pb)<X[i]<=(pb+pa+pc):
	   F+=c
	else:
		F+=d
# write comments

print("Output sequence is",F) 

#now we print output to a text file. 
sys.stdout = open("output.txt", "w")

print(F) 

sys.stdout.close()
