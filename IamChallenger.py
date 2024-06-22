# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:50:24 2023

@author: Steven

Package it.
    To package this file, you need to install PyInstaller in the environment where it can be executed and then repackage it.
    Remember to include the '--hidden-import=win32com.client --hidden-import=psutil' flags for any required libraries.
"""

from json import loads
import sys
from os import system as cmd
import requests
from base64 import b64encode
from json import loads
from psutil import process_iter
# disable alert
import requests.packages.urllib3 as alert
alert.disable_warnings()

# detect and locate exe path
assert [proc.exe() for proc in process_iter(['pid', 'name', 'exe']) if proc.name() == "LeagueClient.exe"][0], "START CLIENT FIRST"

# Global var
LOL_PATH = [proc.exe() for proc in process_iter(['pid', 'name', 'exe']) if proc.name() == "LeagueClient.exe"][0]

def End():
    cmd('cls')
    print('                        ,\n   ,::.::::.            / `.\n ;::        `.         (  ,--.\n ,;           :   _,--\'"\\/""-.\\_\n,:             `./ ,---./( O )) `;\n;  `.           _,\'    (  `-\' ) /_.\n;   :         ,\'        \\    , (o\\\\\n ;  :         \\  \\-.  -.__--\'   \\\' )\n ;  ;         /\\ (    `-._`-._   \\/\n  \';,        ; : |      -.`._\'\\   `.\n    ;       ;  : `-.,-..  )  \\\'\\   ^.\n     ;     ;   `.__   )))\\ ) (`.\\    \\\n      ;   ;        `-`///(, \\ \\ \\)  ,ooo.\n       ;,;      ;     ``  ))))_;\'(  88888p\n        ;      ;         ((-=\'--\',-,Y8888\'\n        ;     :         ;     ,:\'-\'  `"\'\n         ;     `        ;      |\n          ;      (_   __   _,-\'\n           `---.   ;"(,-\' /                              ____\n                \\ (__/\\\\_`-.-.                     _____/\n              ,(( \'/\\/\\/\\`-;;))             ______//\n             ((\\\'\'/\\/\\/\\/\\/\\/`/\\      _____/  ____/\n             /\'/\\/\\/\\/\\/\\/\\/\\/\\/)  __/  _____/\n            (\\/\\/\\/\\/\\/\\/\\/\\/\\_/ _/ ___/\n             `-|""--"-.___,--\'|-\'__/\n               |              | /\n               |         __,--\'\n               _\\,----""\'')
    print("\n\tBye ~")
    cmd("timeout 3 /nobreak >nul")
    return sys.exit(0)

class LeagueClient:

    def __init__(self):
        global LOL_PATH
        with open(LOL_PATH.rstrip("LeagueClient.exe") + 'lockfile', 'r') as f:
            lock = f.read()
            data = lock.split(':')
            self.info          =  dict(zip(["Name", "PID", "Port", "Authorization token", "Connecton method"],data))
            self.host          =  '127.0.0.1'
            self.PID           =  data[1]
            self.port          =  data[2]
            self.method        =  data[4]
            self.authorization =  'Basic ' + b64encode(('riot:' + data[3]).encode(encoding = 'utf-8')).decode('utf-8')
            self.url_front     =  f"{self.method}://{self.host}:{self.port}"
            self.headers       =  {'Accept' : 'application/json', 'Authorization' : self.authorization}

    def request(self, mode, method_, json = {}):
        return eval(r"requests.%s"%mode)(url = self.url_front + method_, headers = self.headers, verify = False, json = json).text


    def set_rank(self, rank = 1, division = 1, type_ = 1):
        """
        set chat rank
        type_    = 1:RANKED_SOLO_5x5  2:RANKED_TFT
        rank     = 1:CHALLENGER  2:GRANDMASTER  3:MASTER  4:DIAMOND  5:PLATINUM  6:GOLD  7:SILVER  8:BRONZE  9:IRON
        division = 1:I  2:II  3:III  4:IV
        return : js.text (Str)
        """
        type_    = ['RANKED_SOLO_5x5', 'RANKED_TFT'][type_-1]
        rank     = ['CHALLENGER', 'GRANDMASTER', 'MASTER', 'DIAMOND', 'PLATINUM', 'GOLD', 'SILVER', 'BRONZE', 'IRON'][rank-1]
        division = ['I', 'II', 'III', 'IV'][division-1]
        return self.request('put', '/lol-chat/v1/me', loads('{"lol" :{"rankedLeagueDivision": "%s", "rankedLeagueQueue": "%s", "rankedLeagueTier": "%s"}}'%(division, type_, rank)))

if __name__ == '__main__':
    cmd("title=你就這? By阿毛")
    msg = """
    模式 = 1.單雙  2.戰棋
    牌位 = 1.菁英  2.宗師  3.大師  4.鑽石  5.白金  6.金牌  7.銀牌  8.銅牌  9.鐵牌
    階級 = 1.I   2.II   3.III  4.IV
    """
    print("     .-----.            .'`-.\n    /      ,--          | .- `-.\n  ,'    ,-'   `.     _.-'  ,-.`.)\n ;     /   ,=---`--+'     .- -. `.\n(   \\    ,'   =,- ,'     ( o ) | /\\\n :   :  /  =,-'  /        \\-'  ;(o :\n  \\  |     '    ;  (       `--'  \\ ;\n   \\ |        = |  \\`--+   --.    `(\n    `+       =/ :   :   `.    `.    \\\n     '      =/   \\   `--. '-.   `.   `.\n      \\    =;     `._    : ( `-.  `.   `.\n       \\  = ;        `._.'  `-.-`-._\\    `-.\n        \\= '                   _.-'_)  (::::)\n         `+      -.           `--7'  `--`..'\n          (        :    .'       ;\n           \\       |    |       /\n            \\      | _.-|  +---'\n             `--+   `.  \\   \\\n                /`.  '-.-\\   `--.\n               /    /#### `----.'\n              (  ,-'############\\\n              \\\\/###############;\n               \\###############/\n                |--------------|     _.---------\n                :::::::::::::::|_.-''\n                 ::::::::::_.-''\n       .-''..'---'-------''")
    print(msg)
    type_ =  int(input("輸入模式: "))
    rank = int(input("輸入牌位: "))
    level = int(input("輸入階級: "))
    LeagueClient().set_rank(rank, level, type_)
    End()
