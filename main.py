from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style, init
from time import sleep as delay
from datetime import datetime as time
from os import system as cmd
import random





#variables
proxyList = []

#console colors
cGreen = Fore.GREEN
cRed = Fore.RED
cMagenta = Fore.MAGENTA
cBlue = Fore.BLUE

#random UA list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0 Mobile Safari/537.36",
]





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






#Functions
#Error handling + Error to log in local dir
def errorLog(error):
    with open("Error Log.txt", 'a') as file:
        file.write(str(error) + '\n\n\n')

#program main
def checkTicket(link):
    #Scope variables
    ticketlinks = []
    proxyForGet = random.choice(proxyList)



    #Setup - browser/antibot
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server=%s" % proxyForGet) #Add the proxy as argument 
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") #Adding argument to disable the AutomationControlled flag 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) #Exclude the collection of enable-automation switches 
    chrome_options.add_experimental_option("useAutomationExtension", False) #Turn-off userAutomationExtension
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=chrome_options)#Add set options to Chrome
    random_UA = random.choice(user_agents) #Getting Random UA
    browser.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": random_UA}) #Using choisen UA
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") #Changing the property of the navigator value for webdriver to undefined 
    browser.get(link)


    #initial info
    cmd("cls")
    print(cBlue + "Browser setup complete")
    print(cBlue + f"using proxy: {proxyForGet} with User-Agent: {random_UA}")

 
#Trying to find ticket listings

    tickets = browser.find_elements(By.CSS_SELECTOR, 'a[data-testid="listing"]')
    print("Listing found")
    
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
        gglogin = browser.find_element(By.CSS_SELECTOR, 'input[aria-label="E-mailadres of telefoonnummer"]')
        #facebook = WebDriverWait(browser, timeout=timeout_seconds).until(EC.element_to_be_clickable(fblogin))
        print(Fore.GREEN + "Google login button found")
        delay(3)
        gglogin.click()
        delay(timeout_seconds)
        gEmail = browser.find_element(By.CLASS_NAME, 'whsOnd')
        gEmail.send_keys("f4ckbot@gmail.com")
        gNext = browser.find_element(By.CSS_SELECTOR, "div.VfPpkd-RLmnJb")
        gNext.click()
        delay(1)
        gPass = browser.find_element(By.NAME, "Passwd")
        gPass.send_keys("3Monsterjam!?")
        gNext.click()
        delay(timeout_seconds)
        TicketToCard = browser.find_element(By.CLASS_NAME, "css-obhtex.e1dvqv261")
        TicketToCard.click()
        delay(5)
        idealButton = browser.find_element(By.ID, "STRIPE_MONEY_MACHINE_IDEAL")
        idealButton.click()
        delay(5)
        rabobank = browser.find_element(By.ID, "rabobank")
        rabobank.click()
        delay(5)
        checkoutButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].css-obhtex.e1dvqv261')
        checkoutButton.click()
        delay(10)
        country = browser.find_element(By.ID, "wrapper-phoneCountry")
        country.click()
        delay(2)
        nederland = browser.find_element(By.ID, ":r1:-149")
        nederland.click()
        phone = browser.find_element(By.ID, "phoneNumber")
        phone.send_keys("0637612945")
        
        


        #print("fb cookie clicked")
        #fbcookie.click()
        

while True:
    try:
        checkTicket(link)
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        errorLog(f"Error occured at {time.now()}!\nError info:\nProxy: {proxy}\n{e}\n\n--------------------------------")
    finally:
        print(Fore.YELLOW + "Loop done!")
        
        
