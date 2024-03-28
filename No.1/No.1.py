import requests
import execjs
import json
import math
def get_page_data(data, page):
    url = f"https://match.yuanrenxue.cn/api/match/1?page={page}&m={data["m"]}%E4%B8%A8{data["time"]}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    }
    response = requests.get(url, headers=headers, data=json.dumps(data,separators=(',',':')))
    page_data = response.json()["data"]
    result = []
    for data in page_data:
        result.append(data["value"])
    return result

if __name__ == '__main__':
    with open("./No.1.js", mode="r", encoding="utf-8") as f:
        page_js =  f.read()

    exec = execjs.compile(page_js)

    i = 1
    result = []
    while i <= 5:
        res = exec.call("get_m")
        response = get_page_data(res, i)
        result.append(response)
        i += 1
    for data in result:
        print(data)
    result = [b for a in result for b in a]
    print(result)
    print(sum(result)/len(result))