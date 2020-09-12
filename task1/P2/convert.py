import numpy as np
import csv

np.set_printoptions(suppress=True)

data = np.loadtxt('mumbai_data.csv', usecols=range(1,5), skiprows=1, delimiter=',')
row_headers = np.loadtxt('mumbai_data.csv', usecols=0, skiprows=1, delimiter=',', dtype = "object")

tpr = data[:,1]/data[:,0]
for i in range(tpr.size):
	tpr[i] = format(tpr[i], '.3f')

tpm = data[:,0]/(20.4)
tpm = tpm.astype(np.int32)

data = np.int32(data)
fields = ['Day', 'Tests per Million', 'Test Positivity rate', 'Recovered', 'Deceased']
filename = "transformed.csv"

with open(filename, 'w') as csvfile:  
	csvwriter = csv.writer(csvfile)  
	csvwriter.writerow(fields)      
	for row_title, tm, tr, data_row in zip(row_headers, tpm, tpr, data[:,2:]):
		csvwriter.writerow([row_title] + [tm] + [tr] + data_row.tolist())
