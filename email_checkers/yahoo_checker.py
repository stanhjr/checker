import requests
import re


def yahoo_checker(email):
    try:
        username = email.split("@")[0]
        host = email.split("@")[1]
        if host != "yahoo.com":
            return False
    except:
        return False
    s = requests.Session()
    link = 'https://login.yahoo.com/account/create?.intl=us&.lang=en-US&src=ym&activity=ybar-mail&pspid=2023538075&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail&specId=yidReg&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    try:
        resp = s.get(link, headers=headers).text
    except:
        return None
    specData = re.findall(r'value="(.*?)" name="specData"', resp)[0]
    crumb = re.findall(r'value="(.*?)" name="crumb"', resp)[0]
    acrumb = re.findall(r'value="(.*?)" name="acrumb"', resp)[0]
    link = "https://login.yahoo.com/account/module/create?validateField=yid"
    headers = {
        'Referer': 'https://login.yahoo.com/account/create?.intl=us&.lang=en-US&src=ym&activity=ybar-mail&pspid=2023538075&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail&specId=yidReg&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-360,"timezone":"Asia/Dhaka","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"1","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 520 Direct3D11 vs_5_0 ps_5_0, D3D11-20.19.15.4380)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1624081774716,"render":1624081773747}}',
        'specId': 'yidreg',
        'cacheStored': '',
        'crumb': crumb,
        'acrumb': acrumb,
        'done': 'https://mail.yahoo.com/d?pspid=2023538075&activity=ybar-mail',
        'googleIdToken': '',
        'authCode': '',
        'attrSetIndex': '0',
        'specData': specData,
        'tos0': 'oath_freereg|us|en-US',
        'firstName': '',
        'lastName': '',
        'yid': username,
        'password': '',
        'shortCountryCode': 'US',
        'phone': '',
        'mm': '',
        'dd': '',
        'yyyy': '',
        'freeformGender': '',
        'signup': '',
    }
    try:
        resp = s.post(link, headers=headers, data=data).json()
    except:
        return None
    all_errors = resp.get('errors', [])
    if len(all_errors) == 0:
        return None
    for errors in all_errors:
        if errors.get('name') == "yid":
            return True
    return False

