import os
from colorama import Fore
import time
from subprocess import Popen
def banner():
    os.system("clear")
    print("")
    Popen('neofetch')
    time.sleep(2)


def show_menu():
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" PILIH SATU DARI OPSI RAT \n")
    time.sleep(0.1)
    print(Fore.RED+" [0]"+Fore.WHITE+" Dapatkan Data base "+Fore.YELLOW+"[Tanpa izin akses korban]\n")
    time.sleep(0.1)
    print(Fore.RED+" [1]"+Fore.WHITE+" Dapatkan Geolokasi TRGL "+Fore.GREEN+"[HANDPHONE]\n")
    time.sleep(0.1)
    print(Fore.RED+" [2]"+Fore.WHITE+" Akses Kamera Korban \n") 
    time.sleep(0.1)
    print(Fore.RED+" [3]"+Fore.WHITE+" Akses Perekaman Suara Korban \n")
    time.sleep(0.1)
    print(Fore.RED+" [4]"+Fore.WHITE+" Keluar 0101010101 . . .\n")
