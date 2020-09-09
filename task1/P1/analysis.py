import numpy as np

np.set_printoptions(suppress=True)

data = np.loadtxt('mumbai_data.csv', usecols=range(1,5), skiprows=1, delimiter=',')
means = np.mean(data, axis = 0)
stds = np.std(data, axis = 0)
means = [format(round(x,3),'.3f') for x in means]
stds = [format(round(x,4),'.3f') for x in stds]

print('Field     Mean      Std.Dev.')
print('Tests    ', means[0], stds[0])
print('Infected ', means[1], ' '+stds[1])
print('Recovered', means[2], '  '+stds[2])
print('Deceased ', means[3], '   '+stds[3])