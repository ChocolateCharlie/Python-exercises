#! /usr/bin/env python3
# coding: utf-8

from os import path
import pandas as pd



class SetOfParliamentMembers:

    # Constructor
    def __init__(self, name):
        self.name = name

    # Fetch data in file
    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    # Use existing dataframe
    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    # Show circulat diagramm
    def display_chart(self):
        pass

    def split_by_political_party(self):
        result = {}
        data = self.datatframe
        all_parties = data["parti_ratt_financier"].dropna().unique()
        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset
        return result



def launch_analysis(data_file, by_party = False):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(path.join(directory, "data", data_file))
    sopm.display_chart()
    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.diplay_chart()



def main():
    pass



if __name__ == "__main__":
    launch_analysis('current_mps.csv')
