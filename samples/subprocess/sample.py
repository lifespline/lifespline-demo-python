import subprocess as sp
import os

# utils
def bytes_to_string(res):
    return str(res.decode('utf-8')).strip()

print("1 - single command")
sp.run("whoami")

print("2 - save result of single command")
res = sp.run("whoami", capture_output=True)
print(bytes_to_string(res.stdout))

print("3 - save result of single command")
res = sp.check_output("whoami")
print(bytes_to_string(res))

print("4 - command with parameter")
sp.run(["echo", "hello"])

print("5 - print stdout as process is being executed")
process = sp.Popen("ls", stdout=sp.PIPE)
for line in process.stdout:
    print(bytes_to_string(line))

print("6 - execute complex command with parameters and piping")
res = sp.check_output("ls | grep sample", shell=True)
print(bytes_to_string(res))

print("7 - execute complex command with parameters and piping")
# ls | grep sample > res
ls = sp.Popen("ls", stdout=sp.PIPE)
buffer = open('res', 'wb')
grep = sp.run("grep sample".split(), stdin=ls.stdout, stdout=buffer)
os.system("cat res")
os.remove('res')

