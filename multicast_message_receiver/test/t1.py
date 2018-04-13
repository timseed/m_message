from pprint import pprint

some_pt1 = [(10.76,2.9),(3.24,4.28),(7.98,1.98),(3.21,9.87)]
some_pt2 = [(11.87,6.87), (67.87,8.88), (44.44, 6.78), (9.81, 1.09), (6.91, 0.56), (8.76, 8.97), (8.21, 71.66)]


distance = {}
for x in some_pt1:
    for y in some_pt2:
        dist =abs(abs(x[0])-abs(y[0]))+abs(abs(x[1])-abs(y[1]))
        distance[dist]=[x,y]

shortest =sorted(distance.keys())[0]
print("Min Distance is {} Objects are  {} {} ".format(shortest, distance[shortest][0],distance[shortest][0]))