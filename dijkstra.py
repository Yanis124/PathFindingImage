from queue import PriorityQueue
import cv2
import numpy as np
import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import heapq
import time




# calculate the distance between two points in an image
def calculCout(point1, point2, image_rgb):
    pixel1 = image_rgb[point1[0], point1[1]].astype(int)
    pixel2 = image_rgb[point2[0], point2[1]].astype(int)
    
    return np.linalg.norm(pixel1 - pixel2)


def dijkstra(image_rgb, start, end):
    height, width = image_rgb.shape[:2]
    visited = np.full((height, width), False, dtype=bool)
    distance_map = np.full((height, width), np.inf)
    parent_map = np.full((height, width, 2), -1, dtype=int)
    

    distance_map[start] = 0  #set the distance to the start point to 0
    
    list_vertex = []
    list_vertex.append(start)

    while not list_vertex == []:
        dist, current_node = find_smallest_vertex(list_vertex, distance_map)
        
        list_vertex.remove(current_node)
        
        if current_node == end: # if we find the last vertex we stop the algorithm"
            break

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x = current_node[1] + dx
            new_y = current_node[0] + dy
            neighbor = (new_y, new_x)

            if (0 <= new_x < width and 0 <= new_y < height):
                cost = calculCout(current_node, neighbor, image_rgb)
                new_dist = dist + cost
                
                if new_dist < distance_map[neighbor]: #update the distance of a vertex 
                    distance_map[neighbor] = new_dist
                    parent_map[neighbor] = current_node

                
                if not visited[neighbor]:
                    visited[neighbor]=True #mark the vertex as visited
                    list_vertex.append(neighbor)

    path = [end]
    while path[-1] != start:
        parent = tuple(parent_map[path[-1]])
        path.append(parent)

    return path[::-1]

#Dijkstra algorithm using a binary heap
def dijkstra_binary_heap(image_rgb, start, end):
    
    height, width = image_rgb.shape[:2]
    visited = np.full((height, width), False, dtype=bool)
    distance_map = np.full((height, width), np.inf)
    parent_map = np.full((height, width, 2), -1, dtype=int)

    distance_map[start] = 0  # set the distance to the start point to 0

    priority_queue = [(0, start)]

    while priority_queue:
        dist, current_node = heapq.heappop(priority_queue) #get the smallest element in the heap

        if visited[current_node]:
            continue

        visited[current_node] = True

        if current_node == end:  # if we find the last vertex, we stop the algorithm
            break

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x = current_node[1] + dx
            new_y = current_node[0] + dy
            neighbor = (new_y, new_x)

            if 0 <= new_x < width and 0 <= new_y < height:
                cost = calculCout(current_node, neighbor, image_rgb)
                new_dist = dist + cost

                if new_dist < distance_map[neighbor]:  # update the distance of a vertex
                    distance_map[neighbor] = new_dist
                    parent_map[neighbor] = current_node

                if not visited[neighbor]:
                    heapq.heappush(priority_queue, (new_dist, neighbor))

    path = [end]
    while path[-1] != start:
        parent = tuple(parent_map[path[-1]])
        path.append(parent)

    return path[::-1]

#find the smallest vertex in a list
def find_smallest_vertex(list_vertex,distance_map):
    min_distance = np.inf
    min_vertex = None

    for vertex in list_vertex:
        if distance_map[vertex] < min_distance:
            
            min_distance = distance_map[vertex]
            min_vertex = vertex

    return min_distance, min_vertex

#calculate execution time 
def calculate_execution_time_dijkstra_binary_heap(image_rgb, start, end):
    start_time = time.time()
    path=dijkstra_binary_heap(image_rgb, start, end)
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time

    # Write the result to a file
    result_file_path = "execution_time_dijkstra_optimisation.txt"
    with open(result_file_path, "a") as file:
        file.write(f"{execution_time}\n")
        
    return path

#calculate execution time 
def calculate_execution_time_dijkstra(image_rgb, start, end):
    start_time = time.time()
    path=dijkstra_binary_heap(image_rgb, start, end)
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time

    # Write the result to a file
    result_file_path = "execution_time_dijkstra_optimisation.txt"
    with open(result_file_path, "a") as file:
        file.write(f"{execution_time}\n")
        
    return path

