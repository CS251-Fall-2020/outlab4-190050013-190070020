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

data[:,0] = tpm
data[:,1] = tpr

fields = ['Day', 'Tests per Million', 'Test Positivity rate', 'Recovered', 'Deceased']
filename = "transformed.csv"

with open(filename, 'w') as csvfile:  
	csvwriter = csv.writer(csvfile)  
	csvwriter.writerow(fields)      
	for row_title, data_row in zip(row_headers, data):
		csvwriter.writerow([row_title] + data_row.tolist())
