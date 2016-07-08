import platform
import commands
import os
import subprocess

score = 0 #if score reaches 3 or higher, we assume virtual

'''
Determine the operating system the program is running on
'''
def determine_os():
    if platform.system() ==  "Linux":
        #we know the platform is linux, test linux commands
        ubuntu_dmesg()     
    elif platform.system() == "Windows":
        #we know the platform is win, test win commands
        windows_sysinfo()
    else:               
        #the platform is something else, abort program
        quit()

'''
Run the Ubuntu dmesg command to check for hypervisor
'''
def linux_dmesg():
    dmesg = commands.getstatusoutput("dmesg |grep -i hypervisor")
    if(dmesg[0]==0):
        if(dmesg[1][:34] == "[    0.000000] Hypervisor detected"):
            score += 1 #add to score, as hypervisor was detected
        else:
            score += 0 #no hypervisor detected, may not be vm
    else:
        score += 0

def windows_sysinfo():
    sysinfo = subprocess.Popen(["systeminfo"])
    print sysinfo
    os.system("pause")

determine_os()