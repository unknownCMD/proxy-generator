import datetime 
import os
import ctypes
import webbrowser

try:
    import requests
except: 
    pass
try:
    from console.utils import set_title
except:
    pass
try:
    from colorama import Fore, init
    init()
except:
    pass

date = datetime.datetime.today()
month = date.month
day = date.day
year = date.year

hour = date.hour
minutes = date.minute
seconds = date.second

http = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
socks4 = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all'
socks5 = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'

text = r'''
██╗░░░██╗███╗░░██╗██╗░░██╗███╗░░██╗░█████╗░░██╗░░░░░░░██╗███╗░░██╗░█████╗░███╗░░░███╗██████╗░
██║░░░██║████╗░██║██║░██╔╝████╗░██║██╔══██╗░██║░░██╗░░██║████╗░██║██╔══██╗████╗░████║██╔══██╗
██║░░░██║██╔██╗██║█████═╝░██╔██╗██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░╚═╝██╔████╔██║██║░░██║
██║░░░██║██║╚████║██╔═██╗░██║╚████║██║░░██║░░████╔═████║░██║╚████║██║░░██╗██║╚██╔╝██║██║░░██║
╚██████╔╝██║░╚███║██║░╚██╗██║░╚███║╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║╚█████╔╝██║░╚═╝░██║██████╔╝
░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝╚═════╝░
{}'''.format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTMAGENTA_EX, Fore.MAGENTA, Fore.MAGENTA, Fore.MAGENTA, Fore.RESET)

class Scraper:
    def __init__(self, scrape):
        self.scrape = scrape

    def HTTPScraper():
        https = requests.get(http).text
        try:
            with open(f'Oluşturulan Proxyler/HTTP-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{(https)}{Fore.WHITE} Proxyler Oluşturuldu! {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Tipi: {Fore.LIGHTCYAN_EX}HTTP/s{Fore.RESET}')
                os.system('pause>nul')
        except:
            os.mkdir('Oluşturulan Proxyler')
            with open(f'Oluşturulan Proxyler/HTTP-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proxyler Oluşturuldu! Lütfen yeni proxy oluşturmadan önce eski listeyi siliniz. {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Tipi: {Fore.LIGHTCYAN_EX}HTTP/s{Fore.RESET}')
                os.system('pause>nul')

    def SOCKS4Scraper():
        https = requests.get(socks4).text
        try:
            with open(f'Oluşturulan Proxyler/SOCKS4-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proxyler Oluşturuldu!  {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Tipi: {Fore.LIGHTCYAN_EX}SOCKS4{Fore.RESET}')
                os.system('pause>nul')
        except:
            os.mkdir('Oluşturulan Proxyler')
            with open(f'Oluşturulan Proxyler/SOCKS4-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proyler Oluşturuldu!  {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}SOCKS4{Fore.RESET}')
                os.system('pause>nul')

    def SOCKS5Scraper():
        https = requests.get(socks4).text
        try:
            with open(f'Oluşturulan Proxyler/SOCKS5-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proyler Oluşturuldu!  {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}SOCKS5{Fore.RESET}')
                os.system('pause>nul')
        except:
            os.mkdir('Oluşturulan Proxyler')
            with open(f'Oluşturulan Proxyler/SOCKS5-{month}-{day}-{year}-{hour}-{minutes}-{seconds}.txt', 'w') as txt_file:
                for line in https.split('\n'):
                    txt_file.write(line)
                print(f' [{Fore.LIGHTMAGENTA_EX}+{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}{len(https)}{Fore.WHITE} Proyler Oluşturuldu!  {Fore.LIGHTMAGENTA_EX}-{Fore.WHITE} Type: {Fore.LIGHTCYAN_EX}SOCKS5{Fore.RESET}')
                os.system('pause>nul')

if __name__ == '__main__':
    set_title('unknownCMD - Ana Menü.')
    print(text)
    print(f' [{Fore.LIGHTMAGENTA_EX}-{Fore.WHITE}] Oluşturmak istediğiniz proxy türü nedir?{Fore.RESET}\n\n')
    print(f' [{Fore.LIGHTMAGENTA_EX}1{Fore.WHITE}] HTTP/HTTPS{Fore.RESET}')
    print(f' [{Fore.LIGHTMAGENTA_EX}2{Fore.WHITE}] SOCKS4{Fore.RESET}')
    print(f' [{Fore.LIGHTMAGENTA_EX}3{Fore.WHITE}] SOCKS5{Fore.RESET}')
    print(f'\n [{Fore.LIGHTMAGENTA_EX}!{Fore.WHITE}] Seçiminiz: ', end='')
    scraper = input('')

    if (scraper) == '1':
        Scraper.HTTPScraper()
    elif (scraper) == '2':
        Scraper.SOCKS4Scraper()
    elif (scraper) == '3':
        Scraper.SOCKS5Scraper()