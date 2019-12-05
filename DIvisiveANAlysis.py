import numpy as np
import matplotlib.pyplot as plt
from distance_matrix import DistanceMatrix 
import copy
import pandas as pd 


class DianaClustering:
	def __init__(self,data):
		self.data = data
		self.n_samples, self.n_features = data.shape

	def fit(self,n_clusters):
		similarity_matrix = DistanceMatrix(self.data)
		clusters = [list(range(self.n_samples))]
		while True:
			c_diameters = [np.max(similarity_matrix[cluster][:, cluster]) for cluster in clusters]
			max_cluster_dia = np.argmax(c_diameters)
			max_difference_index = np.argmax(np.mean(similarity_matrix[clusters[max_cluster_dia]][:, clusters[max_cluster_dia]], axis=1))
			splinters = [clusters[max_cluster_dia][max_difference_index]]
			last_clusters = clusters[max_cluster_dia]
			del last_clusters[max_difference_index]
			while True:
				split = False
				for j in range(len(last_clusters))[::-1]:
					splinter_distances = similarity_matrix[last_clusters[j], splinters]
					last_distances = similarity_matrix[last_clusters[j], np.delete(last_clusters, j, axis=0)]
					if np.mean(splinter_distances) <= np.mean(last_distances):
						splinters.append(last_clusters[j])
						del last_clusters[j]
						split = True
						break
				if split == False:
					break
			del clusters[max_cluster_dia]
			clusters.append(splinters)
			clusters.append(last_clusters)
			if len(clusters) == n_clusters:
				break

		cluster_labels = np.zeros(self.n_samples)
		for i in range(len(clusters)):
			cluster_labels[clusters[i]] = i

		return cluster_labels

		


if __name__ == '__main__':
	data = pd.read_csv('HAYES_ROTH.csv')
	data = data.drop(columns="Name")
	data = data.drop(columns="Class")

	diana = DianaClustering(data)
	clusters = diana.fit(3)
	print(clusters)