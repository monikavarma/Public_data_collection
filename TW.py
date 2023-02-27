from idlelib.multicall import r

import requests
# from botocore.vendored import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
import ssl
import json
import pandas as pd
from threading import Thread

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

url = "https://electoralsearch.in/Home/GetCaptcha?image=true&id="

try:
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    result = requests.get(url, verify=False)
    cookies = dict((x, y) for x, y in result.cookies.items())
    print(cookies)

except requests.exceptions.ConnectionError:
    print("connection error")
file = open("resp_content.png", "wb")
file.write(result.content)
file.close()
file = open("vID_vb1].txt")
list4 = file.readlines()
list = []
captcha = input()
cookies_dict = {}

file1 = open("data.json", "w+")  # append mode
file1.seek(0)
file1.write("[")


def request_search_terms(*args):
    # your logic for a request goes here
    for i in range(1, 4):
        file = open("vo" + str(i) + ".txt")
        for line in file:
            list = file.readlines()
            for i in range(len(list)):
                s = requests.Session()

                url1 = "https://electoralsearch.in/Home/searchVoter?epic_no=" + list[
                    i] + "&page_no=1&results_per_page=10&reureureired=ca3ac2c8-4676-48eb-9129-4cdce3adf6ea&search_type=epic&state=U05&txtCaptcha=" + captcha
                results = s.get(url1, cookies=cookies, verify=False)
                data = json.loads(results.text)
                dataframe = pd.DataFrame.from_dict(data, orient="index")
                print(dataframe.to_string())
                with open('data.json', 'a', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    f.write(",")

            pass


def random(id):
    list1 = [id]
    with open("vID_vb1].txt", 'r') as f:
        while not id in next(f):
            pass
        for line in f:
            list1.append(line)
            for i in range(len(list1)):
                s = requests.Session()
                url1 = "https://electoralsearch.in/Home/searchVoter?epic_no=" + list1[
                    i] + "&page_no=1&results_per_page=10&reureureired=ca3ac2c8-4676-48eb-9129-4cdce3adf6ea&search_type=epic&state=U05&txtCaptcha=" + captcha
                results = s.get(url1, cookies=cookies, verify=False)
                data = json.loads(results.text)
                dataframe = pd.DataFrame.from_dict(data, orient="index")
                print(dataframe.to_string())
                with open('data.json', 'a', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    f.write(",")

            pass
        pass
    pass


def random1(id):
    pay_attention = False
    with open("vID_vb1].txt", 'r') as f:
        for line in f:

            if pay_attention:
                continue
            else:  # We haven't found our trigger yet; see if it's in this line
                if id in line:
                    pay_attention = True
                    list4.append(line)
                    for i in range(len(list4)):
                        s = requests.Session()
                        url1 = "https://electoralsearch.in/Home/searchVoter?epic_no=" + list4[
                            i] + "&page_no=1&results_per_page=10&reureureired=ca3ac2c8-4676-48eb-9129-4cdce3adf6ea&search_type=epic&state=U05&txtCaptcha=" + captcha
                        results = s.get(url1, cookies=cookies, verify=False)
                        data = json.loads(results.text)
                        dataframe = pd.DataFrame.from_dict(data, orient="index")
                        print(dataframe.to_string())
                        with open('data.json', 'a', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, indent=4)
                            f.write(",")

                pass


p = ""

f = open("data.json")

for line in f:
    line = line.strip()
    p = line
file1 = open("data.json", "a")  # append mode
file1.write("]")

choice = input('choose options 1.all voter id", " 2.start from partivular id ')
print(choice)

if choice == 'all':
    threads = []
    try:
        for st in request_search_terms():
            threads.append(Thread(target=request_search_terms, args=(st,)))

            threads[-1].start()

    except:
        print("Wrong captcha or File end")
        captcha = input()
        request_search_terms()
    for t in threads:
        t.join();
elif choice == 'random':
    voter_id = input("enter id")
    threads = []
    try:
        for st in random1(voter_id):
            threads.append(Thread(target=request_search_terms, args=(st,)))

            threads[-1].start()

    except:
        print("Wrong captcha or File end")
        captcha = input()
        request_search_terms()
    for t in threads:
        t.join();

else:
    print('Try again.')

os.remove("resp_content.png")
