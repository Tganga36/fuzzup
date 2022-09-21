from audioop import add
import sys , requests
from urllib.parse import urlparse
from typing import final
from colorama import Fore
print()
print(Fore.LIGHTYELLOW_EX + '[#]'+ Fore.LIGHTWHITE_EX+' created by mrhack125 ... Version = 1.1')
print()
address = sys.argv[1]
if address == '-h':
    print()
    print('''help:
                fuzzup.py [address] [wordlist]
                Y = yes , save in one file : Result.txt
                N = no , dont save
                FY = yes , save and filter by status-code : Result-200.txt , Result-404.txt , Result-301.txt , Result-order.txt''') 
    print()
    sys.exit()
wordlist = sys.argv[2]    
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
            if fuzz.status_code == 200:
                fileResult = open('Result.txt' , 'a')
                fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.GREEN + str(fuzz.status_code))
            elif fuzz.status_code == 404:
                fileResult = open('Result.txt' , 'a')
                fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                print(Fore.LIGHTRED_EX + '[$] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.RED + str(fuzz.status_code))
            elif fuzz.status_code == 301:
                fileResult = open('Result.txt' , 'a')
                fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                print(Fore.LIGHTYELLOW_EX + '[!] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
            else:
                fileResult = open('Result.txt' , 'a')
                fileResult.write(f'[+] {fuz} | {str(fuzz.status_code)}\n')
                print(Fore.LIGHTYELLOW_EX + '[!] ' + Fore.LIGHTWHITE_EX + fuz + '|' + Fore.YELLOW + str(fuzz.status_code))
        elif save == 'n' or 'N':
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
    file200.close() , file404.close() , file301.close() , fileorder.close()

fuzzing()