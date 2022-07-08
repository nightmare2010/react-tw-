import requests
import re
import threading
import random
import colorama
from colorama import Fore
import time
colorama.init(autoreset=True)
print(Fore.RED+"""

                    ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗    
                    ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝    
                    ██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗      
                    ██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝      
                    ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗    
                    ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    
                                                                              

""")
num_ = print(Fore.YELLOW+ 'enter Number Thread: ',end="")
num_ = int(input())
number_user = 1
number_pass = 2
number_email = 3
sleeti=print(Fore.YELLOW+"enter time to sleep: ",end="")
sleeti=int(input())
proxyche = print(Fore.YELLOW+ 'want use proxy (y/n): ',end="")
proxyche = str(input())
if proxyche == "y":
    number_prpxxy = 5
    number_port = 6

r = requests.session()

t = {}

###
j = []
n = []
y = []
k = 0
accn = []
filee = open("mails.txt", "r")
filee1 = open("cookies.txt", "r")
for mail in filee:
    mail = mail.rstrip("\n")
    mail = mail.split(":")
    j.append(mail)

for acc in filee1:
    acc = acc.rstrip("\n")
    acc = acc.split(":")

    n.append(acc[4])

for i in j:

    cb = i[2]

    if cb in n:
        continue
    else:
        accn.append(i)

###
file = accn
# files = file.readlines()
files = file
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
file = accn
# for mail in file.readlines():
for mail in file:
    # mail = mail.rstrip("\n")
    mail = mail
    t[n].append(str(mail))
    o = o + 1
    if o == number_len:
        o = 0
        n = n + 1

proxyDict = ""


########
def cook_tok(proxyDict):
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

    if proxyche == "y":

        while True:

            for bb in range(5):
                checkBroxy = False
                try:

                    r = requests.session()
                    req = r.get("https://twitter.com/", headers=headers, proxies=proxyDict)
                    checkBroxy = True

                    break
                except requests.exceptions.ConnectionError:
                    print("try again")
                    checkBroxy = False
            if checkBroxy:
                break

    else:
        req = r.get("https://twitter.com/", headers=headers)

    for cookienew in r.cookies.get_dict():
        # cookies=none
        cookies = cookies + cookienew + "=" + r.cookies.get_dict()[cookienew] + "; "

    headerst = {
        'accept': "*/*",
        'authorization': "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        'content-length': "0",
        'content-type': "application/x-www-form-urlencoded",

        'origin': "https://twitter.com",
        'referer': "https://twitter.com/",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-site",
    }

    if proxyche == "y":

        while True:

            for bb in range(5):
                checkBroxy = False
                try:


                    req = r.post("https://api.twitter.com/1.1/guest/activate.json", headers=headerst, proxies=proxyDict)
                    checkBroxy = True

                    break
                except requests.exceptions.ConnectionError:
                    checkBroxy = False
            if checkBroxy:
                break

    else:
        req = r.post("https://api.twitter.com/1.1/guest/activate.json", headers=headerst)
    print(Fore.BLACK+"got new token")
    # os.system("cls")
    guest_token = req.json()['guest_token']
    return cookies, guest_token


##########

