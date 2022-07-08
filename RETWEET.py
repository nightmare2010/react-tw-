import requests
import threading
import time
import re
import random
import colorama
from colorama import Fore
import lxml.html

colorama.init(autoreset=True)

print(Fore.RED + """

                    ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗    
                    ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝    
                    ██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗      
                    ██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝      
                    ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗    
                    ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    
                                                                              
""")
t = {}
num_ = print(Fore.YELLOW + 'enter Number Thread: ', end="")
num_ = int(input())
likee = print(Fore.YELLOW + "want like tweet (y/n): ", end="")
likee = str(input())
rettwee = print(Fore.YELLOW + "want retweet tweet (y/n): ", end="")
rettwee = str(input())
sumbm = print(Fore.YELLOW + "want quote tweet (y/n): ", end="")
sumbm = str(input())
comment = print(Fore.YELLOW + "want comment on tweet (y/n): ", end="")
comment = str(input())
timeper = print(Fore.YELLOW + "enter time per action: ", end="")
timeper = int(input())
timeacc = print(Fore.YELLOW + "enter time per acount: ", end="")
timeacc = int(input())
link = print(Fore.YELLOW + "enter the link: ", end="")
link = str(input())

r = requests.session()

file = open("cookies.txt", "r")
files = file.readlines()
number_len = len(files) // num_

collect = num_ * number_len

corrector = len(files) - collect

if corrector != 0:
    num_ = num_ + 1
    number_len = number_len + 1
for num_Thrad in range(num_):
    t[num_Thrad] = []

o = 0
n = 0
file = open("cookies.txt", "r")
for mail in file.readlines():
    mail = mail.rstrip("\n")
    t[n].append(str(mail))
    o = o + 1
    if o == number_len:
        o = 0
        n = n + 1

k = [0]
proxyDict = ""


def getcookies(proxyDict):
    r = requests.session()

    cookies = ""
    headers = {
        'accept': '*/*',
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "cccd",
    }

    while True:

        for bb in range(5):
            checkBroxy = False
            try:

                req = r.get("https://twitter.com/", headers=headers, proxies=proxyDict)
                checkBroxy = True

                break
            except requests.exceptions.ConnectionError:
                checkBroxy = False

        if not checkBroxy:
            print("no connection")


        else:
            break
        for cookienew in r.cookies.get_dict():
            # cookies=none
            cookies = cookies + cookienew + "=" + r.cookies.get_dict()[cookienew] + "; "

    return cookies


