import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from random import choice
from playsound import playsound
from os import system as cmd

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0 Mobile Safari/537.36",
]
proxyList = []

def get_all_links(url, proxy):
    response = requests.get(url, headers=CaseInsensitiveDict({'User-Agent': choice(user_agents)}), proxies=proxy, timeout=timeout_seconds)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a["href"] for a in soup.find_all('a',{'data-testid': 'listing'}, href=True)]
        if not links:
            print("No Links Found")
        else:
            cmd(f"start Chrome {links[0]}")
            playsound('C://Users//VRK-1//Desktop//code//TSbot//files//audio//Win.wav')
            return links[0]

link = input("link: ")
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
        print("Failed")
        continue