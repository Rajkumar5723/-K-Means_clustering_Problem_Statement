# importing the libraries

"""  DO NOT MODIFY  """
import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
"""  DO NOT MODIFY  """

def find_best_kmeans(data, min_k, max_k):

    """  write from here  """
    best_k = None
    best_silhouette_score = -1      

    for k in range(min_k, max_k + 1):
        # Initialize the K-Means model
        kmeans = KMeans(n_clusters=k, n_init='auto', random_state=0)
        kmeans.fit(data)

        labels = kmeans.labels_
      
        silhouette_score = metrics.silhouette_score(data, labels)

        if silhouette_score > best_silhouette_score:
            best_silhouette_score = silhouette_score
            best_k = k

    return best_k



"""  DO NOT MODIFY  """
if __name__ == '__main__':
 
    if len(sys.argv) == 2:
        print("Usage: python assignment.py <number> <number>")
        sys.exit(1)

    input_data_one = sys.argv[1].strip()
    input_data_two = sys.argv[2].strip()

    if input_data_one.isdigit() and input_data_two.isdigit():

        min_k = int(input_data_one)
        max_k = int(input_data_two)
        if min_k>=2 or max_k>min_k:
            data =pd.read_csv(r"C:\Users\RAJKUMAR\Desktop\iit\housing.csv")
            print(find_best_kmeans(data, min_k, max_k)) 
        else:
           print("Invalid input")
    else:
        print("Invalid input")