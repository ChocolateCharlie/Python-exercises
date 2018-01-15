#! usr/bin/python3.4
# -*- coding: utf-8 -*-

import json

##### AGENT #####

class Agent:

    # Constructor
    def __init__(self, **agent_attributes):
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)



##### LOGIC #####

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        agent = Agent(**agent_attributes)
        print(agent.agreeableness)

if __name__ == '__main__':
    main()