def dataaa(file_name_, tr, rell):
    for mail in file_name_:
        r = requests.session()
        #print(mail[0])
        #print(mail.split(","))
        #print(mail.split(",")[0][1])
        user = mail.split(",")[number_user - 1]
        password = mail.split(",")[number_pass - 1]
        email1 = mail.split(",")[number_email - 1]

        if proxyche == "y":
            proxy = mail.split(",")[number_prpxxy - 1]
            port = mail.split(",")[number_port - 1]
            proxy = proxy[2:-1]
            port = port[2:-2]
            prpxxy = f"{proxy}:{port}"
        if "@" in user:
            user = user[3:-1]
        else:
            user = user[2:-1]
        email1 = email1[2:-1]
        password = password[2:-1]

        #print(email1)
        print(Fore.YELLOW+user)
        #print(password)

        ###
        if proxyche == "y":

            proxyDict = {

                "http": "http://" + prpxxy,
                "https": "http://" + prpxxy,

            }
        else:
            prpxxy = ""
            proxyDict = {
                "https": "http://",
                "http": "http://",
            }
        ###
        try:
            if rell == 30:
                rell = 0
                cookies, guest_token = cook_tok(proxyDict)
            head = {

                'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                'content-length': '282',
                'content-type': 'application/json',
                'cookie': cookies,
                'origin': 'https://twitter.com',
                'referer': 'https://twitter.com/i/flow/login',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',

                'user-agent': "cccc",
                'x-csrf-token': "638508987dc11e26daba393769bb0ee6",
                'x-guest-token': guest_token,

            }

            payload = '{"input_flow_data":{"flow_context":{"debug_overrides":{},"start_location":{"location":"splash_screen"}}},"subtask_versions":{"contacts_live_sync_permission_prompt":0,"email_verification":1,"topics_selector":1,"wait_spinner":1,"cta":4}}'

            if proxyche == "y":

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:


                            read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=login",
                                          headers=head, data=payload, proxies=proxyDict)
                            checkBroxy = True

                            break
                        except requests.exceptions.ConnectionError:
                            print("proxy connection")
                            checkBroxy = False
                    if checkBroxy:
                        break

            else:

                read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=login", headers=head,
                              data=payload)

            dataa = read.json()
            flow_token = dataa['flow_token']
            #print(flow_token)

            payload = '{"flow_token":"' + str(
                flow_token) + '","subtask_inputs":[{"subtask_id":"LoginEnterUserIdentifierSSO","settings_list":{"setting_responses":[{"key":"user_identifier","response_data":{"text_data":{"result":' + '"' + user + '"' + '}}}],"link":"next_link"}}]}'

            # print(payload)

            if proxyche == "y":

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:


                            read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head,
                                          data=payload, proxies=proxyDict)
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
            else:
                read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head, data=payload)

            # print(read)
            dataa = read.json()
            flow_token = dataa['flow_token']
            # print(flow_token)


            payload = '{"flow_token":"' + str(
                flow_token) + '","subtask_inputs":[{"subtask_id":"LoginEnterUserIdentifierSSO","settings_list":{"setting_responses":[{"key":"user_identifier","response_data":{"text_data":{"result":' + '"' + user + '"' + '}}}],"link":"next_link"}}]}'
            if proxyche == "y":

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:


                            read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head,
                                          data=payload, proxies=proxyDict)
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
            else:
                read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head, data=payload)
            #print(read.json())
            dataa = read.json()

            if 'errors' in dataa:
                payload = '{"flow_token":"' + str(
                    flow_token) + '","subtask_inputs":[{"subtask_id":"LoginEnterUserIdentifierSSO","settings_list":{"setting_responses":[{"key":"user_identifier","response_data":{"text_data":{"result":' + '"' + email1 + '"' + '}}}],"link":"next_link"}}]}'
                print(Fore.RED + "can't find User")
                if proxyche == "y":

                    while True:

                        for bb in range(5):
                            checkBroxy = False
                            try:


                                read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head,
                                              data=payload, proxies=proxyDict)
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
                else:
                    read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head, data=payload)
                #print(read.json())
                dataa = read.json()
                flow_token = dataa['flow_token']
                print(Fore.GREEN + user+" >>> User supmit")
            else:
                flow_token = dataa['flow_token']
                print(Fore.GREEN+email1+" >>> Email supmit")

            # print(flow_token)
            tele = re.search("\:[0-9]", flow_token)
            chtele = tele.group()
            chtele = chtele[1:]
            chtele = str(chtele)

            if chtele == "4":

                payload = '{"flow_token":"' + str(
                    flow_token) + '","subtask_inputs":[{"subtask_id":"LoginEnterAlternateIdentifierSubtask","enter_text":{"text":' + '"' + user + '"' + ',"link":"next_link"}}]}'

                if proxyche == "y":

                    while True:

                        for bb in range(5):
                            checkBroxy = False
                            try:

                                read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head,
                                              data=payload, proxies=proxyDict)
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
                else:
                    read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head, data=payload)

                dataa = read.json()
                flow_token = dataa['flow_token']
                #print(flow_token)
                print(Fore.GREEN + user + " Cofirmed")

            payload = '{"flow_token":"' + str(
                flow_token) + '","subtask_inputs":[{"subtask_id":"LoginEnterPassword","enter_password":{"password":' + '"' + password + '"' + ',"link":"next_link"}}]}'
            #print(payload)
            if proxyche == "y":

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:


                            read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head,
                                          data=payload,
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
            else:
                read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head, data=payload)

            try:
                dataa = read.json()
                #print(dataa)
                flow_token = dataa['flow_token']
                print(Fore.GREEN + " Successful password >>> " + password)
                #print(flow_token)
            except:
                Error = open("Error.text", "a")
                Error.write(f"@{user}:{password}:{email1}:{prpxxy}" "\n")
                print(Fore.RED+"Error-wrong password >>> " + email1)

            payload = '{"flow_token":"' + str(
                flow_token) + '","subtask_inputs":[{"subtask_id":"AccountDuplicationCheck","check_logged_in_account":{"link":"AccountDuplicationCheck_false"}}]}'
            #print(payload)
            if proxyche == "y":

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:


                            read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head,
                                          data=payload,
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
            else:
                read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head, data=payload)
            #print(read.json())
            dataa = read.json()
            flow_token = dataa['flow_token']
            #print(flow_token)
            tele = re.search("\:[0-9]", flow_token)
            chtele = tele.group()
            chtele = chtele[1:]
            chtele = str(chtele)

            if chtele == "7":
                if str(dataa['subtasks'][0]['enter_text']['hint_text'])=='Email address':
                    payload = '{"flow_token":"' + str(
                        flow_token) + '","subtask_inputs":[{"subtask_id":"LoginAcid","enter_text":{"text":"' + email1 + '","link":"next_link"}}]}'

                    #print("emm" + payload)
                    if proxyche == "y":

                        while True:

                            for bb in range(5):
                                checkBroxy = False
                                try:


                                    read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head,
                                                  data=payload, proxies=proxyDict)
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
                    else:
                        read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head, data=payload)

                    dataa = read.json()
                    flow_token = dataa['flow_token']
                    print(Fore.GREEN + email1 + " >>> Email Cofirmed")
                    #print(dataa)

                elif str(dataa['subtasks'][0]['enter_text']['hint_text'])=='Confirmation code' :
                    print(Fore.RED+ "need cood >>> " + email1)

                else:
                    payload = '{"flow_token":"' + str(
                        flow_token) + '","subtask_inputs":[{"subtask_id":"LoginAcid","enter_text":{"text":"@' + user + '","link":"next_link"}}]}'
                    # print("usss" + payload)

                    if proxyche == "y":

                        while True:

                            for bb in range(5):
                                checkBroxy = False
                                try:

                                    read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json",
                                                  headers=head,
                                                  data=payload, proxies=proxyDict)
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
                    else:
                        read = r.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers=head,
                                      data=payload)

                    dataa = read.json()

                    flow_token = dataa['flow_token']
                    print(Fore.RED + "Need User >>> " + user)
                    print(Fore.GREEN + user + " >>> User Cofirmed")



                #print(dataa)
                #print(flow_token)
            ################
            print(Fore.GREEN + "Enetered >>> "+ email1 )






            cookiesnew = ""
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

            if proxyche == "y":

                while True:

                    for bb in range(5):
                        checkBroxy = False
                        try:

                            req = r.get("https://twitter.com/home", headers=headers, proxies=proxyDict)
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
            else:

                req = r.get("https://twitter.com/", headers=headers)

            for cookienew in r.cookies.get_dict():
                # cookies=none
                cookiesnew = cookiesnew + cookienew + "=" + r.cookies.get_dict()[cookienew] + "; "

            coget = cookiesnew.encode("utf-8")
            #print(coget)
            aatok = re.search("[a-z]{5}\=[A-z0-9]{1,}\;", str(coget))
            auth = aatok.group()

            auth = auth[6:-1]

            cttok = re.search("\D\d\=[A-z0-9]{1,}\;", str(coget))
            ct0 = cttok.group()
            ct0 = ct0[3:-1]
            access = open("cookies.txt", "a")
            access.write(f"{auth}:{ct0}:@{user}:{password}:{email1}:{prpxxy}" "\n")
            #print("success")
            print(Fore.GREEN + "success >>> " + email1)
            rell = rell + 1
        except:
            Error = open("Error.text", "a")
            Error.write(f"@{user}:{password}:{email1}:{prpxxy}" "\n")
            print(Fore.RED+ "Error >>> " + email1)
            rell = rell + 1
        time.sleep(sleeti)

for tr in range(num_):
    file_name_ = t[tr]
    r = requests.session()
    rell = 30

    threading.Thread(target=dataaa, args=(file_name_, tr, rell)).start()






