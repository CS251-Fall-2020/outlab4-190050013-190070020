import argparse
from PIL import Image
import numpy as np
from scipy.cluster.vq import kmeans2, vq

def load_image(infilename) :
	img = Image.open(infilename)
	img.load()
	data = np.asarray(img, dtype="float64")
	return data

def save_image(npdata, outfilename):
	img = Image.fromarray(np.asarray( npdata, dtype="uint8"))
	img.save(outfilename)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input")
	parser.add_argument("--k")
	parser.add_argument("--output")
	args = parser.parse_args()

	data = load_image(args.input)
	m, n, _ = data.shape
	M = data.reshape(m*n, 3)

	centroid, label = kmeans2(M, int(args.k), minit='++')

	for i in range(0, int(args.k)):
		M[label==i] = centroid[i]

	M = M.reshape(m, n, 3)
	save_image(M, args.output)


if __name__ == '__main__':
	main()