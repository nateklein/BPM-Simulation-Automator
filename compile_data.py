import fnmatch
import os
import shutil
import datetime

name = str(input("Name: "))

outputs = []

for file in os.listdir(r'E:\SRP\IREAP 2019\Simulation Data'):
	if fnmatch.fnmatch(file, '*.dsp'):
		outputs.append(file)

data = open("sim_data.csv", "a")

now = datetime.datetime.now()
direc = r"E:\SRP\IREAP 2019\Simulation Data\\"+name+" "+str(now.year)+"_"+str(now.month)+"_"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)
os.mkdir(direc)

for i in outputs:

	f = open(i, "r")
	x = i.split("_")[2]
	y = i.split("_")[3][:-4]

	# Get to the correct line
	line = f.readline()
	while "ElemSolution" not in line:
		line = f.readline()
	f.close()

	# Strip the beginning and end of the line and put all the voltages into an array
	line = line[16:-2]
	voltages = list(map(float, line.split(", ")))
	while voltages[0] != voltages[1]:
	    voltages.pop(0)

	# Get the 4 plate voltages
	plate_voltages = []
	plate_voltages.append(voltages[0])

	for i in range(len(voltages)-1):
		if voltages[i] != voltages[i+1]:
			plate_voltages.append(voltages[i+1])
		
	# Write the 4 voltages to the master data file
	data.write("\n"+x+","+y+","+",".join(map(str, plate_voltages)))
	shutil.move(i, direc)

data.close()
