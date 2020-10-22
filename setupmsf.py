import os, sys

os.system('pkg update && pkg upgrade')
os.system('chmod 777 metasploit.sh')
os.system('./metasploit.sh')
print("Installation Completed")
