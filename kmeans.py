# -*- coding: utf-8 -*-
import math
import random

""" implementation of k-means algroithm
k is the number of clusters to make
    1. reads the data from the file named filename
    2. stores that data by column in self.data
    3. normalizes the data using Modified Standard Score
    4. randomly selects the initial centroids
    5. assigns points to clusters associated with those centroids

"""

def getMedian(alist):
    """ get the median value of a list """
    tmp = list(alist)
    tmp.sort()
    alen = len(tmp)
    if (alen % 2 == 0):
        return (tmp[alen // 2] + tmp[alen // 2 - 1]) / 2.0
    else:
        return tmp[alen // 2]

def normalizeColumn(column):
    """ normalize the column value using Modified Standard Score
        (each value - median) / absolute standard deviation"""
    median = getMedian(column)
    asd = sum([abs(x-median) for x in column]) / len(column)
    result = [(x - median)/ asd for x in column]
    return result


class kClusterer:
    """ Implement the k-means algroithm """
    def __init__(self, filename, k):
        file = open(filename)

        self.data = {}
        self.k = k
        self.counter = 0
        self.iterationNumber = 0

        # track the % of the points that change cluster
        self.pointsChanged = 0
        # sum of Squared Error
        self.sse = 0

        # read data from file
        lines = file.readlines()
        file.close()

        header = lines[0].split(',')
        self.cols = len(header)
        self.data = [[] for i in range(len(header))]

        for line in lines[1:]:
            cells = line.split(',')
            # the first column is label
            toggle = 0
            for cell in range(self.cols):
                if toggle == 0:
                    self.data[cell].append(cells[cell])
                    toggle = 1
                else:
                    self.data[cell].append(float(cells[cell]))
        # rows of data items
        self.datasize = len(self.data[1])
        self.memberOf = [-1 for x in range(self.datasize)]

        ## normalize column data
        for i in range(1, self.cols):
            self.data[i] = normalizeColumn(self.data[i])

        ## select random centroids from existing points
        random.seed()
        self.centriods = [[self.data[i][r] for i in range(1,len(self.data))]
                          for r in random.sample(range(len(self.data[0])),
                                                 self.k)]
        ## assign each points to cluster
        self.assignPointsToCluster()


    def assginPointToCluster(self, i):
        """ Assgin point i to cluster based on the distance from centriods"""
        # pass
        min = 999999
        clusterNum = -1
        for centroid in range(self.k):
            dist = self.euclideanDistance(i, centroid)
            if dist < min:
                min = dist
                clusterNum = centroid
        # track changing points
        if clusterNum != self.memberOf[i]:
            self.pointsChanged += 1
        self.sse += min ** 2
        return clusterNum

    def euclideanDistance(self,i,j):
        """ compute the distance between point i and centriod j """
        sumSquare = 0
        for k in range(1,self.cols):
            sumSquare += (self.data[k][i] - self.centriods[j][k-1]) ** 2
        return math.sqrt(sumSquare)

    def updateCentriods(self):
        """ Using the points in the cluster to determine
            the centriod (mean) of each cluster """
        # the number belong to each cluster
        members = [self.memberOf.count(i) for i in range(len(self.centriods))]
        self.centriods = [[sum([self.data[k][i]
                                for i in range(len(self.data[0]))
                                if self.memberOf[i] == centriod])/members[centriod]
                           for k in range(1, len(self.data))]
                          for centriod in range(len(self.centriods))]

    def assignPointsToCluster(self):
        self.pointsChanged = 0
        self.sse = 0
        # call method assginPointToCluster
        self.memberOf = [self.assginPointToCluster(i)
                         for i in range(len(self.data[1]))]


    def kCluster(self):
        done = False

        while not done:
            self.iterationNumber += 1
            self.updateCentriods()
            self.assignPointsToCluster()

            # if fewer than 1% of the points change cluster
            if float(self.pointsChanged) / len(self.memberOf) < 0.01:
                done = True
        print "Final SSE: %f" % self.sse

    def showMembers(self):
        """ Display the result """
        for centriod in range(len(self.centriods)):
            print "\n\nClass %i\n=======" % centriod
            for name in [self.data[0][i] for i in range(len(self.data[0]))
                         if self.memberOf[i] == centriod]:
                print name







######################################
##      RUN THE K-MEANS CLUSTER     ##
######################################
km = kClusterer('C:\\Users\\claus_000\\Desktop\\cereal.csv',3)
km.kCluster()
km.showMembers()
