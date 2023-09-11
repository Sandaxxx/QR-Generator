from colorama import Fore
import os
import qrcode
import time

banner="""
   ___  ___     ___   _   __  __     ___ ___ _  _ 
  / _ \| _ \   |   \ /_\  \ \/ /    / __| __| \| |
 | (_) |   /   | |) / _ \  >  <    | (_ | _|| .` |
  \__\_\_|_\   |___/_/ \_\/_/\_\    \___|___|_|\_|
                                    crédit: Sandax
                                                                                      
"""
print(Fore.BLUE+banner)

urltext = input(Fore.YELLOW + "[+] Enter The URL/TEXT: "+ Fore.BLUE)
file_name = input(Fore.YELLOW + "[+] Enter the Name of Output File: "+ Fore.BLUE)
def gen_qr():
    qr = qrcode.make(urltext)
    qr.save(file_name+'.png')
gen_qr()
os.system('cls')
print(Fore.GREEN + "[!] QR Code Generated -",file_name)
time.sleep(4)

