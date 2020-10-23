# !/usr/bin/env python
import time
import requests
import optparse
import time as mm
import sys as n
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray
def slow(M): ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 200)
parser = optparse.OptionParser()
parser.add_option("-e", "--email",dest="email", help="Email You want check in Twitter")
(options, arguments) = parser.parse_args()
slow( B +

'''


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
        * -> Development: Xcode          *
        * -> Telegram: https://t.me/x0Saudi *
        * -> Twitter @XcodeOn1              *      
        **************************************                                                 
''')
url = "https://api.twitter.com:443/i/users/email_available.json?email="+ options.email +"&send_error_codes=1"
headers = {"Accept": "application/json", "X-Twitter-Client-Version": "8.41.1",  "Accept-Language": "en", "Accept-Encoding": "gzip, deflate",  "User-Agent": "Twitter-iPhone/8.41.1 iOS/Enjoy (ByXcode;@Xcodeone1,4;;;;;1;https://t.me/x0Saudi)", "Connection": "close", "X-Twitter-Client-Limit-Ad-Tracking": "0", "X-Twitter-API-Version": "5", "X-Twitter-Client": "Twitter-Xcode"}
email = requests.get(url, headers=headers)
Emaildata = email.json()

if Emaildata["msg"] == 'Available!' :
	print(R+ " [ Twitter - Dont' Have account ]")
else:
	print(G + " [Twitter - Have account ] ")
print("\n")
