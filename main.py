# -*- coding: utf-8 -*-

import platform
import pip
import sys
from termcolor import colored

ver = platform.python_version()
architecture = platform.architecture()
pip = pip.__version__
packages = sys.modules.__len__()

print(
colored("           ,.:;!!!;:.,", "blue"), colored("                        Python:            ", "blue"), colored(ver, "yellow"), "\n",
colored("         !!!()::::!!!", "blue"), colored("                        Pip:               ", "blue"), colored(pip, "yellow"), "\n",
colored("         !:::::;;;;::", "blue"), colored("                        Pip packages:      ", "blue"), colored(packages, "yellow"), "\n",
colored("   ,,,,,.......!!!!!!", "blue"), colored("                        Operating System:  ", "blue"), colored(architecture[1], "yellow"), "\n",
colored("  !!!::::::;;;;;;;;;;", "blue"), colored("!!;;::::.,", "yellow"),  colored("             Arhitecture:       ", "blue"), colored(architecture[0], "yellow"), "\n",
colored(" !!!::::::::;;;;:::::", "blue"), colored("!!;;:::::::\n", "yellow"),
colored("!!!:::::;;;:''''''''", "blue"), colored(".;;;;;:;;;;;\n", "yellow"),
colored("!!!::;::::", "blue"),  colored(",.::::;;;:::::::;;;;;;\n", "yellow"),
colored(" !!!!:::::", "blue"),  colored("::::::::::::::::::;;;\n", "yellow"),
colored("  !!!:::::", "blue"),  colored(";;;;;;;`````````````\n", "yellow"),
colored("           !::::::::;!!\n", "yellow"),
colored("           !::::::()!!!\n", "yellow"),
colored("            `':;!!!;:'`\n", "yellow"))