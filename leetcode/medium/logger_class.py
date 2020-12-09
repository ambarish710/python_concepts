# Write python logger class


# import requests
# import mysql.connector
# import pandas as pd
import time
import os
import re


class Logger():
    def __init__(self, path, name, size, log_rotation_count):
        self.path = path
        self.size = size
        self.name = name
        self.log_rotation_count = log_rotation_count
        self.file_ptr_list = []
        self.file_names = []
        self.count = 0
        self.check_exists()
        if len(self.file_ptr_list) == 0:
            self.current = self.path + self.name + "_" + self.count + ".log"
            self.file_ptr_list.append(open(self.current, "w+"))
        else:
            self.count = int(re.split("[._]", self.file_names[-1])[1])

    def log(logtype, data):
        if self.file_ptr_list[-1].size() > self.size:
            self.count += 1
            self.current = self.path + self.name + self.count + ".log"
            self.file_ptr_list.append(open(self.current, "w+"))
            self.delete()
        self.file_ptr_list[-1].write("Time - {}, {} -- {}".format(time.time(), logtype, data))
        ls_output = os.system("ls -al")

    def delete(self):
        if len(self.file_ptr_list) > self.log_rotation_count:
            del self.file_ptr_list[0]
            os.system("rm {}".format(self.current))

    def check_exists():
        os.system("cd {}".format(self.path))
        ls_output = os.system("ls -lrt")
        ls_output = ls_output.split(" ")
        for line in ls_output:
            self.file_names.append(line)
            if self.name in line:
                self.file_ptr_list.append(open("{}/{}".format(self.path, line), "w+"))
