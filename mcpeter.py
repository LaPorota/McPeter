import subprocess
import random
import time
import re
from tqdm import tqdm


print("")
print("")
print("")

print(" /$$      /$$  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$ ")
print("| $$$    /$$$ /$$__  $$ /$$__  $$| $$__  $$| $$_____/|__  $$__/| $$_____/| $$__  $$")
print("| $$$$  /$$$$| $$  \ $$| $$  \__/| $$  \ $$| $$         | $$   | $$      | $$  \ $$")
print("| $$ $$/$$ $$| $$$$$$$$| $$      | $$$$$$$/| $$$$$      | $$   | $$$$$   | $$$$$$$/")
print("| $$  $$$| $$| $$__  $$| $$      | $$____/ | $$__/      | $$   | $$__/   | $$__  $$")
print("| $$\  $ | $$| $$  | $$| $$    $$| $$      | $$         | $$   | $$      | $$  \ $$")
print("| $$ \/  | $$| $$  | $$|  $$$$$$/| $$      | $$$$$$$$   | $$   | $$$$$$$$| $$  | $$")
print("|__/     |__/|__/  |__/ \______/ |__/      |________/   |__/   |________/|__/  |__/   by Pedro Orlando")
                                                                                   
print("")
print("")
print("")
print("")
print("")
print("")                                                                                 




def mac_gen():

    new_mac= "00:" + str(random.randint(10,99)) + ":" + str(random.randint(10,99)) + ":" + str(random.randint(10,99)) + ":" + str(random.randint(10,99))
    return str(new_mac)

interface =""

while interface == "":    
    
    print("1 - eth0")
    print("2 - wlan0")
    print("3 - tun0")

    entrada_interface = input("Choose your interface: ")
    if entrada_interface == "1":
        interface = "eth0"
    elif entrada_interface == "2":
        interface = "wlan0"
    elif entrada_interface == "3":
    	interface = "tun0"
    else:

        print("Wrong interface, choose it again.")


print("")
print("")   
print("selected interface :" + interface)

while 1:
    print("[+]Changin MAC adress for " + interface)
    mac_cambiante = mac_gen()
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + mac_cambiante, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    print("")
    print("")   
    for i in tqdm(range(100)):
    	time.sleep(0.01)
    print("")
    print("")   
    print("[+] Mac replaced successfully.")
    print("-This mac will be refreshed in 240 seconds.")
    time.sleep(240)



    



