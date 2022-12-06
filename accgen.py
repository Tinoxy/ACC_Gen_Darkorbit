import re
import random
import string
import requests
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def register(Username,Password,Serverid):

    url = "https://www.darkorbit.com/"
    token = requests.get(url, headers=headers)
    soup = BeautifulSoup(token.content, 'lxml')
    get = soup.find('form', attrs={'class': 'bgc_signup_form'}) ['action']

    with open("api.txt") as f:
        for i, line in enumerate(f):
            line = line.strip()

            if len(line) > 0:
                # this will only run when the line is NOT empty

                data, _ = line.split(';')

    solver = TwoCaptcha(data)

    g_recaptcha = ''
    try:
        result = solver.recaptcha(
            sitekey='6LfkgUIUAAAAAETf-SZEx_exK2SEPirE8i2RZQ_U',
            url='https://www.darkorbit.com/',
            invisible=1)

    except Exception as e:
        print("You need a TwoCaptcha API!!!")
        exit(e)
    else:
        g_recaptcha = result['code']

    payload = {
    'username': Username,
    'password': Password,
    'email': random_char(12) + "@gmail.com",
    'termsAndConditions': '1',
    'g-recaptcha-response': g_recaptcha
    }


    login = requests.post(get, payload)
    Server = login.url.rsplit("/",2)[1]



    payload_reg1 = {
        'action': 'internalCompanyChoose',
        'subaction': 'factionChoose',
        'factionID': '2'
    }



    requests.get(f'https://{Server}/indexInternal.es?action=internalCompanyChoose&subaction=factionChoose&factionID=1', payload_reg1, cookies=login.cookies)

    payload_inernalStart = {
        'action': 'internalStart'
    }

    requests.get(f'https://{Server}/indexInternal.es?action=internalStart', payload_inernalStart, cookies=login.cookies)

    php_payload = {
        'command': 'getInstanceList'
    }

    oldserver = requests.post(f'https://{Server}/ajax/instances.php', php_payload, cookies=login.cookies)
    soup = BeautifulSoup(oldserver.text, 'lxml')

    server_need_edit = soup.find('tr', {'id': re.compile('serverSelection_ini_1389')}) ['target']




    server_link_edit = server_need_edit[32:]
    serverid = server_link_edit [:-2]


    server_company = requests.post(f"https://{Serverid}.darkorbit.com//{serverid}")

    server_Link = server_company.url.rsplit("/",2)[1]



    payload_reg_server = {
        'action': 'internalCompanyChoose',
        'subaction': 'factionChoose',
        'factionID': '2'
    }


    requests.get(f'https://{server_Link}/indexInternal.es?action=internalCompanyChoose&subaction=factionChoose&factionID=1', payload_reg_server, cookies=server_company.cookies)

    payload_inernalStart_gbl1 = {
    'action': 'internalStart'
    }

    requests.get(f'https://{server_Link}/indexInternal.es?action=internalStart', payload_inernalStart_gbl1, cookies=server_company.cookies)
    requests.get(f'https://{server_Link}.darkorbit.com/flashAPI/dailyLogin.php?doBook=1')
