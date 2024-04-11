import requests
import re
import subprocess
import execjs

all_sum =  0
count = 0
session = requests.Session()
headers = {
    "user-agent": "yuanrenxue.project",
}
session.headers = headers

def get_cookie_m(m_max, timestamp):
    out = subprocess.Popen(["node", "No.9\\No.9.js", str(m_max), timestamp], stdout=subprocess.PIPE)
    cookies_m = out.stdout.read().decode("utf-8").strip()
    return cookies_m

def set_cookie_m():
    url = "https://match.yuanrenxue.cn/match/9"
    response = session.get(url)
    # 获取for循环代码
    code = re.findall(r"window=new Array\(\);(.*?var m=.*?)document", response.text, re.S)[0]
    
    # 获取时间戳
    try:
        timestamp = re.findall(r"decrypt\(\'(.*?)\'\)", code)[0]
    except IndexError:
        timestamp = re.findall(r"\(decrypt,\'(.*?)\'\)", code)[0]
    
    # 获取m值
    try:
        m_max = re.findall(r"\(m,(.*?)\);m\+\+", code)[0]
    except IndexError:
        m_max = re.findall(r"m<=(.*?);m\+\+", code)[0]
        
    
    # 获取cookie_m值
    with open("No.9\\No.9.js", "r", encoding="utf-8") as f:
        js_code = f.read()
    func = execjs.compile(js_code)
    cookies_m = func.call("get_m", m_max, timestamp)
    # cookies_m = get_cookie_m(m_max, timestamp)
    session.cookies.update({"m": cookies_m})

def get_data(page):
    global all_sum
    global count
    url = 'https://match.yuanrenxue.cn/api/match/9?page=' + str(page)
    res = session.get(url)
    print(res.text)

    for data in res.json()['data']:
        all_sum += data['value']
        count += 1

if __name__ == "__main__":
    
    set_cookie_m()
    for page in range(1, 6):
        get_data(page)
    print("评论平均数-->", all_sum/count)