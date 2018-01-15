#! usr/bin/python3.4
# -*- coding: utf-8 -*-



##### AGENT #####

class Agent:

    # Constructor
    def __init__(self, agreeableness):
        self.agreeableness = agreeableness

    # Greatings function
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + " !"




##### LOGIC #####

def main():
    agent = Agent(23)
    print(agent.say_hello("Charlie"))
    print(agent.agreeableness)

if __name__ == '__main__':
    main()

