from collections import defaultdict
from datetime import datetime

##time of day / crowding
now = datetime.now()
current_time = now.strftime("%H:%M")

day = datetime.now()
current_day = day.strftime("%A")

Gate_Administration_weight = 80
Gate_VillageOffices_weight = 60
Gate_VillageOne_weight = 70

Administration_LilianK_weight = 20
Administration_Cafeteria_weight = 40
Administration_VillageOne_weight = 60

LilianK_MainLabs_weight = 40
LilianK_Cafeteria_weight = 20
LilianK_Humanities_weight = 60
LilianK_Library_weight = 100
LilianK_Chandaria_weight = 50

Cafeteria_Hostels_weight = 40
Cafeteria_LilianK_weight = 20

Hostels_FreidaBrown_weight = 60
Hostels_Animation_weight = 20
Hostels_LilianK_weight = 60
Hostels_Humanities_weight = 60

Animation_Auditorium_weight = 20
Animation_FreidaBrown_wieght = 60

Auditorium_Library_weight = 40
Auditorium_FreidaBrown_weight = 70
Auditorium_Libray_weight = 20

Library_ScienceBlock_weight = 100
Library_FreidaBrown_weight = 80
Library_Chandaria_weight = 40

Chandaria_Library_weight = 40
Chandaria_LilianK_weight = 50
Chandaria_Humanities_weight = 40

Humanities_Chandaria_weight = 40
Humanitites_Hostels_weight = 60
Humanities_StoneBenches_weight = 20
Humanities_LilianK_weight = 60
Humanities_VillageFive_weight = 20

StoneBenches_Humanities_weight = 20
StoneBenches_MainLabs_weight = 10
StoneBenches_VillageFour_weight = 10

MainLabs_LilianK_weight = 50
MainLabs_VillageOffices_weight = 50
MainLabs_StoneBenches_weight = 10

VillageOne_VillageThree_weight = 20
VillageOne_Gate = 70

VillageTwo_VillageThree_weight = 20

VillageThree_VillageFour_weight = 20
VillageFour_VillageFive_weight = 20
VillageFive_VillageSix_weight = 20

if current_time == '9:00' and current_day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday':
    Gate_Administration_weight += 20
elif current_time == '9:00' and current_day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday':
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
    ('Gate', 'VillageOffices', Gate_VillageOffices_weight),
    ('Gate', 'VillageOne', Gate_VillageOne_weight),
    
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

def dist_covered(shortest_distance):
    if shortest_distance == ['Gate', 'Village', 'MainLabs']:
        distance = 100
    elif shortest_ditance == []
    return distance

#a list of possible paths
print("Heres a list of possible paths: ")
print(find_all_paths(user_location, user_goal))

#shortest_path
print("The shortest path is: ")
print(shortest_path(graph, user_location, user_goal))

#total distance 
shortest_distance = shortest_path(graph, user_location, user_goal)
print("The distance to be covered is: ",dist_covered(shortest_distance))

print(wheel_chair_access(user_goal))

##TO-DO-LIST
#Distance calculations from each node
#Crowding - time of day
#multiple destinations




