from collections import defaultdict
from datetime import datetime

##time of day / crowding
now = datetime.now()
current_time = now.strftime("%H:%M")

day = datetime.now()
current_day = day.strftime("%A")

Gate_Administration_weight = 80
Gate_Village_weight = 60
Administration_LilianK_weight = 20
LilianK_MainLabs = 40
MainLabs_Village = 40

if current_time == '9:00' and current_day == 'Monday' or 'Tuesday' or 'Wednesday':
    Gate_Administration_weight += 20
elif current_time == '9:00' and current_day == 'Monday':
    Gate_Village_weight += 20
elif current_time == '10:40' and current_day == 'Monday':
    Gate_Village_weight += 20
elif current_time == '15:30' and current_day == 'Sunday':
    Gate_Village_weight += 60

#define the graph
class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        
graph = Graph()

edges = [
    ('Gate', 'Administration', Gate_Administration_weight),
    ('Gate', 'Village', Gate_Village_weight),
    ('Administration', 'LilianK', Administration_LilianK_weight),
    ('LilianK', 'MainLabs', LilianK_MainLabs),
    ('MainLabs', 'Village', MainLabs_Village),
       ]

for edge in edges:
    graph.add_edge(*edge)

##START
print("1.Gate")
print("2.Administration")
print("3.LilianK")
print("4.MainLabs")
print("5.Village")
user_location = input("Where are you right now: ")
user_goal = input("Where do you want to go: ")

def wheel_chair_access(user_goal):
    if user_goal == "Gate":
        print("There is wheel chair access at your destination")
    elif user_goal == "Administration":
        print("There is wheel chair access at your destination")
    elif user_goal == "LilianK":
        print("There is wheel chair access at your destination")
    elif user_goal == "MainLabs":
        print("There is wheel chair access at your destination")
    elif user_goal == "Village":
        print("Be Warned there is no wheel chair access")
        
def shortest_path(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

def find_all_paths(start_vertex, end_vertex, path=[]):
    graph = {
            "Gate" : ["Administration", "Village"],
            "Administration" : ["LilianK", "Gate"],
            "LilianK" : ["Administration", "MainLabs"],
            "MainLabs" : ["LilianK", "Village"],
            "Village" : ["Gate", "MainLabs"]
            }

    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in graph:
        return []
    paths = []
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_paths = find_all_paths(vertex,end_vertex,path)                                                     
            for p in extended_paths: 
                paths.append(p)
    return paths

def dist(location, goal):
    distance = graph.weights[(location, goal)] 
    return distance

print("Heres a list of possible paths: ")
print(find_all_paths(user_location, user_goal))
print("The shortest path is: ")
print(shortest_path(graph, user_location, user_goal))
#print("The distance to be covered is: ")
#print(dist(user_location, user_goal))
print(wheel_chair_access(user_goal))

##TO-DO-LIST
#Distance calculations from each node
#Crowding - time of day
#multiple destinations




