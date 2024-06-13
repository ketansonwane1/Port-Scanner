import argparse
import threading
import socket
from colorama import Fore
import requests
print("************************************************************************************************************************************************************")
print(Fore.CYAN)

print('''      
                        $$$$$$$\                       $$\                                                                      
                        $$  __$$\                      $$ |                                                                     
                        $$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
                        $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                        $$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
                        $$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
                        $$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
                        \__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
                                                                                                |
|--------------------------------------------------------------------Coded by Ketan------------------------------------------------------------------------|
''') 

print("\n                                                    Github: https://github.com/ketansonwane1                                                          \n")

print("************************************************************************************************************************************************************")

print("\nPorts scanning is strated")
import socket
import argparse
import threading

parser = argparse.ArgumentParser(description="Port Scanner Tool")
parser.add_argument("-host", type=str, help="provide valid IP", required=True)
parser.add_argument('-p', help='provide port like 80 OR  1,443  OR 1-443 ')
a = parser.parse_args()

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        sock.close()
        print("Port {} is open".format(port))
    except:
        print("Port {} is closed".format(port))
    finally:
        sock.close()

def run_scanner(host, ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if a.p:
    ports = []
    for i in a.p.split(','):
        if '-' in i:
            sp, ep = i.split('-')
            ports.extend(range(int(sp), int(ep)+1))
        else:
            ports.append(int(i))
    run_scanner(a.host, ports)
else:
    print("Enter Valid port")
    exit()

print("--------------------------------------------------------------------Thank-you------------------------------------------------------------------------------")

