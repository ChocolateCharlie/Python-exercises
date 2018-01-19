#! usr/bin/env python3
# coding: utf-8

import argparse
import analysis.csv as c_an
import analysis.xml as x_an
import logging as lg



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Can be either CSV or XML.""")
    parser.add_argument("-d", "--datafile", help="""CSV or XML file containing pieces of information about the members of parliament""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Make the application talk !""")
    return parser.parse_args()



def main():
    args = parse_arguments()
    if args.verbose:
        lg.basicConfig(level=lg.DEBUG)
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning('You must indicate a datafile !')
        else:
            try:
                if args.extension == 'csv':
                    c_an.launch_analysis(datafile)
                elif args.extension == 'xml':
                    x_an.launch_analysis(datafile)
            except FileNotFoundError as e:
                lg.warning('Oops :( The file was not found. Here is the original message of the exception :', e)
            finally:
                lg.info('####### Analysis is over #######')
    except Warning as e:
        lg.warning(e)



if __name__ == "__main__":
    main()
