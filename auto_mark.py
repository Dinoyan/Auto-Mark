import subprocess
import os


for file in os.listdir():
    if file.endswith(".c"):
        cmd = os.path.join(file)
        resultFile = cmd[:-1] + "txt"
        subprocess.run(["gcc",cmd]) #For Compiling
        os.system("./a.out > " + resultFile)
        subprocess.run(["FC", "resultFile", "solution.txt"])
        mark = os.system("echo $?")
        if (mark ==0):
        	print("100%")
        else:
        	print("0.0%")

        