#!/usr/bin/env python3
import os
import requests
import optparse
import time as mm
import sys as n

# Enable ANSI colors on some Windows terminals
os.system("")

W  = '\033[0m'   # white (normal)
R  = '\033[31m'  # red
G  = '\033[32m'  # green
O  = '\033[33m'  # orange
B  = '\033[34m'  # blue
P  = '\033[35m'  # purple
C  = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def slow(msg: str):
    for c in msg + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1.0 / 200)

parser = optparse.OptionParser()
parser.add_option("-e", "--email", dest="email", help="Email you want to check in Twitter/X")
(options, arguments) = parser.parse_args()

if not options.email:
    print(R + "[!] Missing email. Use: -e target@email.com" + W)
    n.exit(1)


slow(B + r'''

By Xcode @Xcodeone1

          _.-'`)     (`'-._
        .' -' / __    \ '- '.
       / .-' ( '-,`|   ) '-. \ 
      / .-',-`'._/ \_.'`-,'-. \ 
     ; ; /.`'.-'(   )'-.'`.\ ; ;
     | .-'|\//'-/   \-'   /|'-. |
     |` |; :|'._\   /_,'|: ;| `|
     || : |;    `Y-Y`    ;| : ||
     \:| :/======"="======\| |:/
      /_:-`    

        **************************************
        * -> Development: Mohamed Almarri | Xcode0x *
        * -> Twitter: @xcode0x                     *
        **************************************
'''+W)

url = f"https://api.twitter.com/i/users/email_available.json?email={options.email}&send_error_codes=1"

headers = {
    "Accept": "application/json",
    "X-Twitter-Client-Version": "8.41.1",
    "Accept-Language": "en",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Twitter-iPhone/8.41.1 iOS/Enjoy (By :xcodex0;@xcodex0,4;;;;;1;https://twitter.com/xcodex0)",
    "Connection": "close",
    "X-Twitter-Client-Limit-Ad-Tracking": "0",
    "X-Twitter-API-Version": "5",
    "X-Twitter-Client": "Twitter-xcodex0"
}

try:
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()

    data = resp.json()


    msg = data.get("msg", "")

    if msg == "Available!":
        print(R + " [Twitter - Don't have account]" + W)
    else:
        print(G + " [Twitter - Have account]" + W)

except requests.exceptions.Timeout:
    print(R + " [!] Request timed out" + W)
except requests.exceptions.RequestException as e:
    print(R + f" [!] Request error: {e}" + W)
except ValueError:
    print(R + " [!] Failed to parse JSON response" + W)

print()
