import sys , requests
import urllib.request
from typing import final
from colorama import Fore
print()
print(Fore.LIGHTYELLOW_EX + '[#]'+ Fore.LIGHTWHITE_EX+' created by Tganga36 ... Version = 1.5')
print()
try:
    address = sys.argv[1]
except:
    print("please enter valid url or -h")
    sys.exit();
if address == '-h':
    print()
    print('''help:
                fuzzup.py [address] [wordlist] [option]
                Y = yes , save in one file : Result.txt
                N = no , dont save
                FY = yes , save and filter by status-code : Result-200.txt , Result-404.txt , Result-301.txt , Result-order.txt
                
             Options:
                dir = Find only Directorys
                normal = normal Fuzzing''') 
    print()
    sys.exit()
try:
    wordlist = sys.argv[2]
    if("/" not in wordlist):
        try:
            options = sys.argv[2]
        except:
            options = "normal"
        wordlist = "wordlist/wordlist.txt"
    else:
        try:
            options = sys.argv[3]
        except:
            options = "normal"
except:
    wordlist = "wordlist/wordlist.txt"
    try:
        options = sys.argv[2]
    except:
        options = "normal"
    pass    
check = requests.get(address)
def fuzzing():
    print()
    save = input(Fore.LIGHTYELLOW_EX + '[?]' + Fore.LIGHTWHITE_EX + 'Do you like Save it ? (Y , N , FY)' + Fore.LIGHTWHITE_EX)
    for line in open(wordlist):
        line = line.strip("\n")
        if address[-1] == '/':
            fuz = address + line
        else:
            fuz = address + '/' + line
        fuzz = requests.get(fuz)
        if options == 'normal':
            if save == 'FY' or save == 'fy':
                if fuzz.status_code == 200:
                    file200 = open('Result-200.txt' , 'a')
                    file200.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.GREEN + str(fuzz.status_code))
                elif fuzz.status_code == 404:
                    file404 = open('Result-404.txt' , 'a')
                    file404.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTRED_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.RED + str(fuzz.status_code))
                elif fuzz.status_code == 301:
                    file301 = open('Result-301.txt' , 'a')
                    file301.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTYELLOW_EX + '[!] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
                else:
                    fileorder = open('fileorder.txt' , 'a')
                    fileorder.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTYELLOW_EX + '[!] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
            elif save == 'Y' or save == 'y':
                fileResult = open('Result.txt' , 'a')
                if fuzz.status_code == 200:
                    fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.GREEN + str(fuzz.status_code))
                elif fuzz.status_code == 404:
                    fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTRED_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.RED + str(fuzz.status_code))
                elif fuzz.status_code == 301:
                    fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTYELLOW_EX + '[!] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
                else:
                    fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTYELLOW_EX + '[!] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
            elif save == 'n' or save == 'N':
                if fuzz.status_code == 200:
                    print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.GREEN + str(fuzz.status_code))
                elif fuzz.status_code == 404:
                    print(Fore.LIGHTRED_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.RED + str(fuzz.status_code))
                elif fuzz.status_code == 301:
                    print(Fore.LIGHTYELLOW_EX + '[!] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
                else:
                    print(Fore.LIGHTYELLOW_EX + '[!] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
            else:
                print()
                print(Fore.LIGHTRED_EX + '[$]' +Fore.LIGHTWHITE_EX +'please select one option')
                fuzzing()
    
        elif options == 'dir':
            if save == 'FY' or save == 'fy':
                if fuzz.status_code == 200:
                    url = urllib.request.urlopen(fuz)
                    url_sec = str(url.read())
                    if 'Index of' in url_sec:
                        file200 = open('Result-dir-200.txt' , 'a')
                        file200.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                        print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.GREEN + str(fuzz.status_code))
                    else:
                        pass
                elif fuzz.status_code == 404:
                    file404 = open('Result-dir-404.txt' , 'a')
                    file404.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTRED_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.RED + str(fuzz.status_code))
                else:
                    file404 = open('Result-dir-404.txt' , 'a')
                    file404.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTYELLOW_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
            elif save == 'Y' or save == 'y':
                fileResult = open('Result-dir.txt' , 'a')
                if fuzz.status_code == 200:
                    url = urllib.request.urlopen(fuz)
                    url_sec = str(url.read())
                    if 'Index of' in url_sec:
                        fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                        print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.GREEN + str(fuzz.status_code))
                    else:
                        pass
                elif fuzz.status_code == 404:
                    fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTRED_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.RED + str(fuzz.status_code))
                else:
                    fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                    print(Fore.LIGHTYELLOW_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
            elif save == 'n' or save == 'N':
                if fuzz.status_code == 200:
                    url = urllib.request.urlopen(fuz)
                    url_sec = str(url.read())
                    if 'Index of' in url_sec:
                        print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.GREEN + str(fuzz.status_code))
                    else:
                        pass
                elif fuzz.status_code == 404:
                    print(Fore.LIGHTRED_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.RED + str(fuzz.status_code))
                else:
                    print(Fore.LIGHTYELLOW_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
            else:
                print()
                print(Fore.LIGHTRED_EX + '[$]' +Fore.LIGHTWHITE_EX +'please select one option')
                fuzzing()
        else:
            print()
            print(Fore.LIGHTRED_EX + '[!] Your option is mistake')
            print()
            sys.exit()

fuzzing()
