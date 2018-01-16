#! usr/bin/python3.4
# -*- coding: utf-8 -*-

import json
import math

##### ZONE #####

class Zone:
    
    # Attributes
    # Grid size values
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    # Zone size
    WIDTH_DEGREES = 1
    HEIGHT_DEGREES = 1
    # List of zones
    ZONES = []

    # Constructor
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []

    # The population is the number of inhabitants
    @property
    def population(self):
        return len(self.inhabitants)

    # Initialize the list of zones
    @classmethod
    def initialize_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)

    # Compute the index of the ZONES array that contains a given position
    @classmethod
    def find_zone_that_contains(cls, position):
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES) / cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        zone_index = latitude_index * longitude_bins + longitude_index
        # Check the zoning is correct before returning zone
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)
        return zone

    # Test for a given position if it belongs to the zone
    def contains(self, position):
        return  position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
                position.longitude <= max(self.corner1.longitude, self.corner2.longitude) and \
                position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
                position.latitude <= max(self.corner2.latitude, self.corner2.latitude)
    
    # Add an inhabitant to the zone
    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)



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
    Zone.initialize_zones()
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        print("Zone population: ", zone.population)

if __name__ == '__main__':
    main()

