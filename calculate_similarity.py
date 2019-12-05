# L2 and Cosine similarity measurement
import math

def l2_norm(x): #function to calculate L2 norm of a vector
	'''
	arguement
	---------
	x - the vector

	returns - L2 norm of the vector
	'''
	sum = 0
	for i in range(len(x)):
		sum += x[i]**2
	return math.sqrt(sum)

def SimilarityMeasure(data1, data2, type='L2'):
	'''
	arguements 
	----------
	data1, data2 - vectors, between which we are going to calculate similarity

	returns
	-------
	distance between the two vectors
	'''
	if type=='L2':
		# for L2 norm or pythagorean distance
		dist = 0
		for i in range(4):
			dist += (data1[i] - data2[i] )**2

		dist = math.sqrt(dist)
		return dist

	if type=='Cosine':
		# form cosine similarity = a.b/|a|.|b|
		dot_prod = 0
		data1_mod = l2_norm(data1)
		data2_mod = l2_norm(data2)
		for x in range(4):
			dot_prod += data1[x]*data2[x]
		return (dot_prod/(data1_mod*data2_mod))

	else:
		print('Please provide proper similarity measurement type')
		return 0



if __name__=='__main__':
	# for testing this module
	print(SimilarityMeasure([0,0,0,0],[3,4,0,0]))
	print(l2_norm([3,4]))