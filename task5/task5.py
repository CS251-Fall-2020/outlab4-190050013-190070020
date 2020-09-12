import matplotlib.pyplot as plt
import scipy
import numpy as np
import requests
from functools import reduce
from scipy.stats import linregress

covid_url = "https://api.covid19india.org/csv/latest/case_time_series.csv"

with requests.Session() as s:
    download = s.get(covid_url)
    decoded_content = download.content.decode("utf-8")
    content = decoded_content[decoded_content.find("14 April"):]
    content = content.splitlines()

deaths = [c.split(',')[-1] for c in content]
h = []
for i in range(1,len(deaths)):
    h.append(int(deaths[i])/int(deaths[i-1]))

days = np.linspace(1,len(h),len(h))

h = np.array(h,dtype='float64')
slope, intercept, r_value, p_value, std_err = linregress(days, h)
num_days = int(np.ceil(((1 - intercept)/slope)))
print(num_days)

plt.scatter(days,h,c = 'r',marker = '.',label = fr'$H(t)$ vs t (in days)')
days = np.linspace(1,num_days,num_days)
h = [(intercept + slope * d) for d in days]
h = np.array(h,dtype='float64')
plt.plot(days,h, label = fr'Linear least squares fit')
plt.xlabel("Time (in days)")
plt.ylabel(fr"$H(t)$")
plt.title(fr'$H(t)$ vs t')
plt.legend()
plt.savefig("covid.png")
plt.clf()
