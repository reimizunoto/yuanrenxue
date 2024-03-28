import requests
import numpy as np
import collections

def get_jssm(session):
    session.headers = {
        "Host": "match.yuanrenxue.cn",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Accept": "*/*",
        "Origin": "https://match.yuanrenxue.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://match.yuanrenxue.cn/match/3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,zh-CN;q=0.9"
    }
    cookies = {
        "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1711440094,1711505433",
        "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1711440065,1711505190",
        "qpfccr": "true",
        "no-alert3": "true",
        "m": "de2ea606de78601bfa7d1dcb6866e395|1711506718000",
        "sessionid": "05yg1dgrgjomdilz8v790fd7bompzamr",
        "tk": "-677797514432928300",
        "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1711506737",
        "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1711509264"
    }
    url = "https://match.yuanrenxue.cn/jssm"
    session.post(url, cookies=cookies, verify=False)


def get_page(page, session):
    session.headers = {
        "Host": "match.yuanrenxue.cn",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://match.yuanrenxue.cn/match/3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,zh-CN;q=0.9"
    }
    cookies = {
        "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1711440094,1711505433",
        "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1711440065,1711505190",
        "qpfccr": "true",
        "no-alert3": "true",
        "m": "de2ea606de78601bfa7d1dcb6866e395|1711506718000",
        "sessionid": "05yg1dgrgjomdilz8v790fd7bompzamr",
        "tk": "-677797514432928300",
        "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1711506737",
        "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1711509264"
    }
    url = "https://match.yuanrenxue.cn/api/match/3"
    params = {
        "page": "1"
    }
    response = session.get(url, cookies=cookies, params=params, verify=False)
    result = []
    for item in response.json()["data"]:
        result.append(item["value"])
    return result


if __name__ == '__main__':
    session = requests.Session()

    result = []
    for page in range(1, 6):
        get_jssm(session)
        print(session.cookies)
        temp = get_page(page, session)
        result.append(temp)
    res = np.array(result)
    res = res.reshape(-1)
    print(collections.Counter(res))
