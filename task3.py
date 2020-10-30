import os
import shutil
cwd = os.getcwd()
print("Current Directory:", cwd)
script = os.path.realpath(__file__)
print("Script path:", script)
print(os.listdir())
try:
   file_Name = 'task3.py'
   f = open(file_Name, 'r')
   text = f.read()
   f.close()
except IOError:
   print('Not accessed or problem in reading: ' + file_Name)