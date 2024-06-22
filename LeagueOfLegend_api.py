import sys
import inspect
import requests
from time import sleep
from base64 import b64encode
# from os import system as cmd
from bs4 import BeautifulSoup
from msvcrt import getch, kbhit
from collections import Counter
from json import loads, dumps, dump
from win32com.client import Dispatch
from psutil import process_iter
# disable alert
import requests.packages.urllib3 as alert
alert.disable_warnings()

# detect and locate exe path
assert [proc.exe() for proc in process_iter(['pid', 'name', 'exe']) if proc.name() == "LeagueClient.exe"][0], "START CLIENT FIRST"


# Global var
# LOL_PATH = [p.Properties_[7].Value for p in GetObject('winmgmts:').InstancesOf('Win32_Process') if p.Properties_("Name").Value == "LeagueClient.exe"][0]
LOL_PATH = [proc.exe() for proc in process_iter(['pid', 'name', 'exe']) if proc.name() == "LeagueClient.exe"][0]
# LOL_PATH = r"C:\Riot Games\League of Legends"
join_room_members = 5

# DEBUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
def cmd(var):
    return
# DEBUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

def End():
    cmd('cls')
    print(Pic().sid_run)
    print(f'\n{c("Bye~", 34)}')
    sleep(3)
    return sys.exit(0)

def c(text, pattern = '0'):
    """
    font back color
    30   40   Black
    31   41   Red
    32   42   Green
    33   43   Magenta
    34   44   Blue
    35   45   Purple
    36   46   Cyan
    37   47   White gray
    4 dash
    just work in terminal.
    """
    return f'\033[{pattern}m{text}\033[0m'

def dict_find(find, dic):
    """
    search a item wherever it is
    return : Str/null
    """
#    dict(zip(list(dic.values()), list(dic.keys())))    # reverse key and value
    rt = ''
    for k,v in dic.items():
        if k == find:
            rt = v
        if v == find:
            rt = k
    return rt

def js_beauty(json):
    """
    return a beautiful js dictionary
    return : Str
    """
    return dumps(json, indent = 4, ensure_ascii = False)

def find_list_most_frequent_strs(input_list):
    cleaned_list = [item for item in input_list if item is not None and item != ""]
    if len(cleaned_list) == 0:
        raise EmptyListError
    string_count = Counter(cleaned_list)
    max_count = max(string_count.values())
    most_frequent_strings = [string for string, count in string_count.items() if count == max_count]
    return most_frequent_strings

def find_consecutive_value(list_, reverse=False):
    if reverse:
        list_.reverse()
    count = 0
    for i in list_:
        if i != list_[0]:
            break
        count += 1
    return count, list_[0]

def get_dict(dict_, keys, rt_preset=None):
    key = keys[0]
    if len(keys) == 1:
        try:
            rt = dict_.get(key)
        except:
            rt = rt_preset
        return rt
    else:
        next_level = dict_.get(key, {})
        return get_dict(next_level, keys[1:])

class EmptyListError(Exception):
    def __init__(self):
        current_function_name = inspect.currentframe().f_back.f_code.co_name
        super().__init__(f'"{current_function_name}" function can\'t input empty list!')



