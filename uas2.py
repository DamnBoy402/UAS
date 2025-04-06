import os
import requests
import random
import time
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import pyfiglet

os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    cols = os.get_terminal_size().columns
    logo = pyfiglet.figlet_format("UAS", font="slant")
    judul = "User Agent Scraper"
    auth = "Authored by DamnBoy402"
    team = "Powered by NoxLeviathan"
    
    centered = '\n'.join([line.center(cols) for line in logo.split('\n')])
    
    print("\n" + centered)
    print(judul.center(cols))
    print(auth.center(cols))
    print(team.center(cols) + "\n")

banner()

def s1():
    ualist = []
    try:
        r = requests.get('http://useragentstring.com/pages/useragentstring.php?name=All', timeout=20)
        sop = BeautifulSoup(r.text, 'html.parser')
        for li in sop.find_all('li'):
            if li.a:
                ualist.append(li.a.text.strip())
    except:
        pass
    return ualist

def s2():
    agents = []
    try:
        for page in range(1, 6):
            r = requests.get(f'https://www.whatismybrowser.com/guides/the-latest-user-agent/page/{page}', timeout=15)
            sop = BeautifulSoup(r.text, 'html.parser')
            for code in sop.find_all('code'):
                agents.append(code.text)
    except:
        pass
    return agents

def s3():
    try:
        data = requests.get('https://www.useragents.me/api', timeout=10).json()
        return [ua['ua'] for ua in data['data']]
    except:
        return []

def s5():
    uas = []
    try:
        r = requests.get('https://www.advancedwebranking.com/useragents.txt', timeout=10)
        uas = r.text.splitlines()
    except:
        pass
    return uas

def skrp5():
    ualist = []
    try:
        for _ in range(3):
            r = requests.get('https://jnrbsn.github.io/user-agents/user-agents.json', timeout=15)
            ualist.extend(json.loads(r.text))
    except:
        pass
    return ualist

def s6():
    try:
        r = requests.get('https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt')
        return r.text.split('\n')
    except:
        return []

def scrap7():
    agents = []
    try:
        r = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/', timeout=10)
        sop = BeautifulSoup(r.text, 'html.parser')
        for td in sop.select('td.useragent'):
            agents.append(td.text.strip())
    except:
        pass
    return agents

def s8():
    try:
        r = requests.get('https://fake-useragent.herokuapp.com/browsers/0.1.11', timeout=15)
        data = r.json()
        return [browser['userAgent'] for browser in data['browsers']['chrome']]
    except:
        return []

def s9():
    uas = []
    try:
        for _ in range(5):
            res = requests.get('https://www.useragentgenerator.com/history.json', timeout=10)
            uas.extend([x['useragent'] for x in res.json()])
    except:
        pass
    return uas

def s10():
    try:
        r = requests.get('https://cdn.jsdelivr.net/gh/tamimibrahim17/UserAgents@main/user_agents.json', timeout=20)
        return json.loads(r.text)
    except:
        return []

def scraper():
    allua = set()
    scraptor = [
        s1, s2, s3,
        s5, skrp5, s6,
        scrap7, s8, s9,
        s10
    ]
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(func) for func in scraptor]
        for future in as_completed(futures):
            try:
                hasil = future.result()
                if hasil:
                    allua.update(hasil)
            except:
                continue
    return list(allua)

jmlh = int(input("[?] Enter the number of user agents required > "))
sv = input("[?] Save to txt file? (y/n) > ").lower().strip() == 'y'

print("\n[+] Wait...")
mula = time.time()
end = scraper()
random.shuffle(end)
end = end[:jmlh]

if sv:
    with open('useragents.txt', 'w') as f:
        f.write('\n'.join(end))
    print(f"\n[!] {len(end)} user agent successfully saved to useagents.txt")
else:
    print("\n" + "\n".join(end))

print(f"\n[!] Total execution time {time.time() - mula:.2f} sec")
print("[!] Operation completed adios\n")

# Special Thanks To:
# - Noxs404
# - ChiroXploit404
# - FkzSec
# - Darkness
# - Leviathan404CyberTeam
# - Always Mikaelz
# - Fem|301
# - YhujinOS
# - Laten Cyber
# - Zull
# - HyperXclic!
# - NoTolerance - Ilham
# - C10F - Darkness
# - Lucia
# - Nia
# - TC20
# - Doom3r
# - Zhan
# - Sastra
# And all contributors
# You are free to recode this tool, but don't forget to include the original developer!
# Copyright©2025 UAS - UserAgent Scrapper
# Respect me as developer!