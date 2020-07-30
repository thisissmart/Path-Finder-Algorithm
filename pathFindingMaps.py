import random

class Building:
    def __init__(self, name, access):
        self.name = name
        self.access = access
               

class Environment(object):
    locations_maps = ['Gate', 'Administration', 'Village', 'Mainlab', 'LilianK']

    maps = {   "Gate" : 'Administration ' 'Villages',
               "Administration" : 'Villages ' 'LilianK',
               "Villages" : 'Administration Mainlab Gate',
               "LilianK" : 'Administration Cafeteria',
               "Mainlab" : 'Cafeteria ChandariaSchool Villages'
            }

    myheuristics = {
        "Gate" : ["Gate", "Village"],
        "Administration" : ["Administration", "Villages"],
        "Villages" : ["3","3"],
        "LilianK" : ["4","3"],
        "Mainlab" : ["2","2"]
    }

    location = random.choice(locations_maps)
    goal = random.choice(locations_maps)

class Agent(Environment):    
    print("Random Location is here: ", Environment.location)
    print("Random Goal is here: ", Environment.goal)

    def get_distances(goal, location):
        distance = Environment.location - Environment.goal
        

    if Environment.location == "Gate":
        print("These are the buildings closest to you. ",Environment.maps["Gate"])
    elif Environment.location == "Administration":
        print("These are the buildings closest to you. ",Environment.maps["Administration"])
    elif Environment.location == "Villages":
        print("These are the buildings closest to you. ",Environment.maps["Villages"])
    elif Environment.location == "LilianK":
        print("These are the buildings closest to you. ",Environment.maps["LilianK"])
    elif Environment.location == "Mainlab":
        print("These are the buildings closest to you. ",Environment.maps["Mainlab"])

    
theEnvironment = Environment()
theAgent = Agent(theEnvironment)

    
