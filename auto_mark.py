import subprocess
import os


for file in os.listdir():
    if file.endswith(".c"):
        cmd = os.path.join(file)
        resultFile = cmd[:-2] + ".txt"
        subprocess.run(["gcc",cmd]) #For Compiling
        os.system("./a.out > " + resultFile)
        mark = subprocess.run(["cmp", resultFile, "solution.txt"])
        os.remove(resultFile)
        mark = mark.returncode
        if (mark == 0):
        	print("100%")
        else:
        	print("0.0%")

        