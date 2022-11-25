import os

# list dir of interpreter
print(os.listdir())

# list dir of executed script
script_path = os.path.abspath(__file__)
script_dir_path = os.path.dirname(script_path)
print(os.listdir(script_dir_path))

# list target dir
# path is either an existing path relative to the interpreter's path
# or an absolute path.
path = '/'
print(os.listdir(path))