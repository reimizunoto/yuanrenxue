import json
import requests
import time
import execjs


if __name__ == '__main__':


    with open("./No.2.js",mode="r",encoding="utf-8") as f:
        json_code = f.read()

    exec = execjs.compile(json_code)


    url = "https://match.yuanrenxue.cn/api/match/2?page="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    }
    result = []
    for page in range(1,6):
        page_url = url + str(page)
        headers["Cookie"] = exec.call("get_m")
        print(url + " : " + headers["Cookie"])
        res = requests.get(page_url, headers=headers)
        for var in res.json()["data"]:
            result.append(var["value"])
    print(result)
    print(sum(result))
