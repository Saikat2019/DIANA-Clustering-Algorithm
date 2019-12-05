# L2 and Cosine similarity
import math

def l2_norm(x):
	sum = 0
	for i in range(len(x)):
		sum += x[i]**2
	return math.sqrt(sum)

def SimilarityMeasure(data1, data2, type='L2'):
	if type=='L2':
		dist = 0
		for i in range(4):
			dist += (data1[i] - data2[i] )**2

		dist = math.sqrt(dist)
		return dist

	if type=='Cosine':
		dot_prod = 0
		data1_mod = l2_norm(data1)
		data2_mod = l2_norm(data2)
		for x in range(4):
			dot_prod += data1[x]*data2[x]
		return (dot_prod/(data1_mod*data2_mod))

	else:
		print('Please provide proper similarity measurement type')



if __name__=='__main__':
	print(SimilarityMeasure([0,0,0,0],[3,4,0,0]))
	print(l2_norm([3,4]))