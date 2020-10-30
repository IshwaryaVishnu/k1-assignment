import os
import shutil
from os import path
def main():
    if path.exists("kloudone.py"):
        src = path.realpath("kloudone.py")
        os.rename("kloudone.py" ,"task2.py")
if __name__ == "__main__":
    main()