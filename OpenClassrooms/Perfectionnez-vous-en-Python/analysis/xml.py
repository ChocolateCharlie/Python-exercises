#! usr/bin/env python3
# coding: utf-8

from os import path
import logging as lg



def launch_analysis(data_file):
    path_to_file = path.join("data", data_file)

    file_name = path.basename(path_to_file)
    directory = path.dirname(path_to_file)
    lg.info("Opening data file {} from directoru '{}'".format(file_name, directory))

    try:
        with open(path_to_file, "r") as f:
            preview = f.readline()
            lg.debug("We managed to read the file. Here is a preview: {%s}" % preview)
    except FileNotFoundError as e:
        lg.critical("Oops ! The file was not found. Here is the original message of the exception : {%s}" % e)
    except:
        lg.critical('Destination unknown')



if __name__ == "__main__":
    launch_analysis('SyceronBrut.xml')

