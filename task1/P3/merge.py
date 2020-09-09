import numpy as np
import csv

np.set_printoptions(suppress=True)

data_lock = np.loadtxt('mumbai_data.csv', usecols=range(1,5), skiprows=1, delimiter=',')
data_unlock = np.loadtxt('mumbai_unlock.csv', usecols=range(1,5), skiprows=1, delimiter=',')
row_headers = np.loadtxt('mumbai_data.csv', usecols=0, skiprows=1, delimiter=',', dtype = "object")

tpr_lock = data_lock[:,1]/data_lock[:,0]
for i in range(tpr_lock.size):
	tpr_lock[i] = format(tpr_lock[i], '.3f')

tpr_unlock = data_unlock[:,1]/data_unlock[:,0]
for i in range(tpr_unlock.size):
	tpr_unlock[i] = format(tpr_unlock[i], '.3f')

infected_lock = data_lock[:,1]
infected_unlock = data_unlock[:,1]

fields = ['Day', 'Infected(Unlock)', 'Infected(Lock)', 'Positivity Rate(Lock)', 'Positivity Rate(Unlock)']
filename = "info_combine.csv"

with open(filename, 'w') as csvfile:  
	csvwriter = csv.writer(csvfile)  
	csvwriter.writerow(fields)      
	for row_title, iu, il, prl, pru in zip(row_headers, infected_lock, infected_unlock, tpr_lock, tpr_unlock):
		csvwriter.writerow([row_title] + [iu] + [il] + [prl]+ [pru])
