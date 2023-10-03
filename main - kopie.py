from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style, init
from time import sleep as delay
from os import system as cmd

import random

#todo
#1. facebook button wait unity clickable

#variables
proxyList = []

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0 Mobile Safari/537.36",
]

cGreen = Fore.GREEN
cRed = Fore.RED
cMagenta = Fore.MAGENTA
cBlue = Fore.BLUE

#Setup
cmd("title TicketFuck v1 - FuckFile")
cmd("cls")
print(cMagenta + "Welcome to TicketFuck v1\n\n\n")
link = input("Enter Event Link: ")
proxyPath = input("Enter proxy file: ")
timeout_seconds = int(input("Timeout: "))
cmd("cls")


#Read Proxy file and adds to array
with open(f'{proxyPath}', 'r') as proxyFile:
    for proxy in proxyFile:
        proxyList.append(proxy.strip())

def errorLog(error):
    with open("Error Log.txt", 'a') as file:
        file.write(str(error) + '\n\n\n')

def checkTicket(link):
    #Scope variables
    ticketlinks = []

    proxyForGet = random.choice(proxyList)

    #Browser setup - 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server=%s" % proxyForGet) # Add the proxy as argument 
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") # Adding argument to disable the AutomationControlled flag 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # Exclude the collection of enable-automation switches 
    chrome_options.add_experimental_option("useAutomationExtension", False) # Turn-off userAutomationExtension
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=chrome_options)

    random_UA = random.choice(user_agents) # Getting Random UA
    browser.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": random_UA}) # Using choisen UA
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") # Changing the property of the navigator value for webdriver to undefined 
    browser.get(link)


    cmd("cls")
    print(cBlue + "Browser setup complete")
    print(cBlue + f"using proxy: {proxyForGet} with User-Agent: {random_UA}")

 
    #Trying to find a ticket
    try:

        """"
        #checks if website loads within the timeout time
        try:
            print("Website Loading time check")
            checkLoading = browser.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div[5]/button[2]')
            timeoutCheck = WebDriverWait(browser, timeout=timeout_seconds).until(EC.element_to_be_clickable(checkLoading))
            print("Website loaded")
        except Exception as e:
                print(f"Page did not load within {timeout_seconds} seconds. Error: {str(e)}")
        """

        tickets = browser.find_elements(By.CSS_SELECTOR, 'a[data-testid="listing"]')
        print("Listing found")
    except Exception as e:
        if not e == 0:
            print(cRed + f"Error: {e}")
            errorLog(e)
            browser.quit|()
            return
        else:
            print(f"page took longer then {timeout_seconds} secondes to load")
            browser.quit()
            return


    
    for ticket in tickets:
        print(Fore.GREEN + ticket.text)
        tLink = ticket.get_attribute("href")
        ticketlinks.append(tLink)


        #Swtitching to new ticket page
        ticket.send_keys(Keys.CONTROL + Keys.RETURN)
        browser.switch_to.window(browser.window_handles[1])
        buyButton = browser.find_element(By.CLASS_NAME, "css-17jso0u")
        buyButton.click()
        delay(2)


        #Open facebook login page
        #facebook = browser.find_element(By.XPATH, '/html/body/ticketswap-portal[9]/div/div/div/div/div/div/div/button[2]')
        fblogin = browser.find_element(By.XPATH, '/html/body/ticketswap-portal[9]/div/div/div/div/div/div/div/button[2]')
        #facebook = WebDriverWait(browser, timeout=timeout_seconds).until(EC.element_to_be_clickable(fblogin))
        print(Fore.GREEN + "Facebook login button found")
        delay(3)
        r = True
        if r == True:
            print(cGreen + "Ticket found!")
        fblogin.click()
        delay(500000)
        #print("facebook click")
        #fbcookie = browser.find_element(By.XPATH, '//*[@id="u_0_h_ OF"]')
        #print("fb cookie clicked")
        #fbcookie.click()
        

while True:
    try:
        checkTicket(link)
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        errorLog(e)
    finally:
        print(Fore.YELLOW + "Loop done!")
        
        
