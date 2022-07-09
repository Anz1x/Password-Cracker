#!/usr/bin/env python3

import hashlib
import colorama
import time
import os
import sys
from colorama import Fore

colorama.init(autoreset=True)

print(f"""
{Fore.LIGHTGREEN_EX}╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ╔═╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
╠═╝├─┤└─┐└─┐││││ │├┬┘ ││  ║  ├┬┘├─┤│  ├┴┐├┤ ├┬┘
╩  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘  ╚═╝┴└─┴ ┴└─┘┴ ┴└─┘┴└─
{Fore.RESET}===============================================
""")

time.sleep(1)

hash_alg = str(input(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTYELLOW_EX} Hash Algorithm ({Fore.LIGHTGREEN_EX}MD5{Fore.LIGHTYELLOW_EX}, {Fore.LIGHTGREEN_EX}SHA-1{Fore.LIGHTYELLOW_EX}, {Fore.LIGHTGREEN_EX}SHA256 {Fore.LIGHTYELLOW_EX}are supported): " + Fore.LIGHTGREEN_EX))
passwd_list = str(input(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTYELLOW_EX} Path to Password file: " + Fore.LIGHTGREEN_EX))

if os.path.exists(passwd_list) == False:
    print(Fore.RED + "[-] Unable to locate the file/path")
    sys.exit(1)

hashed_passwd = str(input(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTYELLOW_EX} Hashed Password: " + Fore.LIGHTGREEN_EX))

with open(passwd_list, "r") as file:
    for line in file.readlines():
        # MD5
        if hash_alg == "md5" or hash_alg == "MD5":
            hash_obj = hashlib.md5(line.strip().encode('utf-8'))
            password = hash_obj.hexdigest()
            if password == hashed_passwd:
                print(f"\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTYELLOW_EX} Found the MD5 Password: {Fore.LIGHTGREEN_EX + line.strip()}")

        # SHA-1        
        if hash_alg == "sha1" or hash_alg == "SHA1" or hash_alg == "SHA-1" or hash_alg == "sha-1":
            hash_obj = hashlib.sha1(line.strip().encode('utf-8'))
            password = hash_obj.hexdigest()
            if password == hashed_passwd:
                print(f"\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTYELLOW_EX} Found the SHA-1 Password: {Fore.LIGHTGREEN_EX + line.strip()}")

        # SHA256       
        if hash_alg == "sha256" or hash_alg == "SHA256":
            hash_obj = hashlib.sha256(line.strip().encode('utf-8'))
            password = hash_obj.hexdigest()
            if password == hashed_passwd:
                print(f"\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTYELLOW_EX} Found the SHA256 Password: {Fore.LIGHTGREEN_EX + line.strip()}")
