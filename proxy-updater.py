import requests
import sys
from pathlib import Path
from colorama import Fore
from configparser import ConfigParser
import argparse

config = ConfigParser()

config.read('config/config.ini')



default_type = config.get('defaults', 'proxy_type')
default_path = config.get('defaults', 'path')
default_chain = config.get('defaults', 'chain_type')

additional_proxies = Path("config/additional_proxies.txt").read_text()




parser = argparse.ArgumentParser(description = "OPTIONS: ")
parser.add_argument('-t', '--type', metavar='', required=False, type = str, help='Specify a proxy type (all, http, socks4, socks5')
parser.add_argument('-p', '--path', metavar='', required=False, type = str, help='Specify a path to proxychains config file')
parser.add_argument('-c', '--chain', metavar='', required=False, type=str, help='Specify a chain type (dynamic, random)')
argument = parser.parse_args()
status = False


def add_proxies(proxy_type, path, chain_type):

    if proxy_type == 'all':
        http_master = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
        socks4_master = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt"
        socks5_master = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
        http = requests.get(http_master)
        socks4 = requests.get(socks4_master)
        socks5 = requests.get(socks5_master)
        proxy = "\n" + http.text + "\n" + socks4.text + "\n" + socks5.text 
        length = proxy.count("\n")
    elif proxy_type == 'http' or proxy_type == 'socks4' or proxy_type == 'socks5':
        master = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/{}.txt".format(proxy_type)
        proxy = requests.get(master)
        proxy = "\n" + proxy.text
        length = proxy.count("\n")


    proxy = proxy.replace("\n", "\nraw ")
    proxy = proxy.replace(":", " ")
    proxy = "#" + proxy_type + "\n" + proxy
    
    print("Added", length, proxy_type, "proxies")

    if chain_type == 'dynamic':
        beginning = Path("config/proxychains_dynamic.txt").read_text()
    elif chain_type == 'random':
        beginning = Path("config/proxychains_random.txt").read_text()
    else:
        print('Invalid type!')
        quit
    
    with open(path, "w") as conf:
        conf.writelines(beginning)
        conf.close()
    with open(path, "a") as conf:
        conf.writelines("\n\n\n#Additional proxies:\n")
        conf.writelines(additional_proxies)
        conf.writelines("\n\n\n#Proxies:\n")
        conf.writelines(proxy)
        conf.close()

    



    
    


def proxy_updater():
    print(Fore.BLUE + """ 
    
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗                
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝                
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝                 
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝                  
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║                   
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝ """ + Fore.YELLOW + """                  
                                                          
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗ 
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                          
    """)




def main():

    proxy_updater()

    print(Fore.WHITE)

    if argument.type:
        proxy_type = argument.type
    else:
        proxy_type = default_type
        print("No type specified, using default type:", default_type)
    if argument.path:
        config_path = argument.path
    else:
        config_path = default_path
        print("No path specified, adding proxies to default file:", default_path)
    if argument.chain:
        chain_type = argument.chain
    else:
        chain_type = default_chain
        print("No chain type specified, using default chain type:", default_chain)
    
    add_proxies(proxy_type, config_path, chain_type)

    


if __name__ == "__main__":
    main()
    