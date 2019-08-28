# -*- coding: utf-8 -*-

import platform
import pip
import os
import sys
import requests
import pkgutil
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style


def main():
    os.system("cls")
    ver = platform.python_version()
    architecture = platform.architecture()
    system = platform.platform()
    processor = platform.processor()
    implementation = platform.python_implementation()
    pip_ver = pip.__version__
    packages_num = sys.modules.__len__()


    python_art = [
        Fore.BLUE + "          ,.:;!!!;:.,                " + Fore.BLUE + "Python:                " + Fore.YELLOW + ver,
        Fore.BLUE + "         !!!O:::::!!!                " + Fore.BLUE + "Python implementation: " + Fore.YELLOW + implementation,
        Fore.BLUE + "         !:::::;;;;::                " + Fore.BLUE + "Pip:                   " + Fore.YELLOW + pip_ver,
        Fore.BLUE + "   ,,,,,.......!!!!!!" + Fore.YELLOW + " !!;;::.,       " + Fore.BLUE + "Pip packages:          " + Fore.YELLOW + str(packages_num),
        Fore.BLUE + "  !!!::::::;;;;;;;;;;" + Fore.YELLOW + " !!;;::::.,     ",
        Fore.BLUE + " !!!::::::::;;;;:::::" + Fore.YELLOW + " !!;;:::::::    " + Fore.BLUE + "Operating System:      " + Fore.YELLOW + system,
        Fore.BLUE + "!!!:::::;;;:'''''''' " + Fore.YELLOW + ".;;;;;:;;;;;    " + Fore.BLUE + "Architecture:          " + Fore.YELLOW + architecture[0],
        Fore.BLUE + "!!!::;::::" + Fore.YELLOW + "  ,.::::;;;:::::::;;;;;;   " + Fore.BLUE + "Processor:             " + Fore.YELLOW + processor,
        Fore.BLUE + " !!!!:::::" + Fore.YELLOW + "  ::::::::::::::::::;;;    ",
        Fore.BLUE + "  !!!:::::" + Fore.YELLOW + "  ;;;;;;;`````````````     ",
        Fore.YELLOW + "            !::::::::;!!             ",
        Fore.YELLOW + "            !::::::;O!!!             ",
        Fore.YELLOW + "            `':;!!!;:'`              "
    ]


    for i in python_art:
        print(i)

    print(Fore.WHITE, "\n[1]Show packages list    [2]Find module description    [3]Exit")
    select = int(input("Enter option number: ")) 
    if select == 1:
        print_packages()
    elif select == 2:
        pypi_scrapping()
    elif select == 3:
        exit()
    else: 
        os.system("pause")
        os.system("cls")
        main()


def print_packages():
    for i, value in enumerate(pkgutil.iter_modules()):
        print(Fore.YELLOW, "[", i + 1, "]", Fore.WHITE, value.name)
    os.system("pause")
    os.system("cls")
    main()


def pypi_scrapping():
    name = str(input("Enter module name: "))
    try:
        response = requests.get("https://pypi.org/project/{}".format(name))

        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'html.parser')
            output = html.find(class_="project-description")
            print("\n\n", Fore.BLUE, name, Fore.YELLOW, "PyPi Description")
            print(Fore.WHITE, output.text)
            os.system("pause")
            os.system("cls")
            main()
        elif response.status_code == 404:
            print(Fore.RED, "Error 404: No module named %s in PyPi. Please check spelling." % name)
            os.system("pause")
            os.system("cls")
            main()
        else:
            print(Fore.RED, "Unknown Error: Something went wrong.")
            os.system("pause")
            os.system("cls")
            main()


    except requests.exceptions.ConnectionError:
        print("Error 404: no internet connection.")

if __name__ == "__main__":
    main()
