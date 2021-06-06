import threading
import time
from colorama import init, Fore
import ctypes
import string
import random

init(convert=True)
ctypes.windll.kernel32.SetConsoleTitleW("Amazon Gift Card Generator By Sqwares#4767")
text = '''
▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄▄▄ ..▄▄ ·      ▄▄ • ▄▄▄ . ▐ ▄ 
██· █▌▐█▐█ ▀█ ▀▄ █·▀▄.▀·▐█ ▀.     ▐█ ▀ ▪▀▄.▀·•█▌▐█
██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄▄▌▐█▄▪▐█    ▐█▄▪▐█▐█▄▄▌██▐█▌
 ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪
'''

print(Fore.RED + text + Fore.WHITE)
f = open('amazon_codes.txt', 'a')
print()
print(Fore.RED + 'Enter amount of codes to generate: ')
amount = int(input())
fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=13))
    f.write(code.upper() + '\n')
    print(Fore.GREEN + code.upper())
    fix += 1
    ctypes.windll.kernel32.SetConsoleTitleW("Generated Codes: " + str(fix) + "/" + str(amount))