class Pic:

    def __init__(self):
        self.squirrel_fool          = "                         .-.\n                        |/`\\\\.._\n     _..._,,--.         `\\ /.--.\\ _.-. \n  ,/'  ..:::.. \\     .._.-'/    \\` .\\/ \n /       ...:::.`\\ ,/:..| |(o)  / /o)|\n|:..   |  ..:::::'|:..  ;\\ `---'. `--'\n;::... |   .::::,/:..    .`--.   .:.`\\_\n |::.. ;  ..::'/:..   .--'    ;\\   :::.`\\\n ;::../   ..::|::.  /'          ;.  ':'.---.\n  `--|    ..::;\\:.  `\\,,,____,,,/';\\. (_)  |)\n     ;     ..::/:\\:.`\\|         ,__,/`;----'\n     `\\       ;:.. \\: `-..      `-._,/,_,/\n       \\      ;:.   ). `\\ `>     _:\\\n        `\\,  ;:..    \\ \\ _>     >'"
        self.squirrel_mad           = '              ___                     \n        .-""""   ".                   \n       /         __\'-.                \n      ;      ..sssSSSS;               \n      ;   ;           ;               \n       \'.\'  ..sssSSSSSS;              \n       ;        """"""";              \n      ;    ...ssssSSSSS;              \n      ;          """""";              \n      ;               ;               \n      ;     ....sssSS/                \n      ;          """/                 \n       ;          .\'                  \n       ;    .-""""-.                  \n        \'-.\'  _..ssS,                 \n        .\'  ""  _..sSs                \n       /__    ""  _.sSS.              \n     .-"" `-.   ___     ; _           \n    /_..gg$$$pp\'___`.   .\' `>.        \n  ,s$$$$$$$$$B;"   `;"";  .\' ;        \n :$$$$$$$$$$P"`._():   `-`_O.\'        \n:$$$$$$$$$P              \'   `-.      \n$$$$$$$$$"    _,,-.       :     ;     \n$$$$$$$$!b.._g$$$$$$-.     ;    `.    \n:$$$$$$$$$$$$$$$$$$P j\\    :_.._/     \n T$$$$$$$$$$$$$$$$P  | :    ;         \n  "T$$$$$$$$$$$$P";  ;_;    :         \n    "^T$$$$$$P^"; : //:   __!         \n        | |     : ; `.: .mMMM:        \n        ) :_    ) \'-.   \'MMMP\'        \n        `.i_;I  \'-._i.\''
        self.squirrel_watching_you  = "     .-----.            .'`-.\n    /      ,--          | .- `-.\n  ,'    ,-'   `.     _.-'  ,-.`.)\n ;     /   ,=---`--+'     .- -. `.\n(   \\    ,'   =,- ,'     ( o ) | /\\\n :   :  /  =,-'  /        \\-'  ;(o :\n  \\  |     '    ;  (       `--'  \\ ;\n   \\ |        = |  \\`--+   --.    `(\n    `+       =/ :   :   `.    `.    \\\n     '      =/   \\   `--. '-.   `.   `.\n      \\    =;     `._    : ( `-.  `.   `.\n       \\  = ;        `._.'  `-.-`-._\\    `-.\n        \\= '                   _.-'_)  (::::)\n         `+      -.           `--7'  `--`..'\n          (        :    .'       ;\n           \\       |    |       /\n            \\      | _.-|  +---'\n             `--+   `.  \\   \\\n                /`.  '-.-\\   `--.\n               /    /#### `----.'\n              (  ,-'############\\\n              \\\\/###############;\n               \\###############/\n                |--------------|     _.---------\n                :::::::::::::::|_.-''\n                 ::::::::::_.-''\n       .-''..'---'-------''"
        self.squirrel_watching_sky  = '                        ,\n   ,::.::::.            / `.\n ;::        `.         (  ,--.\n ,;           :   _,--\'"\\/""-.\\_\n,:             `./ ,---./( O )) `;\n;  `.           _,\'    (  `-\' ) /_.\n;   :         ,\'        \\    , (o\\\\\n ;  :         \\  \\-.  -.__--\'   \\\' )\n ;  ;         /\\ (    `-._`-._   \\/\n  \';,        ; : |      -.`._\'\\   `.\n    ;       ;  : `-.,-..  )  \\\'\\   ^.\n     ;     ;   `.__   )))\\ ) (`.\\    \\\n      ;   ;        `-`///(, \\ \\ \\)  ,ooo.\n       ;,;      ;     ``  ))))_;\'(  88888p\n        ;      ;         ((-=\'--\',-,Y8888\'\n        ;     :         ;     ,:\'-\'  `"\'\n         ;     `        ;      |\n          ;      (_   __   _,-\'\n           `---.   ;"(,-\' /                              ____\n                \\ (__/\\\\_`-.-.                     _____/\n              ,(( \'/\\/\\/\\`-;;))             ______//\n             ((\\\'\'/\\/\\/\\/\\/\\/`/\\      _____/  ____/\n             /\'/\\/\\/\\/\\/\\/\\/\\/\\/)  __/  _____/\n            (\\/\\/\\/\\/\\/\\/\\/\\/\\_/ _/ ___/\n             `-|""--"-.___,--\'|-\'__/\n               |              | /\n               |         __,--\'\n               _\\,----""\''
        self.sid_run                = '                        .-.\n                _.--"""".o/         .-.-._\n             __\'   ."""; {        _J ,__  `.\n            ; o\\.-.`._.\'J;       ; /  `- /  ;\n            `--i`". `" .\';       `._ __.\'   |\n                \\  `"""   \\         `;      :\n                 `."-.     ;     ____/     /\n                   `-.`     `-.-\'    `"-..\'\n     ___              `;__.-\'"           `.\n  .-{_  `--._         /.-"                 `-.\n /    ""T    ""---...\'  _.-""   """-.         `.\n;       /                 __.-"".    `.         `,             _..\n \\     /            __.-""       \'.    \\          `.,__      .\'L\' }\n  `---"`-.__    __."    .-.       j     `.         :   `.  .\' ,\' /\n            """"       /   \\     :        `.       |     F\' \\   ;\n                      ;     `-._,L_,-""-.   `-,    ;     `   ; /\n                       `.       7        `-._  `.__/_        \\/\n                         \\     _;            \\  _.\'  `-.     /\n                          `---" `.___,,      ;""        \\  .\'\n                                    _/       ;           `"\n                                 .-"     _,-\'\n                                {       "";\n                                 ;-.____.\'`.\n                                  `.  \\ \'.  :\n                                    \\  : : /\n                                     `\':/ `'
        self.sid_stand              = '                             ,--.""\n                      __,----( o ))\n                    ,\'--.      , (\n             -"",:-(    o ),-\'/  ;\n               ( o) `o  _,\'\\ / ;(\n                `-;_-<\'\\_|-\'/ \'  )\n                    `.`-.__/ \'   |\n       \\`.            `. .__,   ;\n        )_;--.         \\`       |\n       /\'(__,-:         )      ;\n     ;\'    (_,-:     _,::     .|\n    ;       ( , ) _,\':::\'    ,;\n   ;         )-,;\'  `:\'     .::\n   |         `\'  ;         `:::\\\n   :       ,\'    \'            `:\\\n   ;:    \'  _,-\':         .\'     `-.\n    \';::..,\'  \' ,        `   ,__    `.\n      `;\'\'   / ;           _;_,-\'     `.\n            /            _;--.          \\\n          ,\'            / ,\'  `.         \\\n         /:            (_(   ,\' \\         )\n        /:.               \\_(  /-. .:::,;/\n       (::..                 `-\'\\ "`""\'\n       ;::::.                    \\        __\n       ,::::::.            .:\'    )    ,-\'  )\n      /  `;:::::::\'`__,:.:::\'    /`---\'   ,\'\n     ;    `""""\'   (  \\:::\'     /     _,-\'\n     ;              \\  \\:\'    ,\';:.,-\'\n     (              :  )\\    (\n      `.             \\   \\    ;\n        `-.___       : ,\\ \\  (\n           ,\',\'._::::| \\ \\ \\  \\\n          (,(,---;;;;;  \\ \\|;;;)\n                      `._\\_\\'
        self.noob                   = '\n         ｜/／\n\u3000\u3000\u3000／￣￣￣＼\n\u3000 \u3000/ ⊙ \u3000\u3000\u3000\\\n\u3000∠︳\u3000\u3000\u3000\u3000   \\\n\u3000\u3000︳\u3000\u3000\u3000＿＿＿＼＿\n\u3000 \u3000\\\u3000\u3000（＿＿／ _／\n\u3000\u3000\u3000＼\u3000\u3000\u3000\u3000＿＞ 菜雞 哈哈\n\u3000\u3000\u3000\u3000爪︶︶爪'

