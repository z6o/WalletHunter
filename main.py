import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import time
import os
from colorama import Fore, Back
from configparser import ConfigParser
import random
import logging
import threading


def webhook_tester():
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
                "description": f"Your webhook is working.",
                "color": 0x000000,
                "footer": {
                    "text": f"WalletHunter | Webhook: {webhook}"
                }
            }
        ]
    }
    requests.post(webhook, json=embed)



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
use_threads = config['threading']['use_threads']
threads = config['threading']['threads']
checked = 0
hits = 0
os.system("cls||clear")
if log == "True":
    logging.basicConfig(filename='log.log', level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
if use_threads == "True":
    print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] Threads set to {threads}")

if webhook == "":
    w_question = input(f"[{Fore.RED}WARNING{Fore.RESET}] We couldnt find an webhook in config.ini are you sure to continue? (y/n)")
    if w_question == "n":
        exit()
else:
    print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] Founded webhook in config.ini")
if warning_message == "True":
    os.system("msg * WARNING EDUCTIONEL PURPOSES ONLY IF YOU GET CAUGHT ITS YOUR FAULT DEVS ARE NOT RESPONSIBLE FOR ANY DAMAGE!")
if webhook_test == "True":
    webhook_tester()
if proxie_scraper == "True":
    print(f"[{Fore.YELLOW}INFO{Fore.RESET}] Scraping proxies...")
    f = open("./proxies.txt", "a+")
    r = requests.get(f"https://api.proxyscrape.com/?request=displayproxies&proxytype={proxie_type}&timeout=5000")
    print(f"[{Fore.YELLOW}INFO{Fore.RESET}] Loading WalletHunter...")
    for proxy in r.text.split("\n"):
        proxy = proxy.strip()
        if proxy:
            f.write(str(proxy)+"\n")
       
        os.system("")
            
            
   
os.system("cls||clear")

def WalletHunter():
    while True:
        checked = 0
        hits = 0
        url = "https://www.bitcoinlist.io/random"
        headers = CaseInsensitiveDict()
        headers[
                "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
        if use_proxies == "True":
            req = requests.get(url, headers=headers, proxies={f"{proxie_type}": f'{proxie_type}://' + random.choice(proxies)})
        if use_proxies == "False":
            req = requests.get(url, headers=headers)
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
                        embed = {
        "avatar_url": "",
        "username": "WalletHunter",
        "content": "@everyone",
        "embeds": [
            {
                "author": {
                    "name": "WalletHunter",
                    "url": "https://github.com/z6o/WalletHunter",
                    "icon_url": ""
                },
                "description": f"Private Key: {privkey}\nUncompressed Address: {uncompaddy}\nCompressed Address: {compaddy}\nBalance: {balance}\nProxie Type: {proxie_type}",
                "color": 0x000000,
                "footer": {
                    "text": f"WalletHunter | Checked Wallets: {checked} | Hits: {hits} | Threads: {threads}"
                }
            }
        ]
    }
                        requests.post(webhook, json=embed)
                        
                        open('hits.txt', 'a+').write(f"{balance} BTC found in Adress: {compaddy} | Private Key: {privkey}")
                    os.system("cls||clear")
                os.system(f"title WalletHunter ^| Hits: {hits} ^| Threads: {threads} ^| Proxies: {use_proxies}")
                print(f"""{Fore.YELLOW}
        ██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗
        ██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
        ██║ █╗ ██║███████║██║     ██║     █████╗     ██║       ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
        ██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║       ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
        ╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║       ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
         ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                        {Fore.WHITE} v.05{Fore.RESET}
        {Fore.YELLOW}

                                        {Back.RED}:: DEVS ARE NOT RESPONSIBLE FOR ANY DAMAGE ::{Back.RESET}
                                        {Back.RED}:: SO IF SOMETHING HAPPENS ITS YUR FAULT   ::{Back.RESET}
                                                       
                                             https://github.com/z6o/WalletHunter
                        {Fore.RESET}


                            Private Key: {privkey}\r
                            Uncompressed Address: {uncompaddy}\r
                            Compressed Address: {compaddy}\r
                            Balance: {balance}\r
                            Proxie Type: {proxie_type}\r
                            Threads: {threads}\r
                            

        """)
                
                time.sleep(1)
                #os.system("cls||clear")

if use_threads == "True":
    for i in range(int(f"{threads}")):
        os.system("cls||clear")
        threading.Thread(target=WalletHunter).start()
if use_threads == "False":
    WalletHunter()