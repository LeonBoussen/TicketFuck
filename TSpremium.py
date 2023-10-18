import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from random import choice
import winsound
from os import system as cmd
from colorama import Fore, Back, Style, init



user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0 Mobile Safari/537.36",
]

proxyList = []

cRed = Fore.RED
cBlue = Fore.BLUE
cgreen = Fore.GREEN
cMagenta = Fore.MAGENTA



def errorLog(error):
    with open("Error Log.txt", 'a') as file:
        file.write(str(error) + '\n\n\n')

def get_all_links(url, proxy):
    # Send GET request to url using custom headers/User-Agent and proxy. Timeout is input from user
    response = requests.get(url, headers=CaseInsensitiveDict({'User-Agent': choice(user_agents)}), proxies=proxy, timeout=timeout_seconds)
    print(cMagenta + f"response code: {response.status_code}")

    # Check if response code is 200(if website propperly accepted the GET request)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser') # get html code from response
        links = [a["href"] for a in soup.find_all('a',{'data-testid': 'listing'}, href=True)] # Search html for listings
        if not links:
            # No listing found
            print(cBlue + "No listed tickets Found")
        else:
            # if tciket listing is found open in chrome and closes all instences of it self to prefent a block
            print(cgreen + f"Ticket found {links[0]}")
            cmd(f"start Chrome {links[0]}")
            winsound.PlaySound("*", winsound.SND_ALIAS)
            winsound.PlaySound("*", winsound.SND_ALIAS)
            cmd("pause")
            return links[0]
        
    else:
        try:
            soup = BeautifulSoup(response.text, 'html.parser') # get html code from response
            links = [a["href"] for a in soup.find_all('a',{'data-testid': 'listing'}, href=True)] # Search html for listings
            if not links:
                # No listing found
                print(cBlue + "No listed tickets Found")
            else:
                # if tciket listing is found open in chrome and closes all instences of it self to prefent a block
                print(cgreen + f"Ticket found {links[0]}")
                cmd(f"start Chrome {links[0]}")
                winsound.PlaySound("*", winsound.SND_ALIAS)
                winsound.PlaySound("*", winsound.SND_ALIAS)
                cmd("pause")
                return links[0]
        
        except:
            print(cRed + f"Error: {response.status_code}")




#Program
cmd("title TicketSwipe V2.3")
print(cMagenta + "TicketSwipe V2.3")
link = input(cgreen + "link: ")
proxyPath = input("Enter proxy file: ")
timeout_seconds = int(input("Timeout: "))

with open(f'{proxyPath}', 'r') as proxyFile:
    for proxy in proxyFile:
        proxyList.append(proxy.strip())

while True:

    proxy_url = choice(proxyList)
    proxy_dict = {
        "http": proxy_url,
        "https": proxy_url,
    }

    headers = {
        'User-Agent': choice(user_agents),
        'Accept': "application/json",
        'Content-Type': "application/json",
    }
    try:
        print(get_all_links(link, proxy=proxy_dict))
    except:
        print(cRed + f"proxy failed: {proxy_dict}")
        #proxyList.remove(proxy_url)
        #print(f"proxy removed.\nCurrent List:\n{proxyList}")
        continue
