
import json
import requests

from lxml import html

import time
import datetime
from openpyxl import load_workbook
import re

import random
import copy
import numpy as np
import os



def postdata(url, data, headers, filename):

    etext = ''

    proxies = {
        "http": 'http://89.223.80.30:8080',
        "https": 'http://89.223.80.30:8080'
    }

    try:
        #r = requests.post(url, data=data, headers=headers, timeout=3, proxies=proxies)
        r = requests.post(url, data=data, headers=headers, timeout=3)
        print(r.url)
        with open('./data/{}'.format(filename), 'w') as output_file:
            output_file.write(r.text)

        if r.status_code != 200:
            sk = 'post raise=' + str(r.raise_for_status()) + ' sk=' + str(r.status_code)
            if not os.path.exists('./data/sk.txt'):
                with open('./data/sk.txt', 'w') as output_file:
                    output_file.write('')
            with open('./data/sk.txt', 'a') as output_file:
                output_file.write(r.url + '|' + sk + '\n')


    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        etext = etext + "Http Error: " + str(errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        etext = etext + "Error Connecting: " + str(errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        etext = etext + "Timeout Error: " + str(errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
        etext = etext + "Something Else: " + str(err)

    if etext != '':
        with open('./data/sk.txt', 'a') as output_file:
            output_file.write(datetime.datetime.now().strftime("%H:%M:%S") + '|' + etext + '\n')

    return 0



def getdata(url, params, filename):

    etext = ''

    proxies = {
        "http": 'http://89.223.80.30:8080',
        "https": 'http://89.223.80.30:8080'
    }

    try:
        #r = requests.get(url, params=params, timeout=3, proxies=proxies)
        r = requests.get(url, params=params, timeout=3)
        print(r.url)
        with open('./data/{}'.format(filename), 'w') as output_file:
            output_file.write(r.text)

        if r.status_code != 200:
            sk = 'get raise=' + str(r.raise_for_status()) + ' sk=' + str(r.status_code)
            if not os.path.exists('./data/sk.txt'):
                with open('./data/sk.txt', 'w') as output_file:
                    output_file.write('')
            with open('./data/sk.txt', 'a') as output_file:
                output_file.write(r.url + '|' + sk + '\n')

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        etext = etext + "Http Error: " + str(errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        etext = etext + "Error Connecting: " + str(errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        etext = etext + "Timeout Error: " + str(errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
        etext = etext + "Something Else: " + str(err)

    if etext != '':
        with open('./data/sk.txt', 'a') as output_file:
            output_file.write(datetime.datetime.now().strftime("%H:%M:%S") + '|' + etext + '\n')

    return 0



def startchat(nick, isOnline = False):

    headers = {}
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["Connection"] = "keep-alive"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Content-Length"] = "64"
    headers["Host"] = "www.x-time.ru"
    headers["Referer"] = "https://chat.x-time.ru/"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"

    payload = {}
    payload["nick"] = nick.encode('cp1251')
    payload["pas"] = ''
    #payload["sex"] = '1'
    payload["sex"] = '0'
    payload["nc"] = '0'
    #payload["bold"] = 'on'
    #payload["mc"] = '4'
    payload["mc"] = '0'
    payload["sexual_o"] = '1'
    payload["x"] = '230'
    payload["y"] = '10'

    if isOnline:
        postdata('https://www.x-time.ru/cgi-bin/startchat.cgi', payload, headers, 'startchat.txt')
        """
        r = requests.post('https://www.x-time.ru/cgi-bin/startchat.cgi', data=payload, headers=headers, timeout=100)
        print(r.url)
        with open('./data/startchat.txt', 'w') as output_file:
            output_file.write(r.text)
            #print(r.text)
        #"""

    return 0




def refreshchat_opera(userID, isOnline = False):

    payload = {}
    payload["user"] = userID

    if isOnline:
        getdata('https://www.x-time.ru/cgi-bin/refreshchat_opera.cgi', payload, 'refreshchat_opera.txt')
        """
        r = requests.get('https://www.x-time.ru/cgi-bin/refreshchat_opera.cgi', params=payload, timeout=100)
        print(r.url)
        with open('./data/refreshchat_opera.txt', 'w') as output_file:
            output_file.write(r.text)
            #print(r.text)
        #"""

    return 0


def sendmessage_v15_opera(message, userID, nickTo, privateTo = '', isOnline = False):

    headers = {}
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["Connection"] = "keep-alive"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Content-Length"] = "0"
    headers["Host"] = "www.x-time.ru"
    #headers["Referer"] = "https://www.x-time.ru/cgi-bin/chatform_opera.cgi?user={0}&bold=on&cursiv=&underline=&bolds=&cursivs=&underlines=&nc=0&mc=0&s=1&nick={1}&n=0".format(userID, nick).encode('cp1251')
    headers["Referer"] = "https://www.x-time.ru/cgi-bin/chatform_opera.cgi"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"

    payload = {}
    payload["user"] = userID
    #payload["bold"] = 'on'
    payload["cursiv"] = ''
    payload["underline"] = ''
    payload["bolds"] = ''
    payload["cursivs"] = ''
    payload["underlines"] = ''
    payload["nc"] = '0'
    #payload["mc"] = '4'
    payload["mc"] = '0'
    if nickTo != '':
        payload["message"] = str(nickTo + ', ' + message).encode('cp1251')
    else:
        payload["message"] = str(message).encode('cp1251')

    payload["x"] = '12'
    payload["y"] = '8'
    payload["pr"] = ''

    if privateTo != '':
        payload["pr"] = 'on'

    payload["privat"] = privateTo.encode('cp1251')

    if isOnline:
        postdata('https://www.x-time.ru/cgi-bin/sendmessage_v15_opera.cgi', payload, headers, 'sendmessage_v15_opera.txt')
        """
        r = requests.post('https://www.x-time.ru/cgi-bin/sendmessage_v15_opera.cgi', data=payload, headers=headers, timeout=100)
        print(r.url)
        with open('./data/sendmessage_v15_opera.txt', 'w') as output_file:
            output_file.write(r.text)
            #print(r.text)
        #"""

    return 0


def chatonline_opera(userID, isOnline = False):

    if isOnline:
        getdata('https://www.x-time.ru/cgi-bin/chatonline_opera.cgi?user=' + userID, {}, 'chatonline_opera.txt')
        """
        r = requests.get('https://www.x-time.ru/cgi-bin/chatonline_opera.cgi?user=' + userID, timeout=100)
        print(r.url)
        with open('./data/chatonline_opera.txt', 'w') as output_file:
            output_file.write(r.text)
            #print(r.text)
        #"""

    return 0


def awaychat(userID, isOnline = False):

    if isOnline:
        getdata('https://www.x-time.ru/cgi-bin/awaychat.cgi?' + userID, {}, 'awaychat.txt')
        """
        r = requests.get('https://www.x-time.ru/cgi-bin/awaychat.cgi?' + userID, timeout=100)
        print(r.url)
        with open('./data/awaychat.txt', 'w') as output_file:
            output_file.write(r.text)
            #print(r.text)
        #"""

    return 0


def chat_read(filename):

    with open('./data/{}'.format(filename), 'r') as file:
        text = file.read()

    # иначе ошибка в xpath метод html.fromstring
    if text == "":
        text = "<html></html>"

    return text



def read_stop():

    with open('./data/stop.txt', 'r') as file:
        text = file.read()

    return len(text) > 0    # если в файле есть хоть один символ - стоп



def startchat_process(strData):

    rows = re.findall(r'user = \"(.\d+)\";', strData)
    userID = ''
    if len(rows) > 0:
        userID = rows[0]
    return userID


# оповещает о выходе пользователя из чата
def chatonline_opera_process_afk(users):

    # если текущее время отличается от времени последнего онлайна на n секунд и статус онлайн, то засчитать выход
    # если в предыдущем списке был, а сейчас нет - засчитать выход.

    afk = []                                        # список вышедших пользователей
    oli = []                                        # online list
    min = datetime.datetime.min
    answer = ""


    for userName in users:
        if userName == 'refresh': continue
        if min < users[userName]['last_online']:
            min = users[userName]['last_online']

    for userName in users:
        if userName == 'refresh': continue
        if users[userName]['online']:
            delta_time = min - users[userName]['last_online']
            ts = delta_time.total_seconds()
            if ts >= 10:                                # ставим офлайн
                users[userName]['online'] = False
            if (ts >= 10) and (ts <= 60):               # формируем список, не содержащий вышедших очень давно
                afk.append(users[userName]['name'])
            if ts == 0:
                oli.append(users[userName]['name'])


    for userName in afk:
        answer += userName + ", "

    if answer != '':


        question = answer[:-2]

        #count_i =
        first_i = len(oli)-(len(oli)//5)-1
        last_i = len(oli)-1
        answers = {
            '1': 'пака ' + question,
            '2': 'покуши ' + question,
            '3': 'баюшки ' + question,
            '4': question + ' ушел совсем #smail',
            #'3': question + ' помни, ' + oli[len(oli)-1] + ' будет скучать по тебе!',
            '5': question + ' помни, ' + oli[random.randint(first_i, last_i)] + ' будет скучать по тебе! #smail'
        }
        answer = answers[str(np.random.randint(1, 5+1))]

        smiles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 19]
        while answer.find('#smail') > -1:
            smail = ' !{:02d}'.format(smiles[random.randint(0, len(smiles) - 1)])
            answer = answer.replace('#smail', smail, 1)



        #sendmessage_v15_opera(answer, userID, nickTo='unvil222', privateTo='unvil222', isOnline=isOnline)
        sendmessage_v15_opera(answer, userID, nickTo='', privateTo='', isOnline=isOnline)

        print(answer)

    return 0





# Fills data into 'users' dictionary
# strData = all text from chatonline_opera.txt
# users = {} or dictionary with data
def chatonline_opera_process(strData, users):

    now = datetime.datetime.now()
    min = datetime.datetime.min                                             # нулевое время онлайн

    listData = re.findall(r'<tr>(.+)</tr>', strData)                        # делим файл на строки

    for indx, row in enumerate(listData):

        userName = re.findall(r'javascript:info\(\'(.+?)\'\)', row)[0]      # ник. ? - ленивый квантификатор
        userNameFull = userName
        userName = userName.lower()

        #print(indx, ' - ', userName)

        if row.find('/man.jpg') > -1:
            sex = 'man'

        if row.find('/woman.jpg') > -1:
            sex = 'woman'


        users['refresh'] = now.strftime("%m/%d/%Y, %H:%M:%S")

        if userName not in users:
            users[userName] = {}

        users[userName]['name'] = userNameFull
        users[userName]['indx'] = indx
        users[userName]['sex'] = sex

        if 'time_online' not in users[userName]:        # очевидно пересечение с условием userName not in users, но по логике это отдельный абзац
            users[userName]['time_online'] = min
        else:
            delta_time = now - users[userName]['last_online']
            ts = delta_time.total_seconds()
            if ts <= 40:
                users[userName]['time_online'] += delta_time

        users[userName]['last_online'] = now
        users[userName]['online'] = True

        #print(users[userName]['time_online'].strftime("%H:%M:%S"))

    return 0



# Fills data into 'msgs' list
# strData = all text from refreshchat_opera_opera.txt
# msgs = [] or list with old messages
def refreshchat_opera_process(strData, msgs):
    listData = re.findall(r'messages.push\(\"(.+)\"\);', strData)       # делим файл на строки

    for indx, row in enumerate(listData):

        msg = {}
        msg['time'] = re.findall(r'size=1><i>(.+?)</i>', row)[0]        # время. ? - ленивый квантификатор
        msg['from'] = re.findall(r'mesform.pr\(\'(.+?)\'\)', row)[0]
        msg['msg'] = re.findall(r'</a>: (.+)<BR>', row)[0]


        tree = html.fromstring(msg['msg'])
        msg_row = tree.xpath('.//text() | .//img/@src')                 # текст сообщений и смайлы

        msg_text = ''
        for item in msg_row:
            msg_text = msg_text + item

        if msg['from'] == 'HQ':
            msg_text = msg_row[0] + msg_row[1] + msg_row[2]             # в чат зашел |считалка|. Поприветствуем!

        msg_to = re.findall(r'^(\w+),', msg_text)                       # разделяем Кому, и текст сообщения
        if len(msg_to) > 0:
            msg['to'] = msg_to[0]
            msg_end = re.findall(r'^\w+,(.*)$', msg_text)[0].strip()
            msg_text = msg_end

        msg['text'] = msg_text


        if row.find('</a>-><a href=') > -1:
            msg['to'] = re.findall(r'mesform.pr\(\'(.+?)\'\)', row)[1]
            msg['private'] = 1

        msg.pop('msg')

        msgs.append(msg)

        #print(msg)


    return 0





def sendmessage_v15_opera_process(nick, users, msgs):

    antiflood = {}      # структура - пользователь: количество сообщений
    sleeptime = 0       # задержка ответа в секундах. В приват - меньше, в общий - больше.
    flood = 4           # номер пропускаемого сообщения

    a = 5
    while (len(msgs) > 0 and a > 0):

        msg = msgs.pop(0)

        if 'to' not in msg:
            continue

        if msg['from'] == nick:
            continue


        smail = ''
        if msg['to'] == nick:

            key = msg['from']
            if key not in antiflood:
                antiflood[key] = 1
            else:
                antiflood[key] += 1
                if antiflood[key] >= flood:
                    continue

            if antiflood[key] >= flood-1:
                answer = 'помедленнее, я записываю'                         # предупреждение - это не пропускаемое сообщение
            else:

                rows = re.findall(r'\w+', msg['text'])                      # начало формирования ответа
                if len(rows) != 1:                                          # в тексте > 1 слова

                    """ 
                    # случайный смайл интереснее
                    if msg['text'] != '':
                        gifs = re.findall(r'/(\w+).gif', msg['text'])
                        if len(gifs) > 0:
                            smail = ' !' + gifs[-1]
                    """

                    answers = {
                        '1': 'пожалуйста только ник и ничего больше)',
                        '2': 'всего лишь скажи имя )',
                        '3': 'ты знаешь ' + msg['from'] + '? а я уже знаю) о ком тебе рассказать?',
                        '4': 'придумай что-нить поинтереснее! А лучше ник напиши.',
                        '5': 'что ты задумал! только ник пиши и ничего больше! )',
                        '6': 'что это еще за детские сказки! ник напиши',
                        '7': 'давай замутим счастье? ты только ник напиши',
                        '8': 'с ума сошел? ты знаешь что я хочу)',
                        '9': 'тук-тук, у тебя все дома? ник пиши',
                        '10': 'не хочу тебе отвечать)',
                        '11': 'хомяки кучковались кучковались да не выкучковались! всё понятно? пиши ник'
                    }
                    answer = answers[str(np.random.randint(1, 11+1))]

                    question = msg['text'].lower()
                    if question.find('хочеш') > -1:
                        answer = 'как ты хочешь?'

                    if question.find('трахн') > -1:
                        answer = 'мне тебя жалко!'

                    if question.find('дроч') > -1:
                        answer = 'мне тебя жалко, ты урод!'

                    if question.find('веди себя тихо') > -1:
                        answer = 'ок, буду!'
                        global silent
                        silent = not silent


                else:
                    question = rows[0].lower()
                    if question in users:
                        timeO = users[question]['time_online'].strftime("%H:%M")
                        timeL = users[question]['last_online'].strftime("%H:%M:%S")
                        #ts = (users[question]['time_online'] - datetime.datetime(1970, 1, 1)).total_seconds()
                        ts = (users[question]['time_online'] - datetime.datetime.min).total_seconds()
                        #timeO = str(int(ts // 60))
                        uname = users[question]['name']

                        answer = 'я видел ' + question + ' в течение ' + timeO + ' минут до ' + timeL + '. А ты?)'
                        #заглядывал сюда сегодня на ! минут, видел его в
                        #я заметил, что ! был здесь в течение ! минут до !
                        #! хитрый товарищ, просидел ! минут и ушёл в ! не попрощавщись ((( даже с Греей111
                        #все понятно, ! проторчал здесь ! минут последний раз в !

                        answers = {
                            '1': uname + ' заглядывал сюда сегодня на ' + timeO + ' минут, видел его в ' + timeL,
                            '2': 'я заметил, что ' + uname + ' был здесь в течение ' + timeO + ' минут до ' + timeL,
                            '3': uname + ' хитрый товарищ, просидел ' + timeO + ' минут и ушёл в ' + timeL + ' не попрощавщись ((( даже с Греей111',
                            '4': 'все понятно, ' + uname + ' проторчал здесь ' + timeO + ' минут последний раз в ' + timeL,
                            '5': 'я кое-что знаю, но промолчу, попробуй еще разок!)',
                            '6': 'милая ' + uname + ' общалась с девчонками ' + timeO + ' минут до ' + timeL,
                            '7': 'няшка ' + uname + ' общался с парнями ' + timeO + ' минут до ' + timeL
                        }
                        answer = answers[str(np.random.randint(1, 7+1))]

                    else:
                        # answer = question + ' кто такой? ) сегодня не видел'
                        # answer = 'так ) ' + question + ' не видел.'

                        # может быть ты ! с кем-то путаешь? не знаю такого
                        # ничего я тебе не скажу, сам ищи ! я его не видел
                        # спроси лучше про ! у кого-нибудь еще, я не знаю о ком ты
                        # спроси у ! он уже давно здесь!

                        answers = {
                            '1': question + ' кто такой? ) сегодня не видел',
                            '2': 'так ) ' + question + ' не видел.',
                            '3': 'милый, что?',
                            '4': 'сам ты ' + question + ' я такого не знаю!',
                            '5': 'укуси тебя дикая пчела за задницу! Кто ' + question + ' вообще такой?',
                            '6': 'спроси у ' + list(users.items())[1][0] + ' он уже давно здесь!',
                        }
                        answer = answers[str(np.random.randint(1, 5+1))]


                        if question.find('здравствуй') > -1:
                            answer = 'приветик! "справка" - покажу) '

                        if question.find('привет') > -1:
                            answer = 'приветик! "справка" - покажу) '

                        if question.find('справка') > -1:
                            answer = 'Пиши "справка" - эта справка! Пиши "веди себя тихо" - показать/скрыть время выхода.'

                        if question.find('help') > -1:
                            answer = 'Пиши "справка" - эта справка! Пиши "веди себя тихо" - показать/скрыть время выхода.'


            if smail == '':
                smail = ' !{:02d}'.format(np.random.randint(1, 16+1))

            answer = answer + smail

            privateTo = ''
            if 'private' in msg:
                privateTo = msg['from']
                sleeptime = 2       # в приват
            else:
                sleeptime = 10      # в общий

            nickTo = msg['from']

            sendmessage_v15_opera(answer, userID, nickTo, privateTo=privateTo, isOnline=isOnline)

            strData = chat_read('sendmessage_v15_opera.txt')
            refreshchat_opera_process(strData, msgs)

            if not os.path.exists('./data/answers.txt'):
                with open('./data/answers.txt', 'w') as output_file:
                    output_file.write('')

            with open('./data/answers.txt', 'a') as output_file:
                txt = msg['from'] +'|t=' + datetime.datetime.now().strftime("%m/%d/%Y, ") + msg['time'] + '|p=' + privateTo + '|q=' + msg['text'] + '|a=' + answer + '\n'
                output_file.write(txt)
                print(txt)

            a = a - 1
            time.sleep(sleeptime)

    return 0



def users_save(users_list, filename = 'users.txt'):


    users = copy.deepcopy(users_list) # иначе меняется сам словарь пользователей

    for indx, user in enumerate(users):
        if indx == 0:                                   # key = refresh
            continue
        users[user]['time_online'] = users[user]['time_online'].isoformat()
        users[user]['last_online'] = users[user]['last_online'].isoformat()


    if not os.path.exists('./data/{}'.format(filename)):
        with open('./data/{}'.format(filename), 'w') as output_file:
            output_file.write('')

    with open('./data/{}'.format(filename), 'a') as file:
        dumps = json.dumps(users, ensure_ascii=False)   # type(dumps) = string
        file.write(dumps + '\n')

    return 0


def users_load(filename = 'users.txt'):

    users = {}
    text = ''

    if os.path.exists('./data/{}'.format(filename)):
        with open('./data/{}'.format(filename), 'r') as file:
            text = file.read()

    rows = text.splitlines()

    if len(rows) > 0:
        users = json.loads(rows[-1])

    for indx, user in enumerate(users):
        if indx == 0:
            continue
        users[user]['time_online'] = datetime.datetime.fromisoformat(users[user]['time_online'])
        users[user]['last_online'] = datetime.datetime.fromisoformat(users[user]['last_online'])

    #print(type(users), users)

    return users







### ************************ program start here ***************************
### xtime bot v.1.0



nick1 = "считалкабот"
#nick = "unvil222"
#privateTo = "unvil222"
#privateTo = ""
isOnline = True                 # запускать True = онлайн / False = автономно
silent = False                  # вести себя тихо, не отображать в общий чат время выхода пользователей

users1 = {}
msgs1 = []

users1 = users_load()


inchat = 0                                                      # длина ID
if not read_stop():                                             # разрешение входа
    startchat(nick1, isOnline)
    strData = chat_read('startchat.txt')
    userID = startchat_process(strData)
    inchat = len(userID) > 0    # длина строки



while inchat and not read_stop():

    # получить список пользователей
    # обработать список пользователей
    # получить список сообщений - только текст

    # к = количество сообщений, если больше 0 то обработать, k + 1. При k = 10 перелогин (выход).

    # обработать список сообщений - занести ответы в лист
    # разослать ответы (не более 5) и занести новые в лист


    k = 0
    save_k = 0

    while k <= 10 and not read_stop():

        time.sleep(4.5)
        chatonline_opera(userID, isOnline)
        refreshchat_opera(userID, isOnline)

        strData = chat_read('chatonline_opera.txt')
        chatonline_opera_process(strData, users1)

        if not silent and (save_k % 3 == 0):
            chatonline_opera_process_afk(users1)

        strData = chat_read('refreshchat_opera.txt')            # чтение сообщений

        refreshchat_opera_process(strData, msgs1)               # обработка сообщений, заполняется msgs



        #print(users)
        #print(msgs)
        if save_k == 20:
            users_save(users1)
            save_k = 0
        else:
            save_k += 1



        new_mes_count = len(msgs1)
        print('mes in  = {}'.format(new_mes_count))

        if new_mes_count == 0:
            k += 1
        else:
            k = 0

        time.sleep(8)                                           # задержка ответа
        sendmessage_v15_opera_process(nick1, users1, msgs1)

        print('mes out = {}, k = {}'.format(len(msgs1), k))




        if not os.path.exists('./data/answers.txt'):
            with open('./data/answers.txt', 'w') as output_file:
                output_file.write('')

        with open('./data/answers.txt', 'a') as output_file:
            #output_file.write(str(users) + '\n')
            if len(msgs1) > 0:
                output_file.write(str(msgs1) + '\n')

        #time.sleep(4)
        #break      # - k <= 3 and not read_stop()


    # если завершаем программу, выходим из чата, иначе перелогин
    if read_stop():
        awaychat(userID, isOnline)
    else:

        sendmessage_v15_opera('test', userID, nickTo=nick1, privateTo=nick1, isOnline=isOnline)
        strData = chat_read('sendmessage_v15_opera.txt')
        refreshchat_opera_process(strData, msgs1)

        new_mes_count = len(msgs1)

        if new_mes_count == 0:
            print('test ERROR')
        else:
            print('test OK')


        cnt = len(users1.items())
        you = list(users1.items())[random.randint(1, cnt - 1)][0]
        answers = {
            '1': 'что-то скучно тут, пожалуй перезайду)',
            '2': 'щас усну !14',
            '3': 'и куда все подевались? цып цып цып!',
            '4': '!14',
            '5': '!14 перезайти что ли',
            '6': 'ну-ка! где мои цыплятки?',
            '7': you + ', ну-ка говори куда все делись! !05',
        }
        answer = answers[str(random.randint(1, len(answers)-1))]
        sendmessage_v15_opera(answer, userID, nickTo='', privateTo='', isOnline=isOnline)

        with open('./data/answers.txt', 'a') as output_file:
            txt = 'relogin|t=' + datetime.datetime.now().strftime("%H:%M:%S") + '|a=' + answer + '\n'
            output_file.write(txt)
            print(txt)

        print('Relogin!!!')
        awaychat(userID, isOnline)
        time.sleep(10)

        startchat(nick1, isOnline)
        strData = chat_read('startchat.txt')
        userID = startchat_process(strData)
        inchat = len(userID) > 0    # длина строки

        if inchat:
            time.sleep(1)
            strData = chat_read('refreshchat_opera.txt')    # пропуск старых сообщений, чтобы не прочитать их в основном цикле


    #break      # - inchat and not read_stop()


users_save(users1)
#awaychat(userID, isOnline)
print('end.')




"""
            with open('./data/chatonline_json.txt', 'w') as outfile:
                json.dump(users, outfile)
            
            with open('data.txt') as json_file:  
                data = json.load(json_file)
            
# статистика
endTime = datetime.datetime.now()
deltaTime = endTime - startTime
ts = deltaTime.total_seconds()
hours = ts / 3600
minutes = (ts % 3600) / 60
print("time = {0:f} h, {1:f} min, {2:d} sec | ts = {3:f}".format(hours, minutes, deltaTime.seconds, ts))
strftime("%Y-%m-%d-%H.%M.%S")            
print(users[userName]['time_online'].strftime("%H:%M:%S"))
            
    tree = html.fromstring(listData[0])

    rows = tree.xpath('.//td/a/@href')[0]

    print(rows)
    """



"""
    time.sleep(0.5)

    # если завершаем программу, выходим из чата, иначе перелогин
    if read_stop():
        awaychat(userID)
    else:
        userID = getID()
        inchat = len(userID) > 0

    #"""








