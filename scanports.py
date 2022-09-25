import socket
from colorama import Fore
import colorama
from threading import *
import sys
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

colorama.init()
banner = """
$$$$$$\   $$\                         $$\       $$\ 
\_$$  _|  $$ |                        $$ |      \__|
  $$ |  $$$$$$\    $$$$$$\   $$$$$$$\ $$$$$$$\  $$\ 
  $$ |  \_$$  _|   \____$$\ $$  _____|$$  __$$\ $$ |
  $$ |    $$ |     $$$$$$$ |$$ /      $$ |  $$ |$$ |
  $$ |    $$ |$$\ $$  __$$ |$$ |      $$ |  $$ |$$ |
$$$$$$\   \$$$$  |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |$$ |
\______|   \____/  \_______| \_______|\__|  \__|\__|
                                                    
                                                    
                                                    
 $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\              
$$  __$$\ $$ | $$  |$$  __$$\ $$  __$$\             
$$ /  $$ |$$ |$$  / $$ /  $$ |$$ |  $$ |            
$$$$$$$$ |$$$$$  /  $$$$$$$$ |$$$$$$$  |            
$$  __$$ |$$  $$<   $$  __$$ |$$  __$$<             
$$ |  $$ |$$ |\$$\  $$ |  $$ |$$ |  $$ |            
$$ |  $$ |$$ | \$$\ $$ |  $$ |$$ |  $$ |            
\__|  \__|\__|  \__|\__|  \__|\__|  \__|                                                            
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    def main():
        targetip = input("Target IP\n> ")
        print("_" * 50+"\n")
        print("::Scan starting::")
        print("Scanning started at:",datetime.now())
        print("_" * 50)
        

        def scan(target,port):
            try:
                sock.connect((target,port))
                socket.setdefaulttimeout(0.5)
                sock.close()
                return True
            except:
                return False


        for portnum in range(1,65535):
            if scan(targetip,portnum) == True:
                print(Fore.GREEN+"[*] Port {} is open.".format(portnum)+Fore.WHITE)
            else:
                print(Fore.RED+"[*] Port {} is close.".format(portnum)+Fore.WHITE)
        print("Finished at:",datetime.now())
    print(Fore.RED+banner+Fore.WHITE)
    t1 = Thread(target=main)
    t1.start()
    t1.join()
except KeyboardInterrupt:
    print("\nExiting.")
    sys.exit()