def dataaa(file_name_, tr):
    stz = 30
    x = 0

    r = requests.session()
    aaid = re.search("[0-9]{10,}", str(link))
    idtwe = aaid.group()
    idtwe = idtwe[0:]
    ##print(idtwe)
    ##print(link)

    for mail in file_name_:
        user = mail.split(":")[2]
        ct0 = mail.split(":")[1]
        auth = mail.split(":")[0]
        proxy = mail.split(":")[5]
        port = mail.split(":")[6]
        ###
        prpxxy = f"{proxy}:{port}"
        if "@" in user:
            user = user[1:]
        proxyDict = {

            "http": "http://" + prpxxy,
            "https": "http://" + prpxxy,

        }
        print(Fore.YELLOW + user)
        tweets = open("tweets.text", "r")
        twtw = []
        for tweet in tweets.readlines():
            tweet = tweet.rstrip("\n")
            twtw.append(tweet)
            randomtweet = str(random.choice(twtw))

        tweetsump = randomtweet

        # auth="76404286e0d843b86e46cbcb20a40961aecc3dd6"
        # ct0="7629fa259bb9eade5dafe1887f5033364e061d7da29a1a9c58016cbf9a790f3265cfb1023e88874cca668c71a0f847e663288cae7d6529d6f803849272498627325dca1db798c2b272b8a333f7d5f2d9"

        if stz == 30:
            stz = 0
            #print(164)
            cookies = getcookies(proxyDict)

        try:

            headok = {

                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

                'cookie': cookies + "auth_token=" + str(auth) + ";" + "ct0=" + str(ct0) + ";",
                'referer': 'https://twitter.com/account/access',

                'x-csrf-token': str(ct0),
                'authenticity_token': str(auth),
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41',

            }

            while True:

                for bb in range(5):
                    checkBroxy = False
                    try:

                        okk = r.get("https://twitter.com/account/access", headers=headok, proxies=proxyDict)
                        checkBroxy = True

                        break
                    except requests.exceptions.ConnectionError:
                        checkBroxy = False

                if not checkBroxy:
                    print("Proxy Connection Error")

                    proxyDict = {
                        "https": "http://" + prpxxy,
                        "http": "http://" + prpxxy,
                    }
                else:
                    break
            for cookienew in r.cookies.get_dict():
                # cookies=none
                cookies = cookies + cookienew + "=" + r.cookies.get_dict()[cookienew] + "; "
            cookiesn = cookies.find("_twitter_sess")

            lxml_mysite = lxml.html.fromstring(okk.text)

            authenticity_token = lxml_mysite.xpath("//input[@name='authenticity_token']")[0].get('value')
            assignment_token = lxml_mysite.xpath("//input[@name='assignment_token']")[0].get('value')
            lang = lxml_mysite.xpath("//input[@name='lang']")[0].get('value')
            flow = lxml_mysite.xpath("//input[@name='flow']")[0].get('value')
            nsi = lxml_mysite.xpath("//input[@name='nsi']")[0].get('value')
            print(Fore.RED + user + " is locked")

            headok = {

                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '101',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookies + "auth_token=" + str(auth) + ";" + "ct0=" + str(ct0) + ";",
                'origin': 'https://twitter.com',
                'referer': 'https://twitter.com/account/access',
                'x-csrf-token': str(ct0),
                'authenticity_token': str(auth),

                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41',

            }
            dataok = 'authenticity_token=' + authenticity_token + '&assignment_token=' + assignment_token + '&lang=' + lang + '&flow='

            while True:

                for bb in range(5):
                    checkBroxy = False
                    try:

                        okk = r.post("https://twitter.com/account/access", headers=headok, data=dataok,
                                     proxies=proxyDict)
                        checkBroxy = True

                        break
                    except requests.exceptions.ConnectionError:
                        checkBroxy = False

                if not checkBroxy:
                    print("Proxy Connection Error")

                    proxyDict = {
                        "https": "http://" + prpxxy,
                        "http": "http://" + prpxxy,
                    }
                else:
                    break
            if str(okk) == "<Response [200]>":
                print(Fore.CYAN + "now is available >>> " + user)

        except:
            pass

        try:
            while True:
                token_work = False

                try:
                    if likee == "y":
                        headers = {
                            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                            'content-length': '141',
                            'content-type': 'application/json',
                            'cookie': cookies + "auth_token=" + str(auth) + ";" + "ct0=" + str(ct0) + ";",
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                            'x-csrf-token': str(ct0),
                            'authenticity_token': str(auth),

                        }

                        paylike = '{"variables":{"tweet_id":"' + idtwe + '"},"queryId":"lI07N6Otwv1PhnEgXILM7A"}'

                        while True:

                            for bb in range(5):
                                checkBroxy = False
                                try:

                                    like = r.post(
                                        "https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet",
                                        headers=headers, data=paylike, proxies=proxyDict)
                                    checkBroxy = True

                                    break
                                except requests.exceptions.ConnectionError:
                                    checkBroxy = False

                            if not checkBroxy:
                                print("Proxy Connection Error")

                                proxyDict = {
                                    "https": "http://" + prpxxy,
                                    "http": "http://" + prpxxy,
                                }
                            else:
                                break
                        if str(like) == "<Response [200]>":
                            # print(like)
                            # print(like.json())
                            print(Fore.GREEN + "like >>> DONE")
                            token_work = True
                            time.sleep(timeper)

                            break

                        dx = like.json()
                        if str(like) == "<Response [431]>":
                            token_work = False


                except:
                    token_work = False
                if not token_work:
                    print(Fore.BLACK+"token change")
                    cookies = getcookies(proxyDict)
                else:
                    break
            if rettwee == "y":
                headers = {
                    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                    'content-length': '162',
                    'content-type': 'application/json',
                    'cookie': cookies + "auth_token=" + str(auth) + ";" + "ct0=" + str(ct0) + ";",
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                    'x-csrf-token': str(ct0),
                    'authenticity_token': str(auth),

                }

                payretweet = '{"variables":{"tweet_id":"' + idtwe + '","dark_request":false},"queryId":"ojPdsZsimiJrUGLR1sjUtA"}'

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:

                            retweet = r.post("https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet",
                                             headers=headers, data=payretweet, proxies=proxyDict)
                            checkBroxy = True

                            break
                        except requests.exceptions.ConnectionError:
                            checkBroxy = False

                    if not checkBroxy:
                        print("Proxy Connection Error")

                        proxyDict = {
                            "https": "http://" + prpxxy,
                            "http": "http://" + prpxxy,
                        }
                    else:
                        break
                if str(retweet) == "<Response [200]>":
                    # print(retweet)
                    # print(retweet.json())
                    print(Fore.GREEN + "retweet >>> DONE")

                time.sleep(timeper)
            if sumbm == "y":
                headers = {
                    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                    'content-length': '754',
                    'content-type': 'application/json',
                    'cookie': cookies + "auth_token=" + str(auth) + ";" + "ct0=" + str(ct0) + ";",
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                    'x-csrf-token': str(ct0),
                    'authenticity_token': str(auth),

                }

                paysump = '{"variables":{"tweet_text":"' + tweetsump + '","attachment_url":"' + link + '","media":{"media_entities":[],"possibly_sensitive":false},"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withSuperFollowsUserFields":true,"semantic_annotation_ids":[],"dark_request":false},"features":{"dont_mention_me_view_api_enabled":true,"interactive_text_enabled":true,"responsive_web_uc_gql_enabled":false,"vibe_tweet_context_enabled":false,"responsive_web_edit_tweet_api_enabled":false,"standardized_nudges_misinfo":false,"responsive_web_enhance_cards_enabled":false},"queryId":"We8wLGIe9m1lH5JSpPX-2Q"}'

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:

                            sump = r.post("https://twitter.com/i/api/graphql/We8wLGIe9m1lH5JSpPX-2Q/CreateTweet",
                                          headers=headers, data=paysump, proxies=proxyDict)
                            checkBroxy = True

                            break
                        except requests.exceptions.ConnectionError:
                            checkBroxy = False

                    if not checkBroxy:
                        print("Proxy Connection Error")

                        proxyDict = {
                            "https": "http://" + prpxxy,
                            "http": "http://" + prpxxy,
                        }
                    else:
                        break
                if str(sump) == "<Response [200]>":
                    # print(sump)
                    # print(sump.json())
                    print(Fore.GREEN + "quote >>> DONE")

                time.sleep(timeper)

            if comment == "y":
                headers = {
                    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                    'content-length': '754',
                    'content-type': 'application/json',
                    'cookie': cookies + "auth_token=" + str(auth) + ";" + "ct0=" + str(ct0) + ";",
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                    'x-csrf-token': str(ct0),
                    'authenticity_token': str(auth),

                }

                paycomm = '{"variables":{"tweet_text":"' + tweetsump + '","reply":{"in_reply_to_tweet_id":"' + idtwe + '","exclude_reply_user_ids":[]},"media":{"media_entities":[],"possibly_sensitive":false},"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withSuperFollowsUserFields":true,"semantic_annotation_ids":[],"dark_request":false},"features":{"dont_mention_me_view_api_enabled":true,"interactive_text_enabled":true,"responsive_web_uc_gql_enabled":false,"vibe_tweet_context_enabled":false,"responsive_web_edit_tweet_api_enabled":false,"standardized_nudges_misinfo":false,"responsive_web_enhance_cards_enabled":false},"queryId":"We8wLGIe9m1lH5JSpPX-2Q"}'

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:

                            comm = r.post("https://twitter.com/i/api/graphql/We8wLGIe9m1lH5JSpPX-2Q/CreateTweet",
                                          headers=headers, data=paycomm, proxies=proxyDict)
                            checkBroxy = True

                            break
                        except requests.exceptions.ConnectionError:
                            checkBroxy = False

                    if not checkBroxy:
                        print("Proxy Connection Error")

                        proxyDict = {
                            "https": "http://" + prpxxy,
                            "http": "http://" + prpxxy,
                        }
                    else:
                        break
                if str(comm) == "<Response [200]>":
                    # print(comm)
                    # print(comm.json())
                    print(Fore.GREEN + "comment >>> DONE")

                time.sleep(timeacc)
        except:
            Error = open("Error.text", "a")
            Error.write(f"{mail}" "\n")
            print(Fore.RED + "Error >>> " + user)


for tr in range(num_):
    file_name_ = t[tr]

    for cookienew in r.cookies.get_dict():
        # cookies=none
        cookies = cookies + cookienew + "=" + r.cookies.get_dict()[cookienew] + "; "

    threading.Thread(target=dataaa, args=(file_name_, tr)).start()




