import platform
import os
import multiprocessing
import getpass
import datetime
print("name of os is : ",os.name)
print("platform system is : ",platform.system())
print("platform release is : ",platform.release())
print("current file name is : ",os.path.realpath(__file__))
print("count cpu is : ",multiprocessing.cpu_count())
print("username is : ",getpass.getuser())
print("current time is : ",datetime.datetime.now().time())
