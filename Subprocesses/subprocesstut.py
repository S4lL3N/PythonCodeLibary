import subprocess as subp

subp.run('dir', shell= True)
#saves the data from the command in a variable
p1 = subp.run("cd ..;ls -la", shell=True, capture_output=True)
# will print out the output of the command in formatted text
print(p1.stdout.decode())

#will write output of console/ terminal to a file 
with open("Python\Subprocesses\output.txt", 'w') as f:
    p1 = subp.run("dir", shell=True, stdout=f, text=True)

