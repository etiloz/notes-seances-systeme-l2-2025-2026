import os
argv = ["ls", "-lt", "/"]
os.execvp("ls", argv)
