'''

Cluster analysis algorithm: ROCK

Based on article description:
 - S.Guha, R.Rastogi, K.Shim. ROCK: A Robust Clustering Algorithm for Categorical Attributes. 1999.

Implementation by Andrei Novikov (spb.andr@yandex.ru)

'''

import math


# support methods
##test
def ed(i,j):
    sumSquare = 0
    for k in range(len(i)):
        sumSquare += abs(i[k] - j[k])**2
    return math.sqrt(sumSquare)

def jaccardConi(a,b):
    intersect = [val for val in a if val in b]
    union_liist = list(set(a).union(set(b)))

    if len(intersect) == 0:
        return 0.0
    else:
        return len(intersect)*1.0/len(union_list)

def read_sample(filename):
    """ Return sample for cluster analysis. """
    file = open(filename,'r')
    sample = [[float(val) for val in line.split()] for line in file];

    file.close()
    return sample

def euclidean_distance(a,b):
    """ Return Euclidean Distance between point a and point b """
    sumSquare = 0
    for k in range(len(a)):
        sumSquare += abs(a[k] - b[k]) ** 2
    return math.sqrt(sumSquare)


def rock(data, eps, number_clusters, threshold = 0.5):
    "data            - input data - list of points where each point
                        "is represented by list of coordinates."
    "eps             - connectivity radius (similarity threshold), points are neighbors if distance between them is less than connectivity radius."
    "number_clusters - defines number of clusters that should be allocated from the input data set."
    "threshold       - value that defines degree of normalization that influences on choice of clusters for merging during processing."
    
    """ Returns list of allocated clusters,
        each cluster contains indexes of objects in list of data."""
    
    degree_normalization = 1.0 + 2.0 * ( (1.0 - threshold) / (1.0 + threshold) );
    adjacency_matrix = create_adjacency_matrix(data, eps);
    clusters = [[index] for index in range(len(data))];
    
    while (len(clusters) > number_clusters):
        indexes = find_pair_clusters(clusters, adjacency_matrix, degree_normalization);
        
        if (indexes != [-1, -1]):
            clusters[indexes[0]] += clusters[indexes[1]];
            clusters.pop(indexes[1]);   # remove merged cluster.
        else:
            break;  # totally separated clusters have been allocated
    
    return clusters;



def create_adjacency_matrix(data, eps):
    "Private function that is used by rock.
    "Returns 2D matrix (list of lists) where each element
    "described existence of link between points (marks them as neighbors)."
    
    "(in) data                - input data - list of points where each point is represented by list of coordinates."
    "(in) eps                 - connectivity radius (similarity threshold), points are neighbors if distance between them is less than connectivity radius."
    
    "Returns adjacency matrix for the input data set in line with connectivity radius."
    
    size_data = len(data);
    
    adjacency_matrix = [ [ 0 for i in range(size_data) ] for j in range(size_data) ];
    for i in range(0, size_data):
        for j in range(i + 1, size_data):
            distance = euclidean_distance(data[i], data[j]);
            ## jaccardCon
            if (distance <= eps):
                adjacency_matrix[i][j] = 1;
                adjacency_matrix[j][i] = 1;
    
    return adjacency_matrix;



def calculate_links(cluster1, cluster2, adjacency_matrix):
    "Private function that is used by calculate_goodness.
    "Returns number of link between two clusters."
    "Link between objects (points) exists only if distance between them less than connectivity radius."
    
    "(in) cluster1         - cluster that is represented by list contains indexes of objects (points) from input data set."
    "(in) cluster2         - cluster that is represented by list contains indexes of objects (points) from input data set."
    "(in) adjacency_matrix - adjacency matrix that represents distances between objects (points) from the input data set."
    
    "Returns number of links between two clusters."
    
    number_links = 0;
    
    for index1 in cluster1:
        for index2 in cluster2:
            number_links += adjacency_matrix[index1][index2];
            
    return number_links;
  


def find_pair_clusters(clusters, adjacency_matrix, degree_normalization):
    " Private function that is used by rock.
    " Returns pair of clusters that are best candidates for merging in line with goodness measure."
    " The pair of clusters for which the above goodness measure is maximum
    " is the best pair of clusters to be merged."
    
    "(in) clusters                 - list of cluster that have been allocated during processing
                                    ", each cluster is represented by list of
                                    "indexes of points from the input data set."
    "(in) adjacency_matrix         - adjacency matrix that
                                    "represents distances between objects (points)
                                    "from the input data set."
    "(in) degree_normalization     - degree of normalization that is used by
                                    "goodness measurement for obtaining most suitable clusters
                                    "for merging."
    
    "Returns list that contains two indexes of clusters (from list 'clusters')
    "that should be merged on this step. It can be equals to [-1, -1] when number of links between"
    "all clusters doesn't exist."
    
    maximum_goodness = 0.0;
    cluster_indexes = [-1, -1];
    
    for i in range(0, len(clusters)):
        for j in range(i + 1, len(clusters)):
            goodness = calculate_goodness(clusters[i], clusters[j],
                                          adjacency_matrix, degree_normalization);
            if (goodness > maximum_goodness):
                maximum_goodness = goodness;
                cluster_indexes = [i, j];
    
    return cluster_indexes;          


def calculate_goodness(cluster1, cluster2, adjacency_matrix, degree_normalization):
    "Private function that is used by find_pair_clusters. Calculates coefficient 'goodness measurement' between two clusters."
    "The coefficient defines level of suitability of clusters for merging."
    
    "(in) cluster1                - cluster that is represented by list contains indexes of objects (points) from input data set."
    "(in) cluster2                - cluster that is represented by list contains indexes of objects (points) from input data set."
    "(in) adjacency_matrix        - adjacency matrix that represents distances between objects (points) from the input data set."
    "(in) degree_normalization    - degree of normalization that is used by goodness measurement for obtaining most suitable clusters for merging."
    
    "Returns goodness measure between two clusters."
    
    number_links = calculate_links(cluster1, cluster2, adjacency_matrix);
    devider = (len(cluster1) + len(cluster2)) ** degree_normalization - len(cluster1) ** degree_normalization - len(cluster2) ** degree_normalization;
    
    return (number_links / devider);

