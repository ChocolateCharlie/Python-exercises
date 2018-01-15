#! usr/bin/python3.4
# -*- coding: utf-8 -*-

import json
import math

##### POSITION #####

class Position:

    # Constructor
    def __init__(self, longitude_degrees, latitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees
    
    # Latitude is in radian
    @property
    def latitude(self):
        return self.latitude_degrees * math.pi /180

    # Longitude is in radian
    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180



##### AGENT #####

class Agent:

    # Constructor
    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)



##### LOGIC #####

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        print(agent.position.longitude)
        print(agent.position.latitude)

if __name__ == '__main__':
    main()

