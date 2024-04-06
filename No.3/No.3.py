import requests
import numpy as np
import collections

def get_jssm(session):
    url = "https://match.yuanrenxue.cn/jssm"
    session.post(url, verify=False)


def get_page(page, session):
    url = "https://match.yuanrenxue.cn/api/match/3"
    params = {
        "page": f"{page}"
    }
    response = session.get(url, params=params, verify=False)
    result = []
    for item in response.json()["data"]:
        result.append(item["value"])
    return result


if __name__ == '__main__':
    session = requests.Session()
    session.headers = {
        "Host": "match.yuanrenxue.cn",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Origin": "https://match.yuanrenxue.cn",
        "Referer": "https://match.yuanrenxue.cn/match/3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,zh-CN;q=0.9"
    }
    cookies = {
        "qpfccr": "true",
        "no-alert3": "true",
        "m": "de2ea606de78601bfa7d1dcb6866e395|1711506718000",
        "sessionid": "05yg1dgrgjomdilz8v790fd7bompzamr",
        "tk": "-677797514432928300"
    }
    session.cookies.update(cookies)
    result = []
    for page in range(1, 6):
        get_jssm(session)
        print(session.cookies)
        temp = get_page(page, session)
        result.append(temp)
    res = np.array(result)
    res = res.reshape(-1)
    print(collections.Counter(res))