class OPGG:

    def __init__(self, summoners_list):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
        self.url_find = r"https://www.op.gg/summoners/tw/{summoner_name}"
        self.url_get_recent = r"https://op.gg/api/v1.0/internal/bypass/summoners/tw/{summoner_id}/most-champions/{gametype}"
        self.summoners_list = summoners_list
        self.summoners_dict = {}
        self.set_summoners_dict()

    def parse_webs_summoner_info(self, data, summoner_id):
        summoner_info = {
                            'summoner_id': summoner_id,
                            'summoner_name': None,
                            'win_rate': None,
                            'recent_most_tier': None,
                            'kda_average': None,
                            'recent_most_gameplay_type': None,
                            'consecutive_win-lose': None,
            }

        win_rate_list = []
        recent_most_tier_list = []
        kda_average_dict = {'k':0, 'd':0, 'a':0, 'count':0}
        recent_most_gameplay_type_list = []

        for i in data:
            win_rate_list.append(get_dict(i, ['myData', 'stats', 'result']))
            recent_most_tier_list.append(get_dict(i, ['average_tier_info', 'tier']))
            for j in i['participants']:
                try:
                    if get_dict(j, ['summoner', 'summoner_id']) == summoner_id:
                        kda_average_dict['k'] += get_dict(j, ['stats', 'kill'])
                        kda_average_dict['d'] += get_dict(j, ['stats', 'death'])
                        kda_average_dict['a'] += get_dict(j, ['stats', 'assist'])
                        kda_average_dict['count'] += 1
                        # print(kda_average_dict['count'])
                except:
                    summoner_name = get_dict(data[0], ['myData', 'summoner', 'name'])
                    print(c(f"\n召喚師名稱: {summoner_name}\n召喚師ID: {summoner_id}\n", "31;47"))
                    with open('errordata.json', 'w', encoding='utf-8') as f:
                        f.write(str(data))
                        raise
            recent_most_gameplay_type_list.append(get_dict(i, ['queue_info', 'game_type']))

        summoner_info['summoner_name'] = get_dict(data[0], ['myData', 'summoner', 'name'])
        summoner_info['win_rate'] = f"{win_rate_list.count('WIN')/len(win_rate_list)*100.0:.1f}"
        summoner_info['recent_most_tier'] = find_list_most_frequent_strs(recent_most_tier_list)
        summoner_info['kda_average'] = f"{kda_average_dict['k']/kda_average_dict['count']:.1f}/{kda_average_dict['d']/kda_average_dict['count']:.1f}/{kda_average_dict['a']/kda_average_dict['count']:.1f}"
        summoner_info['recent_most_gameplay_type'] = find_list_most_frequent_strs(recent_most_gameplay_type_list)
        summoner_info['consecutive_win-lose'] = find_consecutive_value(win_rate_list)

        return summoner_info

    def parse_web_summoner_played_champions(self, summoner_id, season_id):
        norm_ranked_dict = {}
        for gametype in ["normal", f'rank?game_type=RANKED&season_id={season_id}']:
            response = requests.get(self.url_get_recent.format(summoner_id=summoner_id, gametype=gametype), headers=self.headers)
            json = loads(response.text)
            json_game_type = get_dict(json, ['data', 'game_type'])
            champ_played_list = get_dict(json, ['data', 'champion_stats'])
            norm_ranked_dict[json_game_type] = champ_played_list
        return norm_ranked_dict

    def get_opgg_summoner_info(self, summoner_name):
        response = requests.get(self.url_find.format(summoner_name=summoner_name), headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        json = loads(soup.find('script', {'id': '__NEXT_DATA__'}).string)
        data = get_dict(json, ['props', 'pageProps', 'games', 'data'])
        season_list = get_dict(json, ['props', 'pageProps', 'data', 'seasons'])
        for i in season_list:
            if not get_dict(i, ['is_preseason']):
                season_id = get_dict(i, ['id'])
        try:
            current_tier = get_dict(json, ['props', 'pageProps', 'data', 'previous_seasons'])[0]['tier_info']['tier']
            current_tier += ' ' + str(get_dict(json, ['props', 'pageProps', 'data', 'previous_seasons'])[0]['tier_info']['division'])
        except IndexError:
            current_tier = "UNRANKED"
            pass
        summoner_id = get_dict(json, ['props', 'pageProps', 'data', 'summoner_id'])

        summoner_info = self.parse_webs_summoner_info(data, summoner_id)
        summoner_info['current_tier'] = current_tier
        summoner_info['champs_played'] = self.parse_web_summoner_played_champions(summoner_id, season_id)
        # print(f"{summoner_info = }")
        return summoner_info

    def set_summoners_dict(self):
        for i in self.summoners_list:
            # print("key: {i}, value: {self.get_opgg_summoner_info(i)}") # debug
            self.summoners_dict[i] = self.get_opgg_summoner_info(i)

    def get_champ_played_res(self, summoner_name, champion_id):
        rt = []
        for k,v in self.summoners_dict[summoner_name]["champs_played"].items():
            if k != None:
                for i in v:
                    if get_dict(i, ['id']) == champion_id:
                        played_total = int(get_dict(i, ['play']))
                        win_total = int(get_dict(i, ['win']))
                        rt.append({"type": k, "played_total": played_total, "win_rate": f"{(win_total/played_total)*100.0:.1f}"})
        return rt

    def __str__(self):
        rt = ""
        for i in self.summoners_dict:
            rt += f"{get_dict(self.summoners_dict, [i, 'summoner_name'])}, 近20場勝率: {get_dict(self.summoners_dict, [i, 'win_rate'])}, KDA: {get_dict(self.summoners_dict, [i, 'kda_average'])}"
        return rt

class DDragon:

    def __init__(self, CLIENT_VER, area = 'tw'):
        # from json import loads , dumps, dump
        try:
            with open("data/ddragon.json", "r") as f:
                data = loads(f.read())
                # data['v'] = "xxx.xxx.xxx", CLIENT_VER = "xxx.xxx.xxx.xxx.xxx"
                if "".join(data['v'].split('.')[0:2]) != "".join(CLIENT_VER.split('.')[0:2]):
                    raise Exception("VERSION_ERROR")
        except:
            data = requests.get(f'https://ddragon.leagueoflegends.com/realms/{area}.json').json()
            with open("data/ddragon.json", "w+") as f:
                dump(data, f)
                print(f'{c("Download JSON(DDragon) file Done!", "42;4")}')
        self.ver               =  data['v']
        self.language          =  data['l']
        self.cdn               =  data['cdn']

    def get_versions(self):
        """
        return all versions
        return : List
        """
        return requests.get(self.cdn.strip('cdn') + r"api/versions.json").json()

    def get_champions(self, ver = None):
        """
        it will return all champions in given version
        return : Dict
        """
        try:
            if ver is None:
                ver = self.ver
                name = ''.join(self.ver.split('.')[0:2])
            else:
                name = ver
            with open(f"data/{name}_champions.json", "r") as f:
                champs = loads(f.read())
        except:
            champs = requests.get(self.cdn + f'/{ver}/data/{self.language}/champion.json').json()['data']
            with open(f"data/{name}_champions.json", "w+") as f:
                dump(champs, f)
                print(f'{c("Download JSON(champions) file Done!", "42;4")}')
        ch = {}
        for i in champs:
            ch[int(champs[i]['key'])] = champs[i]['name']
        return dict([(i,ch[i]) for i in sorted(ch.keys())])


class LeagueClient:

    def __init__(self):
        global LOL_PATH
        with open(LOL_PATH.rstrip("LeagueClient.exe") + r'\lockfile', 'r') as f:
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
            self.ver           =  [Dispatch("Scripting.FileSystemObject").GetFileVersion(LOL_PATH)][0]
            # ddragon
            self.champions     =  DDragon(self.ver).get_champions()
            # OPGG
            self.OPGG          =  None

    def stlog(self, msg, status = True, end = '', sep = '', flush = False):
        if status:
            print(f"\r{c('狀態', 36)} : {c(msg, 35)}{' '*10}", end = '', sep = sep, flush = flush)
        else:
            print(f'{msg}')
        return

    def request(self, mode, method_, json = {}):
        return eval(r"requests.%s"%mode)(url = self.url_front + method_, headers = self.headers, verify = False, json = json).text

    def chat(self, text, type_ = 'celebration'):
        """
        type_         = ['championSelect', 'celebration', 'chat']
        color         = [     'gray'     ,    'yellow'  , 'chat']
        visible       = [    'unknow'    ,      'no'    , 'yes' ]
        """
        self.request("post", r"/lol-chat/v1/conversations/%s/messages"%self.get_chatid(), {"body": text,"type": type_})

    def get_chatid(self):
        """
        return : Str/null
        """
        try:
            # rt = loads(self.request("get", "/lol-champ-select/v1/session"))['chatDetails']['chatRoomName'].split("@")[0] + r"@champ-select.sa2.pvp.net"
            rt = loads(self.request("get", "/lol-champ-select/v1/session"))['chatDetails']['multiUserChatId'] + r"@champ-select.sa2.pvp.net"
        except:
            rt = ""
        return rt

    def get_gameflow(self):
        """
        flows = ['"None"'      ,  '"Lobby"'          , '"Matchmaking"',
                 '"ReadyCheck"',  '"ChampSelect"'    , '"InProgress"' ,
                 '"Reconnect"' ,  '"WaitingForStats"', '"EndOfGame"'   ]

        return status as a str
        return : Str
        """
        return self.request("get", "/lol-gameflow/v1/gameflow-phase")

    def get_owned_champions(self):
        """
        return your own champions
        return : Dict
        """
        json_raw   = loads(self.request('get','/lol-champions/v1/owned-champions-minimal'))
        champ_id   = [i['id'] for i in json_raw]
        champ_name = [i['name'] for i in json_raw]
        return dict(zip(champ_id, champ_name))

    def get_money(self, type_= ""):
        """
        it will return a dict or int
        ip => blue dust
        rp => store coin
        return : Dict/Int
        """
        rt = loads(self.request('get', '/lol-store/v1/wallet'))
        if type_:
            rt = rt[type_]
        return rt

    def get_ALL_perks(self):
        """
        return all perks that available in game
        the key is perk id
        use for self.auto_pers()
        return : Dictbb
        """
        perk_js = loads(self.request('get', '/lol-perks/v1/perks'))
        perks = {}
        for i in range(len(perk_js)):
            perks[int(perk_js[i]['id'])] = perk_js[i]['name']
        return dict([(i,perks[i]) for i in sorted(perks.keys())])

    def get_current_perks(self):
        perks = loads(self.request('get', '/lol-perks/v1/currentpage'))
        [perks.pop(key, None) for key in ["autoModifiedSelections", "id", "isDeletable", "isEditable", "lastModified", "order", "isEditable"]]
        perks["isActive"] = True
        return perks

    def get_beauty_loot_list(self):
        """
        this function will return a dict which in loot list
        return : Dict
        """
        return loads(js_beauty(loads(self.request('get', '/lol-loot/v1/player-loot'))))

    def get_loot_info(self, item):
        """
        it will return item infomation
        include recipes and lootID
        return : Dict
        """
        return loads(js_beauty(loads(self.request('get', '/lol-loot/v1/recipes/initial-item/' + item))))

    def get_loot_recipeNames(self, item):
        """
        return Recipe Names
        return : List
        """
        return [i['recipeName'] for i in self.get_loot_info(item)]

    # def get_summoner_info(self):
    #     """
    #     it will return 'name','Blue dust', 'RP', 'Level', 'EXP', 'accountId', 'puuid', 'summonerId' as a dictionary
    #     return : Dict
    #     """
    #     info    = loads(self.request('get', '/lol-summoner/v1/current-summoner'))
    #     wallet  = self.get_money()
    #     return dict(zip(['Name', 'Blue dust', 'RP', 'Level', 'EXP', 'accountId', 'puuid', 'summonerId'], [info['internalName'], wallet['ip'], wallet['rp'], info['summonerLevel'], str(info['percentCompleteForNextLevel'])+" %", info['accountId'], info['puuid'], info['summonerId']]))

    def get_summoner_info(self):
        """
        it will return 'name', 'Level', 'EXP', 'accountId', 'puuid', 'summonerId' as a dictionary
        return : Dict
        """
        info    = loads(self.request('get', '/lol-summoner/v1/current-summoner'))
        return dict(zip(['Name', 'Level', 'EXP', 'accountId', 'puuid', 'summonerId'], [info['internalName'], info['summonerLevel'], str(info['percentCompleteForNextLevel'])+" %", info['accountId'], info['puuid'], info['summonerId']]))

    def auto_loot_champions(self, smart = True):
        """
        if smart set
        it will only disenchant not owned
        return : List
        """
        fragments = [int(i['lootId'].strip('CHAMPION _RENTAL_')) for i in self.get_beauty_loot_list() if "CHAMPION_RENTAL_" in i['lootId']]
        if smart:
            owned = list(self.get_owned_champions().keys())
            fragments = list(set(fragments) & set(owned))
        for j in fragments:
            self.request('post', '/lol-loot/v1/recipes/CHAMPION_RENTAL_disenchant/craft', [f'CHAMPION_RENTAL_{j}'])
        return [self.get_champion_ID_Name(i) for i in fragments] # sorted(fragments)

    def auto_champion(self, id_, lock = False):
        # update /lol-champ-select/v1/grid-champions/62
        """
        allow you to auto pick champ
        if var lock = True
        it will auto lock in
        return : Str
        """
        try:
            js_raw         = loads(self.request("get", "/lol-champ-select/v1/session"))
            actorCellId_id = [i['cellId'] for i in js_raw['myTeam'] if i['summonerId'] == self.get_summoner_info()['summonerId']][0]
            action_id      = [i['id'] for i in js_raw['actions'][0] if i['actorCellId'] == actorCellId_id][0]
            lock_stat      = [i['completed'] for i in js_raw['actions'][0] if i['actorCellId'] == actorCellId_id][0]
            self.request("patch", "/lol-champ-select/v1/session/actions/%d"%action_id, {'championId': id_})
            if lock and lock_stat == False:
                self.request("post", "/lol-champ-select/v1/session/actions/%s/%s"%(action_id, "complete"))
            return f"Picked : {self.get_champion_ID_Name(id_)} \nlocked : {lock}"
        except:
            return "Not in room."

    # def auto_lane(self, lane, directly=False):
    #     """
    #     auto msg what you want to say
    #     return : Str/null
    #     NOTICE : If not work plz check get_chatid()
    #     """
    #     try:
    #         global join_room_members
    #         room_dict = loads(self.request('get', f'/lol-chat/v1/conversations/{self.get_chatid()}/messages'))
    #         join_list = [i['body'] for i in room_dict if i['body'] == 'joined_room']
    #         if directly and (len(join_list) >= 1):
    #             self.chat(lane, 'chat')
    #             return True
    #         else:
    #             if len(join_list) == join_room_members:
    #                 for i in room_dict:
    #                     if (i['body'] == lane) and (i['fromSummonerId'] == lol.get_summoner_info()['summonerId']):
    #                         return True
    #                 self.chat(lane, 'chat')
    #                 return True
    #     except:
    #         return False

    def auto_lane(self, lane):
        """
        auto msg what you want to say
        return : Str/null
        NOTICE : If not work plz check get_chatid()
        """
        try:
            global join_room_members
            if len([i['body'] for i in loads(self.request('get', f'/lol-chat/v1/conversations/{self.get_chatid()}/messages')) if i['body'] == 'joined_room']) == join_room_members:
                self.chat(lane, 'chat')
                return True
        except:
            return False

    def auto_perks(self, runes):
        """
        it will delete current active rune page
        and activate gived runes
        return : null
        """
        current_page = loads(self.request('get', '/lol-perks/v1/currentpage'))
        # print(f"{current_page= }") #debug
        if "message" in current_page:
            get_page_issue = current_page['message']
            # print(f"{get_page_issue = }")  #debug
            if get_page_issue == "Perk Page not found.":
                pass
        try:
            if current_page['isTemporary'] or current_page['isDeletable']:
                self.request('delete', f'/lol-perks/v1/pages/{current_page["id"]}')
        except:
            post_page = loads(self.request('post', '/lol-perks/v1/pages', runes))
            # print(f"{post_page = }") #debug
            if "message" in post_page:
                post_page_issue = post_page['message']
                # print(f"{post_page_issue}") #debug
                if post_page_issue == "Max pages reached":
                    perk_pages = loads(self.request('get', '/lol-perks/v1/pages'))
                    # print(f"{perk_pages = }") #debug
                    for i in perk_pages:
                        if (i['isDeletable'] == True) or (i['isTemporary'] == True):
                            self.request('delete', f'/lol-perks/v1/pages/{i["id"]}')
        finally:
            return loads(self.request('post', '/lol-perks/v1/pages', runes))

    def auto_spell(self, sp1, sp2):
        """
        sp1 = keyboard {D}
        sp1 = keyboard {F}
        {1: '淨化', 3: '虛弱', 4: '閃現', 6: '鬼步', 7: '治癒', 11: '重擊', 12: '傳送', 13: '清晰', 14: '點燃', 21: '光盾', 32: '雪球'}
        return : js.text (Str)
        """
        return self.request('patch', '/lol-champ-select/v1/session/my-selection', loads('{"spell1Id" : %i, "spell2Id" : %i}'%(sp1, sp2)))

    def make_10train(self):
        """
        make 9 bots practice room
        return : js.text (Str)
        """
        roomjs = loads('{"customGameLobby": {"configuration": {"gameMode": "PRACTICETOOL","gameMutator": "","mapId": "11","mutators": {"id": "1"},"spectatorPolicy": "NotAllowed","teamSize": "5"},"lobbyName": "10人練習工具 By毛","lobbyPassword": "null"},"isCustom": "true"}')
        return self.request('post', '/lol-lobby/v2/lobby', roomjs)

    def bypass_countdown(self):
        """
        bypass can't do anything when afk count down
        return : null
        """
        self.request('post', r'/riotclient/kill-and-restart-ux')

    def ui_control(self, mode):
        """
        minimize  =>  min to task bar
        show      =>  bring to front
        return : null
        """
        self.request('post', f'/riotclient/ux-{mode}')

    def skin_booster(self, auto = 0):
        """
        ! ONLY USE WHEN NOT HAVE ENOUGHT RP !
        skin booster in ARAM
        return : js.text (Str)
        """
        if self.get_money('rp') > 10 and auto == 0:
            ans = input('Your RP will be lost\ninput "y" to confirm\n: ')
            if ans != 'y':
                return 'Canceled'
        return self.request('post', '/lol-champ-select/v1/team-boost/purchase')

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

    def set_status(self, st = 1):
        """
        set your status
        1:online 2:away 3:offline 4:phone online
        return : js.text (Str)
        """
        mode = {1:'chat', 2:'away', 3:'offline', 4:'mobile'}
        return self.request('put', '/lol-chat/v1/me', {"availability": mode[st]})

    def get_current_perks_name(self):
        """
        return perks name that current used
        return : list
        """
        perks = self.get_ALL_perks()
        ret = []
        for i in self.get_current_perks()["selectedPerkIds"]:
            ret.append(dict_find(i, perks))
        return ret

    def get_champion_ID_Name(self, var):
        """
        return champion id or name
        return : str/int
        """
        return dict_find(var, self.champions)

    def find_name_by_summonerId(self, summonerId):
        json = loads(self.request("get", f"/lol-summoner/v1/summoners/{str(summonerId)}"))
        # print(json)
        return get_dict(json, ['internalName']) # get_dict(json, ['displayName'])

    def get_room_summoner_name(self):
        json = loads(self.request("get", r"/lol-champ-select/v1/session"))
        summoner_names = []
        myTeam = get_dict(json, ['myTeam'])
        for i in myTeam:
            summoner_id = int(get_dict(i, ['summonerId']))
            if summoner_id != 0:
                summoner_name = self.find_name_by_summonerId(summoner_id)
                if summoner_name:
                    summoner_names.append(summoner_name)
        # print(f"\n{summoner_names = }\n") #debug
        return summoner_names

    def set_OPGG(self):
        while True:
            try:
                self.OPGG = OPGG(self.get_room_summoner_name())
                break
            except:
                pass

    def parse_OPGG_res(self):
        res = []
        res.append(f"\n{'*'*40}")
        for k,v in self.OPGG.summoners_dict.items():
            # print(f"\nkey: {k}\nvalue: {v}\n\n") #debug
            res.append(f"{k} ({v['current_tier']})")
            res.append("近20場:")
            res.append(f"    {'勝率:':5} {v['win_rate']}%")
            res.append(f"    {'KDA:':5} {v['kda_average']}")
            res.append(f"    {'隱分區段:':5} {v['recent_most_tier']}")
            res.append(f"    {'遊玩模式:':5} {v['recent_most_gameplay_type']}")
            if v['consecutive_win-lose'][0] >= 2:
                if v['consecutive_win-lose'][1] == 'WIN':
                    keywords = "贏"
                else:
                    keywords = "輸"
                res.append(f"連{keywords} {v['consecutive_win-lose'][0]} 場")
            if k != list(self.OPGG.summoners_dict.keys())[-1]:
                res.append(f"{'-'*80}")
        res.append(f"{'*'*40}")
        for i in res:

            self.chat(i)
            print(i)

    def find_id_by_summonername(self, name):
        json = loads(self.request("get", f"/lol-summoner/v1/summoners?name={name}"))
        return get_dict(json, ['summonerId'])

    def parse_OPGG_summoner_champ_proficiency(self):
        buffer = []
        buffer.append(f"\n{'*'*40}")
        json = loads(self.request('get', "/lol-champ-select/v1/session"))
        myTeam_list = get_dict(json, ['myTeam'])
        for i in myTeam_list:
            # print(i)
            championId = get_dict(i, ['championId'])
            champion_name = dict_find(championId, self.champions)
            summoner_name = self.find_name_by_summonerId(get_dict(i, ['summonerId']))
            res = self.OPGG.get_champ_played_res(summoner_name, championId)
            if res != []:
                for j in res:
                    buffer.append(f"{summoner_name} 在 {j['type']} 玩 {champion_name}，共 {j['played_total']} 場的勝率是 {j['win_rate']} %% 。")
                if i != myTeam_list[-1]:
                    buffer.append(f"{'-'*80}")
        if buffer[-1] == f"{'-'*80}":
            buffer.pop()
        buffer.append(f"{'*'*40}")
        for i in buffer:
            self.chat(i)
            print(i)

    def find_match(self, **args):
        """
        args include
            lane     = 'message or lane'(str)
            UI       = 'show' 'minimize'(str)
            champion = ['champ id'(str or int),'lock or not'(bool)]
            perks    = 'js'(dictionay)

        if use default settings it will
            1. auto pick top lane
            2. show UI in champ selection
            3. pick WUKONG without lock
            4. set summoner spells (D Flash, F Ignite)
            5. set runes Conqueror

        return : null
        """
        default_settings = {
            'lane'      : 'top'         ,
            'UI'        : 'show'        ,
            'champion'  : [62, False]   ,
            'spells'    : [4, 14]       ,
            'perks'     : {'current': True, 'isActive': True, 'isValid': True, 'name': '悟空 - 征服者', 'primaryStyleId': 8000, 'selectedPerkIds': [8010, 9111, 9104, 8299, 8143, 8135, 5005, 5008, 5002], 'subStyleId': 8100}
            }
        # set variables
        for k,v in default_settings.items():
            args.setdefault(k, v)
        if isinstance(args['champion'], (int, str)):
            args['champion'] = [args['champion'], False]
        # show ascii img
        print(Pic().squirrel_fool,'\n')
        # show summoner informations
        for i,(k,v) in enumerate(self.get_summoner_info().items()):
            if i == 3: break
            # print(f'\t   {"%-11s"%(c(k,34))} :   {c(v,36)}')
            print(f'\t   {"%-19s"%(c(k,34))} :   {c(v,36)}')
        print('')
        # print(f'\n{c("按下(q)退出。", 33)}')
        while (True):
            try:
                if kbhit() and getch() == b'q': raise(KeyboardInterrupt)
                gameflow = self.get_gameflow().strip('"')
                # show current status
                trans_flow = {'None': '請先進入遊戲大廳', 'Lobby': '組隊大廳', 'Matchmaking': '尋找對戰...', 'ReadyCheck': '接受對戰...', 'ChampSelect': '選擇英雄...', 'InProgress': '遊戲中...', 'Reconnect': '重新連線...', 'WaitingForStats': '等待結算...', 'EndOfGame': '結算畫面'}
                self.stlog(f'{c(trans_flow[gameflow], 35)}')
                if gameflow == 'None':
                    break
                elif gameflow == 'Lobby':
                    # auto click find match
                    self.request('post', '/lol-lobby/v2/lobby/matchmaking/search')
                elif gameflow == 'ReadyCheck':
                    # click accept
                    self.ui_control('minimize')
                    self.request("post", "/lol-matchmaking/v1/ready-check/accept")
                elif gameflow == 'ChampSelect':
                    # send lane
                    if self.auto_lane(args['lane']):
                        # show UI
                        self.ui_control(args['UI'])
                        # select champion
                        self.auto_champion(*args['champion'])
                        # select summoner skills
                        self.auto_spell(*args['spells'])
                        # select perks
                        self.auto_perks(args['perks'])
                        # inspect summoners
                        self.set_OPGG()
                        self.parse_OPGG_res()
                        # print and break
                        save_rt = self.save()
                        if save_rt == 0:
                            self.stlog("執行完畢")
                            break
                        elif save_rt == 1:
                            self.stlog("取消儲存...")
                            break
                        elif save_rt == 2:
                            self.stlog("重新匹配...")
                elif gameflow == 'InProgress':
                    break
            except KeyboardInterrupt:
                self.stlog('使用者中斷操作')
                break
            except Exception as e:
                current_function_name = inspect.currentframe().f_back.f_code.co_name
                cmd('cls')
                print(Pic().squirrel_watching_you)
                cmd('pause')
                self.stlog(f'在 "{current_function_name}" 發生預期外的錯誤: ' + f'{str(e)}')
                break

    def save(self):
        try:
            while(True):
                self.stlog('等待鎖定中...')
                js_raw         = loads(self.request("get", "/lol-champ-select/v1/session"))
                myTeam_self    = [i for i in js_raw['myTeam'] if i['summonerId'] == self.get_summoner_info()['summonerId']][0]
                lockin = [i['completed'] for i in js_raw['actions'][0] if i['actorCellId'] == myTeam_self['cellId']][0]
                phase = get_dict(js_raw, ['timer', 'phase'])
                if lockin and (phase == 'FINALIZATION'):
                    self.parse_OPGG_summoner_champ_proficiency()
                    champ = [i['championId'] for i in js_raw['actions'][0] if i['actorCellId'] == myTeam_self['cellId']][0]
                    champ_name = self.get_champion_ID_Name(champ)
                    spells = [myTeam_self["spell1Id"], myTeam_self["spell2Id"]]
                    msg = [i['body'] for i in loads(self.request("get", r"/lol-chat/v1/conversations/%s/messages"%self.get_chatid())) if i['fromSummonerId'] == self.get_summoner_info()['summonerId']]
                    msg.reverse()
                    for i in msg:
                        if i.upper() in ['JG', 'JUNGLE', 'TOP', 'AD', 'AP', 'MID', 'SUP', '上', '上路', '中', '中路', '輔助', '輔', '打野']:
                            lane = i.upper()
                            break
                        lane = "??"
                    perks = self.get_current_perks()
                    perks["name"] = f"{champ_name} - {self.get_current_perks_name()[0]}"
                    for i in ["runeRecommendationId", "recommendationIndex", "recommendationChampionId", "isRecommendationOverride", "isTemporary"]:
                        del(perks[i])
                    # 沒有find版 return (f"\n\n# {champ_name}\nlane = '{lane}', champion = [{champ}, False], spells = {spells}, perks = {perks}")
                    ret = f"\n\n# {perks['name']}\nLeagueClient().find_match(lane = '{lane}', champion = [{champ}, False], spells = {spells}, perks = {perks})"
                    self.stlog(f"{c(ret, 31)}", status = 0)
                    return 0
        except KeyboardInterrupt:
            return 1
        except:
            return 2

    def test(self):
        global join_room_members
        join_room_members = 1
        self.make_10train()
        self.request('post', '/lol-lobby/v1/lobby/custom/start-champ-select')


if __name__ == '__main__':
    debug = False
    lol = LeagueClient()
    if debug:
        lol.test()
    # 娜菲芮 - 死亡電刑
    # LeagueClient().find_match(lane = 'MID', champion = [950, False], spells = [4, 14], perks = {'current': True, 'isActive': True, 'isValid': True, 'name': '娜菲芮 - 死亡電刑', 'primaryStyleId': 8100, 'selectedPerkIds': [8112, 8143, 8138, 8135, 8009, 8014, 5008, 5008, 5003], 'subStyleId': 8000})
    # 悟空 - 征服者
    # LeagueClient().find_match()
    # 烏迪爾 - 刀鋒之雹
    # LeagueClient().find_match(lane = 'JG', champion = [77, False], spells = [6, 11], perks = {'current': True, 'isActive': True, 'isValid': True, 'name': '烏迪爾 - 刀鋒之雹', 'primaryStyleId': 8100, 'selectedPerkIds': [9923, 8143, 8138, 8135, 8234, 8232, 5005, 5008, 5002], 'subStyleId': 8200})
    # 維爾戈 - 強攻
    # LeagueClient().find_match(lane = 'JG', champion = [234, False], spells = [4, 11], perks = {'current': True, 'isActive': True, 'isValid': True, 'name': '維爾戈 - 強攻', 'primaryStyleId': 8000, 'selectedPerkIds': [8005, 9111, 9104, 8014, 8143, 8105, 5005, 5008, 5001], 'subStyleId': 8100})
    # 卡特蓮娜 - 征服者
    # LeagueClient().find_match(lane = 'MID', champion = [55, False], spells = [4, 14], perks = {'current': True, 'isActive': True, 'isValid': True, 'name': '卡特蓮娜 - 征服者', 'primaryStyleId': 8000, 'selectedPerkIds': [8010, 9111, 9105, 8299, 8143, 8105, 5008, 5008, 5002], 'subStyleId': 8100})
    # 卡特蓮娜 - 死亡電刑
    # LeagueClient().find_match(lane = 'MID', champion = [55, False], spells = [4, 14], perks = {'current': True, 'isActive': True, 'isTemporary': False, 'isValid': True, 'name': '卡特蓮娜 - 死亡電刑', 'primaryStyleId': 8100, 'selectedPerkIds': [8112, 8143, 8138, 8105, 8014, 9111, 5008, 5008, 5002], 'subStyleId': 8000})
    #  阿俊 - 卡特蓮娜 - 征服者
    # LeagueClient().find_match(lane = 'MID', champion = [55, False], spells = [21, 14], perks = {'current': True, 'isActive': True, 'isTemporary': False, 'isValid': True, 'name': '卡特蓮娜 - 征服者', 'primaryStyleId': 8000, 'selectedPerkIds': [8010, 9111, 9104, 8014, 8143, 8105, 5005, 5008, 5002], 'subStyleId': 8100})
    # 艾希 - 奧術彗星
    # LeagueClient().find_match(lane = 'SUP', champion = [22, False], spells = [4, 3], perks = {'current': True, 'isActive': True, 'isValid': True, 'name': '艾希 - 奧術彗星', 'primaryStyleId': 8200, 'selectedPerkIds': [8229, 8226, 8210, 8237, 8009, 8014, 5007, 5008, 5002], 'subStyleId': 8000})
    # 雷歐娜 - 裂地衝擊
    # LeagueClient().find_match(lane = 'SUP', champion = [89, False], spells = [4, 14], perks = {'current': True, 'isActive': True, 'isValid': True, 'name': '雷歐娜 - 裂地衝擊', 'primaryStyleId': 8400, 'selectedPerkIds': [8439, 8463, 8473, 8242, 8345, 8347, 5007, 5002, 5001], 'subStyleId': 8300})
    # 索拉卡 - 召喚艾莉
    # LeagueClient().find_match(lane = 'SUP', champion = [16, False], spells = [4, 7], perks = {'current': True, 'isActive': True, 'isValid': True, 'name': '索拉卡 - 召喚艾莉', 'primaryStyleId': 8200, 'selectedPerkIds': [8214, 8226, 8210, 8237, 8453, 8463, 5008, 5008, 5002], 'subStyleId': 8400})
    # 提摩 - 召喚艾莉
    # LeagueClient().find_match(lane = 'TOP', champion = [17, False], spells = [4, 14], perks = {'current': True, 'isActive': True, 'isTemporary': False, 'isValid': True, 'name': '提摩 - 召喚艾莉', 'primaryStyleId': 8200, 'selectedPerkIds': [8214, 8275, 8234, 8237, 8014, 9103, 5005, 5008, 5002], 'subStyleId': 8000})
    # 悠咪 - 搞人專用
    # LeagueClient().find_match(lane = '', champion = [350, False], spells = [11, 14], perks = {'current': True, 'isActive': True, 'isValid': True, 'name': '悠咪 - 搞人專用', 'primaryStyleId': 8200, 'selectedPerkIds': [8214, 8275, 8210, 8237, 8316, 8347, 5005, 5008, 5001], 'subStyleId': 8300})
# "find match or delete" post or delete : lol.request('????', '/lol-lobby/v2/lobby/matchmaking/search')
# "get locked champion" :                 lol.request('get',  '/lol-champ-select-legacy/v1/current-champion')
# "get info" :                            lol.request('get',  '/lol-summoner/v1/current-summoner')
# "skin booster" :                        lol.request('post', '/lol-champ-select-legacy/v1/team-boost/purchase')
# "get current perk" :                    lol.request('get',  '/lol-perks/v1/currentpage')
# "NEW IDEA TO DETECT ! IN ROOM" :        lol.request('get',  '/lol-champ-select-legacy/v1/implementation-active')
# "Get summoner info by name" :           lol.request("get", r"/lol-summoner/v1/summoners?name={url_encode_name}")
# "Get summoner info by id" :             lol.request("get", r"/lol-summoner/v1/summoners/{id}")
# =============================================================================
# TODO
# 1. 房間內顯示別的召喚師
# 2. 背景修改
# =============================================================================
#     json = {
#   "hasNewAbility": "False",
#   "hasNewFanLine": "True",
#   "hasPlayedTutorial": "True",
#   "hasSeenCelebration_Expert": "True",
#   "hasSeenLoadoutTutorial": "True",
#   "hasSeenMapTutorial": "True",
#   "loadout_active_e": "1",
#   "loadout_active_q": "1",
#   "loadout_active_r": "2",
#   "loadout_active_w": "3",
#   "numNodesUnlocked": "14",
#   "progress": "14"
# }
#     lol.request('post', '/lol-marketing-preferences/v1/partition/sfm2023', json=json)
