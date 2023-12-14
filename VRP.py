#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:40:13 2023

@author: can
"""

import numpy as np

n = 73 # 72 number of service stop
m = 10 # number of service
cap = 25 #capacity of a service bus

# initializing variables
visited = np.zeros((n))
routes = np.zeros((m, n))
r_indis = np.zeros((m))
cost = np.zeros((m))

number_of_people = np.zeros((n))
number_of_pinvh = np.zeros((n))

def vehicle_location():
    for i in range(m):
        print(i + 1,".vehicle is at the ",int(routes[i][int(r_indis[i])]) + 1,".stop!")     
         
def starting_points():
# Manually determining the starting points of the vehicles
    routes[0][0] = 0  
    number_of_pinvh[0] += number_of_people[0]
    routes[1][0] = 3  
    number_of_pinvh[1] += number_of_people[3]
    routes[2][0] = 16 
    number_of_pinvh[2] += number_of_people[16]
    routes[3][0] = 19 
    number_of_pinvh[3] += number_of_people[19]
    routes[4][0] = 28 
    number_of_pinvh[4] += number_of_people[28]
    routes[5][0] = 35 
    number_of_pinvh[5] += number_of_people[35]
    routes[6][0] = 46 
    number_of_pinvh[6] += number_of_people[46]
    routes[7][0] = 56 
    number_of_pinvh[7] += number_of_people[56]
    routes[8][0] = 67 
    number_of_pinvh[8] += number_of_people[67]
    routes[9][0] = 7 
    number_of_pinvh[9] += number_of_people[7]
    
    for i in range(10):
        r_indis[i] = 0
    
    visited[0] = 1
    visited[3] = 1
    visited[16] = 1
    visited[19] = 1
    visited[28] = 1
    visited[35] = 1
    visited[46] = 1
    visited[56] = 1
    visited[67] = 1
    visited[7] = 1
    visited[72] = 1

# Reading the input file
file_directory = "/Users/candenizci/Downloads/routedataset.txt"
with open(file_directory, "r") as file:
    dosya = file.readlines()   

ideger = []
for satir in dosya:
    int_deger = [int(deger) for deger in satir.split()]
    ideger.append(int_deger)
    
n1 = ideger.pop(0) #first line in txt file
number_of_people = ideger.pop() #last line in txt file

graph = np.array(ideger) # numpy matrix

starting_points()

next_point = 0 
vh = 0

# Determining the routes of the services
stop = True
while stop:
    
    minimum = 10000    
    for i in range(n):
        if visited[i] == 0:
            for j in range(m):
                if graph[int(routes[j][int(r_indis[j])])][i] < minimum and number_of_pinvh[j] + number_of_people[i] < cap: 
                    minimum = graph[int(routes[j][int(r_indis[j])])][i]
                    next_point = i
                    vh = j
    
    r_indis[vh] = r_indis[vh] + 1
    routes[vh][int(r_indis[vh])] = next_point 
    visited[next_point] = 1
    number_of_pinvh[vh] = number_of_pinvh[vh] + number_of_people[next_point]
    
    temp = 0
    for i in range(n):
        if visited[i] == 1:
            temp += 1
            
    if temp == n: 
        stop = False

# Adding the target point to the end of all routes
for i in range(m):
    r_indis[i] = r_indis[i] + 1
    routes[i][int(r_indis[i])] = 72

#  Calculating the distances to be travelled
totalcost = 0
for i in range(m):
    cost[i] = 0
    for j in range(int(r_indis[i])):
        cost[i] = cost[i] + graph[int(routes[i][j])][int(routes[i][j+1])]
    totalcost = totalcost + cost[i]

# Printing the routes
print("\n Routes:")
for i in range(m):
    print(i + 1,". vehicle")
    for j in range(int(r_indis[i])+1):
        print("->", int(routes[i][j]) + 1)
    print("Cost:", cost[i],"\n")
print("Total Cost:", totalcost)
