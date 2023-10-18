import requests
import random
from colorama import Fore, Back, Style, init
from os import system as cmd
from art import text2art

#var list
proxyList = []
workingproxycount = 0
totalcheck = 0
timeoutCounter = 5
ascii_title = text2art("PorxySwap [ 1.2 ]\n\n\n")
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
pc = 0



#random UA
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0 Mobile Safari/537.36",
]

#Print title in rainbow
def title():
    cmd("cls")
    print(Fore.LIGHTMAGENTA_EX + ascii_title, end="\r")

#calculate %
def Percent(pc):
    for i in proxyList:
        pc = pc + 1
    prc = round((1/pc) * totalcheck, 2)
    return prc


#Check if proxies are working FUNCTION
def check_proxy(proxy, link):

    random_UA = random.choice(user_agents)
    UA_headers = {'User-Agent': random_UA}

    try:
        url_to_test = link
        
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
        print(Fore.RED + f"Error within Fuction 'check_proxy(proxy)\nError: {e}'")
        return False


#First commands
init()# Required for Colorama to work on windows
cmd("echo off")
cmd("title ProxySwap V1.2 x FuckFile >:)")

title()
proxyPath = input("Drag in you proxy.txt file: ")
title()
timeoutCounter = int(input("Timeout time (in seconds): "))
testerLink = input("default: https://www.ticketswap.com\nLeave empty to use default\n\nEnter custom link to test on: ")
if testerLink == '':
    testerLink = "https://www.ticketswap.com"
else:
    print("")

#Read Proxy file and adds to array
with open(f'{proxyPath}', 'r') as proxyFile:
    for proxy in proxyFile:
        proxyList.append(proxy.strip())


while True:
    try:
        # Loop through Proxy list to Check all
        for proxy in proxyList:
            if proxy == "":
                print(Fore.LIGHTRED_EX + "Empty line in proxy file")
            else:
                title()
                print(Fore.BLUE + f"{totalcheck} proxies checked And {workingproxycount} are working")
                print(f"{Percent(pc=pc)}%")
                totalcheck = totalcheck + 1
                if check_proxy(proxy=proxy, link=testerLink):
                    workingproxycount = workingproxycount + 1
                    with open('Working.txt', 'a') as file:
                        file.write(f"{proxy}\n")
        
                    
                    
        
    except Exception as error:
        print(Fore.RED + f"SOMETHING WHENT WRONG\nError: {error}")

    finally:
        print(Fore.YELLOW + "DONE!")
        cmd("pause")