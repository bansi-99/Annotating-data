import pandas as pd

#change custom.csv to the appropriate file name
df=pd.read_csv("custom.csv",delimiter=",")
print(df)

prev=0
tuples=[tuple(x) for x in df.values]

for i in range (len(tuples)):
	tuples[i]=list(tuples[i])
#convert class names to class labels
# Articulated Truck=0
#Bicycle=1
#bus=2
#car=3
#Motorcycle=4
#motorized vehicle=5
#non-motorized vehicle=6
#pedestrian=7
#pickup truck=8
#single unit truck=9
#work van=10

	if (tuples[i][1]=="articulated_truck"):
		tuples[i][1]=0
	elif (tuples[i][1]=="bicycle"):
		tuples[i][1]=1
	elif (tuples[i][1]=="bus"):
		tuples[i][1]=2

	elif (tuples[i][1]=="car"):
		tuples[i][1]=3

	elif (tuples[i][1]=="motorcycle"):
		tuples[i][1]=4
	elif (tuples[i][1]=="motorized_vehicle"):
		tuples[i][1]=5
	elif (tuples[i][1]=="non-motorized_vehicle"):
		tuples[i][1]=6
	elif (tuples[i][1]=="pedestrian"):
		tuples[i][1]=7
	elif (tuples[i][1]=="pickup_truck"):
		tuples[i][1]=8
	elif (tuples[i][1]=="single_unit_truck"):
		tuples[i][1]=9
	elif (tuples[i][1]=="work_van"):
		tuples[i][1]=10
	else:
		print("Unknown class")



	if prev == tuples[i][0]:
#opens last modified file in append mode, when single image has multiple object class
		f= open(str(tuples[i-1][0])+"."+"txt", 'a')
		f.write(' '.join(str(s) for s in tuples[i]))
		f.write("\n")
		f.close()
	else:
#opens a new file 
		f= open(str(tuples[i][0])+"."+"txt", 'w')
		f.write(' '.join(str(s) for s in tuples[i]))
		f.write("\n")
		f.close()

	prev=tuples[i][0]


'''
#to read a file

f=open("1.txt","r")
x=f.readline()
print(x)
y=x.split()
print(y)

print(type(f.readline()))
'''
