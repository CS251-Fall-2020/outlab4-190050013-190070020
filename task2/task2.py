import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--data")
	args = parser.parse_args()
	df = pd.read_csv(args.data)
	grp = df.groupby('instance')
	for name, group in grp: 
		plt.figure() 
		gp= group.groupby(['algorithm','epsilon'])
		for na, g in gp:
			x=[]
			y=[]
			gk = g.groupby('horizon') 
			for nam, gg in gk: 
				hori = gg.iloc[0,4]
				x.append(hori)
				reg = gg['REG'].sample(n=50).mean() 
				y.append(reg)
			if na[0]!='epsilon-greedy':
				lab = na[0]
			else:
				lab = na[0]+" with epsilon="+str(na[1])
			plt.yscale("log")
			plt.xscale("log")
			plt.plot(x, y, label=lab)
		plt.legend(loc="upper left")
		plt.xlabel('horizon')
		plt.ylabel('Regret')
		if name=='i-1.txt':
			plt.title('Instance 1 - both axes in log scale')
			plt.savefig('instance1.png')
			plt.clf()
		if name=='i-2.txt':
			plt.title('Instance 2 - both axes in log scale')
			plt.savefig('instance2.png')
			plt.clf()
		if name=='i-3.txt':
			plt.title('Instance 3 - both axes in log scale')
			plt.savefig('instance3.png')
			plt.clf()

if __name__ == '__main__':
	main()