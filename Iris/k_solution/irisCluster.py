import re
import random
import math

def dist(a, b):
    d = 0
    t = [(i - j)**2 for i, j in zip(a, b)]
    for x in t:
        d += x
    return round(math.sqrt(d), 1);

def newCentr(clust):
    m = [0, 0, 0, 0]
    for i in clust:
        x = 0
        for f in i:
            m[x] += f
            x += 1
    res = [round(y/len(clust), 1) for y in m]
    return res;

irisSet = []
with open('C:\Python36\iris.data') as irisData:
    for line in irisData:
        inst = [float(f) for f in line.split(' ')]
        irisSet.append(inst)
centroids = random.sample(irisSet, 3)
clusterAs = [0] * len(irisSet)
while True:
    clust1 = []
    clust2 = []
    clust3 = []
    x = 0
    for inst in irisSet:
        d = []
        for c in centroids:
            d.append(dist(inst, c))
        if d[0] < d[1] and d[0] < d[2]:
            clust1.append(inst)
            clusterAs[x] = 1
        if d[1] < d[0] and d[1] < d[2]:
            clust2.append(inst)
            clusterAs[x] = 2
        if d[2] < d[0] and d[2] < d[1]:
            clust3.append(inst)
            clusterAs[x] = 3
        x += 1
    newCentroids = [newCentr(clust1), newCentr(clust2), newCentr(clust3)]
    if newCentroids == centroids:
        break
    else:
        centroids = list(newCentroids)
#print(clusterAs)
with open('C:\Python36\irisResult.data', 'w') as results:
    for y in clusterAs:
        results.write('%s\n' % y)
