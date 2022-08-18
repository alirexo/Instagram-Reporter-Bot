# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
    ███     ██       ██       ███  ████████   ███      ████████       ███      ██    ██ 
   ██ ██    ██       ██      ██ ██    ██     ██ ██     ██     ██     ██ ██     ██  ██   
  ██   ██   ██       ██     ██   ██   ██    ██   ██    ████████     ██   ██    ████     
 █████████  ██       ██    ████████   ██   █████████   ██     ██   █████████   ██  ██   
██       ██ ████████ ██   ██      ██  ██  ██       ██  ████████   ██       ██  ██    ██

Instagram Repoeter 
Powerd By Aliatabak In june 2019      """
def print_logo():
    print(Fore.BLUE + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.YELLOW + " Robot Is Ready To Work "+ Style.RESET_ALL + Style.BRIGHT)
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)