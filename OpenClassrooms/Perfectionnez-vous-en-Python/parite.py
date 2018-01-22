#! usr/bin/env python3
# coding: utf-8

import argparse
import analysis.csv as c_an
import analysis.xml as x_an
import logging as lg

lg.basicConfig(level=lg.DEBUG)



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Can be either CSV or XML.""")
    parser.add_argument("-d", "--datafile", help="""CSV or XML file containing pieces of information about the members of parliament""")
    parser.add_argument("-p", "--byparty", action='store_true', help="""Displays a graph for each political party""")
    parser.add_argument("-i", "--info", action='store_true', help="""Information about the file""")
    parser.add_argument("-n", "--displaynames", action='store_true', help="""displays the names of all the mps""")
    parser.add_argument("-s", "--searchname", help="""search for a mp name""")
    parser.add_argument("-I", "--index", help="""displays information about the Ith mp""")
    parser.add_argument("-g", "--groupfirst", help="""displays a graph groupping all the 'g' biggest political parties""")
    return parser.parse_args()



def main():
    args = parse_arguments()
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning('You must indicate a datafile !')
    except Warning as e:
         lg.warning(e)
    else:
        if args.extension == 'csv':
            c_an.launch_analysis(datafile, args.byparty, args.info, args.displaynames, args.searchname, args.index, args.groupfirst)
        elif args.extension == 'xml':
            x_an.launch_analysis(datafile)
    finally:
         lg.info('####### Analysis is over #######')



if __name__ == "__main__":
    main()
