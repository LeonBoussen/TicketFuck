import requests
import random
from colorama import Fore, Back, Style, init
from os import system as cmd

#var list
proxyList = []
workingproxies = []
workingproxycount = 0
totalcheck = 0
timeoutCounter = 5

#random UA
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0 Mobile Safari/537.36",
]

#First commands
cmd("echo off")
cmd("title ProxySwap V1.1 x FuckFile >:)")
cmd("cls")
proxyPath = input(Fore.MAGENTA + "Drag in you proxy.txt file: ")
timeoutCounter = int(input("Timeout time (in seconds): "))



#Read Proxy file and adds to array
with open(f'{proxyPath}', 'r') as proxyFile:
    for proxy in proxyFile:
        proxyList.append(proxy.strip())

#Check if proxies are working FUNCTION
def check_proxy(proxy):

    random_UA = random.choice(user_agents)
    UA_headers = {'User-Agent': random_UA}

    try:
        url_to_test = "https://www.ticketswap.com"
        
        # Define proxy settings
        proxies = {
            "http": proxy,
            "https": proxy,
        }
        
        # Send a GET request using a random UA, Proxy and checks with timeout of 5 sec
        response = requests.get(url_to_test, headers=UA_headers, proxies=proxies, timeout=timeoutCounter)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False

# Loop through Proxy list to Check all
for proxy in proxyList:
        if proxy == "":
            print(Fore.LIGHTBLACK_EX + "Empty line in proxy file")
        else:
            print(Fore.BLUE + f"{totalcheck} proxies checked And {workingproxycount} are working")
            totalcheck = totalcheck + 1
            if check_proxy(proxy=proxy):
                print(Fore.GREEN + f"Proxy {proxy} is working!")
                workingproxycount = workingproxycount + 1
                workingproxies.append(proxy)
        
                #write working proxies to txt file in same directory as executable
                with open("Working-ProxyLineByLine.txt", 'a') as file:
                    file.write(str(proxy) + '\n')
            else:
                print(Fore.RED + f"Proxy {proxy} is not working.")

print(Fore.YELLOW + " DONE!")
quit()