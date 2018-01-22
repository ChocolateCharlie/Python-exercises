#! usr/bin/env python3
# coding: utf-8

from os import path
import logging as lg

import pandas as pd



class SetOfParliamentMember:

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
        # Get the data
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]
        # Do the proportions (will be diplayed in pie chart)
        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps=counts.sum()
        proportions=counts/nb_mps
        # Create labels
        labels = ["Female ({})".format(counts[0]), "Male({})".format(counts[1])]
        # Draw pie chart
        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f%%"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()


    def split_by_political_party(self):
        result = {}
        data = self.datatframe
        all_parties = data["parti_ratt_financier"].dropna().unique()
        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMember('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset
        return result

    def total_mps(self):
        return len(self.dataframe)

    def __repr__(self):
        return "SetOfParliamentMember: {} members".format(len(self.dataframe))



def launch_analysis(data_file, by_party = False):
    sopm = SetOfParliamentMember("All MPs")
    sopm.data_from_csv(path.join("data", data_file))
    sopm.display_chart()
    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.diplay_chart()
    if info:
        print(repr(sopm))



def main():
    pass



if __name__ == "__main__":
    launch_analysis('current_mps.csv')
