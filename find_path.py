import math
import random

class Environment(object):    
    def __init__(self):
        self.mapgraph = {
            "Gate" : ["Administration", "Village"],
            "Administration" : ["LilianK"],
            "LilianK" : ["Administration", "MainLabs.name"],
            "MainLabs" : ["LilianK", "Village"],
            "Village" : ["Gate", "MainLabs"]
            }
        self.list = ['Gate', 'Administration', 'LilianK', 'MainLabs', 'Village']
        self.random_state = random.choice(self.list)
        self.random_goal = random.choice(self.list)
        
class pathFinder(Environment):
    def __init__(self, Environment):
        print("Welcome, this Test 001")
        print(Environment.random_state)
        print(Environment.random_goal)

        if Environment.random_state == Environment.random_goal:
            print("You are already where you want to be")

        def find_path(start_vertex, end_vertex, path=None):
            if path == None:
                path = []
            graph = Environment.mapgraph
            
            path = path + [start_vertex]
            if start_vertex == end_vertex:
                return path
            if start_vertex not in graph:
                return None
            for vertex in graph[start_vertex]:
                if vertex not in path:
                    extended_path = find_path(vertex, 
                                                   end_vertex, 
                                                   path)
                    if extended_path: 
                        return extended_path
            return None

        def find_all_paths(start_vertex, end_vertex, path=[]):
            graph = Environment.mapgraph
            
            path = path + [start_vertex]
            if start_vertex == end_vertex:
                return [path]
            if start_vertex not in graph:
                return []
            paths = []
            for vertex in graph[start_vertex]:
                if vertex not in path:
                    extended_paths = find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                    for p in extended_paths: 
                        paths.append(p)
            return paths
        
        def find_shortest_path(start_vertex, end_vertex, path=[]):
            graph = Environment.mapgraph 
            path = path + [start_vertex]
            if start_vertex == end_vertex:
                return [path]
            if start_vertex not in graph:
                return None
            shortest = None
            for vertex in graph[start_vertex]:
                if vertex not in path:
                    newpath = find_shortest_path(vertex, end_vertex, path)
                    if newpath:
                        if not shortest or len(newpath) < len(shortest):
                            shortest = newpath
            return shortest

        
        print(find_path("Gate", "LilianK"))
        print(find_all_paths("Gate", "LilianK"))

        

        #path = find_shortest_path(Environment.random_start, Environment.random_goal)
        #print(path)
theEnvironment = Environment()
pathFinder = pathFinder(theEnvironment)

    


            








