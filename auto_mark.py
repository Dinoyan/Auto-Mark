import subprocess
import os


for file in os.listdir():
    if file.endswith(".c"):
        cmd = os.path.join(file)
        resultFile = cmd[:-1] + "txt"
        subprocess.run(["gcc",cmd]) #For Compiling
        os.system("./a.out > " + resultFile)
