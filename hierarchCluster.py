##

from Queue import PriorityQueue
import math

def getMedian(alist):
    """get the median value of a list"""
    tmp = list(alist)
    tmp.sort()
    alen = len(tmp)
    if (alen % 2) == 1:
        return tmp[alen // 2]
    else:
        return (tmp[alen // 2] + tmp[alen // 2 - 1]) / 2.0

def normalizeColumn(column):
    """normalize column using Modified Standard Score"""
    median = getMedian(column)
    asd = sum([abs(x - median) for x in column]) / len(column)
    #if asd == 0:
    #    return 
    result = [(x - median) / asd for x in column]
    return result


class hClusterer:
    """the first column is a label not used in clustering,
       the other columns contains numeric data"""

    def __init__(self, filename):
        file = open(filename)
        self.data = {}
        self.counter = 0
        self.queue = PriorityQueue()
        lines = file.readlines()
        file.close()
        header = lines[0].split(',')
        self.cols = len(header)
        self.data = [[] for i in range(len(header))]

        for line in lines[1:]:
            cells = line.split(',')
            flag = 0
            for cell in range(self.cols):
                if flag == 0:
                    # label column
                    self.data[cell].append(cells[cell])
                    flag = 1
                else:
                    # numeric attributes
                    self.data[cell].append(float(cells[cell]))

        # normalize the column
        for col in range(1, self.cols):
            self.data[col] = normalizeColumn(self.data[col])

    # compute Euclidean Distance between item i and item j
    def euclideanDistance(self, i,j):
        sumSquare = 0.0
        for k in range(1, self.cols):
            sumSquare += (self.data[k][i] - self.data[k][j]) ** 2
        return math.sqrt(sumSquare)

    # push the neighbor into PriorityQueue
    """
    sample data for neighbors dict:
    {2: ((1,2), 1.23),  3: ((1, 3), 2.3)... }
    """
    def pushNeighborQueue(self):
        rows = len(self.data[0])

        for i in range(rows):
            minDistance = 999999
            nearestNeighbor = 0
            neighbors = {}
            for j in range(rows):
                if i != j:
                    dist = self.euclideanDistance(i,j)
                    if i<j:
                        pair = (i,j)
                    else:
                        pair = (j,i)
                    neighbors[j] = (pair, dist)
                    if dist < minDistance:
                        minDistance = dist
                        nearestNeighbor = j
            # create nearest pair
            if i < nearestNeighbor:
                nearestPair = (i, nearestNeighbor)
            else:
                nearestPair = (nearestNeighbor, i)

            # put instance into priority queue
            self.queue.put((minDistance, self.counter,
                            [[self.data[0][i]], nearestPair,neighbors]))
            self.counter += 1
        
# unit test
hc = hClusterer('G:\dogs.csv')
hc.pushNeighborQueue()
hc.queue.get()
