import subprocess
 
cmd = "HelloWorld.c"
# Example
# cmd = HelloWorld.c
print ("Hey this is Python Script Running\n")
subprocess.run(["gcc",cmd]) #For Compiling
subprocess.run("./a.out") 
result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
print(result.returncode, result.stdout, result.stderr)

#end thats all