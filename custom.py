import pandas as pd
import cv2
import fnmatch,os
from PIL import Image

import numpy as np

listoffiles=os.listdir('.')
pattern="*.jpg"

#change custom.csv to the appropriate file name
df=pd.read_csv("custom.csv",delimiter=",")
#print(df)

prev=0
tuples=[tuple(x) for x in df.values]


for i in range (len(tuples)):
	tuples[i]=list(tuples[i])
#convert class names to class labels
#Articulated Truck=0
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

	t=str(tuples[i][0]).rjust(8,'0')+".jpg"
	try:
		im=Image.open(t)
		w,h=im.size
	except IOError:
		continue
	
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

	#padds leading zeros 	
	if prev == tuples[i][0]:
#opens last modified file in append mode, when single image has multiple object class
		f= open(str(tuples[i-1][0])+"."+"txt", 'a')
		dw = 1./w
		dh = 1./h
		x = (tuples[i][2]+tuples[i][4])/2.0
		y = (tuples[i][3]+tuples[i][5])/2.0
		w = abs(tuples[i][4]-tuples[i][2])
		h = abs(tuples[i][3]-tuples[i][5])
		x = x*dw
		w = w*dw
		y = y*dh
		h = h*dh
		newTuple=(tuples[i-1][1],x,y,w,h)
		f.write(' '.join(str(s) for s in newTuple))
		f.write("\n")
		f.close()
	else:
#opens a new file 
		f= open(str(tuples[i][0])+"."+"txt", 'w')
		dw = 1./w
		dh = 1./h
		x = (tuples[i][2]+tuples[i][4])/2.0
		y = (tuples[i][3]+tuples[i][5])/2.0
		w = abs(tuples[i][4]-tuples[i][2])		
		h = abs(tuples[i][3]-tuples[i][5])
		x = x*dw
		w = w*dw
		y = y*dh
		h = h*dh
		newTuple=(tuples[i][1],x,y,w,h)
		f.write(' '.join(str(s) for s in newTuple))
		f.write("\n")
		f.close()
	#cv2.rectangle(image,(int(tuples[i][2]),int(tuples[i][3])), (int(tuples[i][4]),int(tuples[i][5])),(255,255,255),3)
	#cv2.imwrite(t+"dup1"+".jpg",image)

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
