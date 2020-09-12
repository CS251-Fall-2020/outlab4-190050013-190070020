import numpy as np

np.set_printoptions(suppress=True)

data = np.loadtxt('mumbai_data.csv', usecols=range(1,5), skiprows=1, delimiter=',')
means = np.mean(data, axis = 0)
stds = np.std(data, axis = 0)
means = [format(round(x,3),'.3f') for x in means]
stds = [format(round(x,4),'.3f') for x in stds]

print('{:<11} {:<13} {:<12}'.format("Field", "Mean", "Std. Dev"))
print('{:<11} {:<13} {:<12}'.format("Tests", str(means[0]), str(stds[0])))
print('{:<11} {:<13} {:<12}'.format("Infected", str(means[1]), str(stds[1])))
print('{:<11} {:<13} {:<12}'.format("Recovered", str(means[2]), str(stds[2])))
print('{:<11} {:<13} {:<12}'.format("Deceased", str(means[3]), str(stds[3])))
