import math

class Building:
    def __init__(self, name, access, x, y):
        self.name = name
        self.access = access
        self.x = x
        self.y = y
      
Gate = Building("Gate", "No", 0, 0)
Administration = Building("Administration", "Yes", 1, 3)
LilianK = Building("LilianKBeam", "Yes", 2, 5)
MainLabs = Building("MainLabs", "Yes", 5, 4)
Village = Building("Village", "No", 5, 1)

class Environment(object):
    mapgraph = {
        Gate.name : [Administration.name, Village.name],
        Administration.name : [LilianK.name],
        LilianK.name : [Administration.name, MainLabs.name],
        MainLabs.name : [LilianK.name, Village.name],
        Village.name : [Gate.name, MainLabs.name]
        }
    
    #Function to generate the list of all edges
    def generate_edges(mapgraph):
        edges = []
        for i in mapgraph:
            for neighbour in mapgraph[i]:
                edges.append((i, neighbour))

        #print(edges)
        
        return edges
    
    #The following Python function calculates the isolated nodes of a given graph
    #this will not do anything as all buildings are connected
    def find_isolated_nodes(mapgraph):
        isolated = []
        for i in mapgraph:
            if not mapgraph[i]:
                isolated.append(i)

        return isolated
    """
    def getheuristics(node, goal):
        D = 2
        dx = abs(node.x - goal.x)
        dy = abs(node.y - goal.y)

        return D * (dx + dy)
    
    def geteuclidean(node, goal):
        D = 2
        dx = abs(node.x - goal.x)
        dy = abs(node.y - goal.y)

        return D * math.sqrt(dx * dx + dy * dy)
    
    print(getheuristics(Gate, Village))
    print(geteuclidean(Gate, Village))
    #print(find_isolated_nodes(mapgraph))
    #print(generate_edges(mapgraph))"""

    def find_path(self, start_vertex, end_vertex, path=None):
        if path == None:
            path = []
        graph = self.mapgraph
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)

                if extended_path:
                    return extended_path
        return None

    path = find_path(Gate, MainLabs)
    print

    
theEnvironment = Environment()

            








