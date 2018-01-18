#! usr/bin/env python3
# coding: utf-8

import argparse
import analysis.csv as c_an
import analysis.xml as x_an



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Can be either CSV or XML.""")
    parser.add_argument("-d", "--datafile", help="""CSV or XML file containing pieces of information about the members of parliament""")
    return parser.parse_args()



def main():
    args = parse_arguments()
    datafile = args.datafile
    if args.extension == 'csv':
        c_an.launch_analysis(datafile)
    elif args.extension == 'xml':
        x_an.launch_analysis(datafile)



if __name__ == "__main__":
    main()
