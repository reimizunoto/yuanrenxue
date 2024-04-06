import requests
import time
import random
import execjs
import json
import numpy as np

if __name__ == '__main__':
    base_url = "https://match.yuanrenxue.cn/api/match/5"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = {
        "no-alert3": "true",
        "tk": "8548623720308057195",
        "sessionid": "98m4ownu1kda60clcjdrfl015d76ttss"
    }
    params = {}
    with open("./No.5/No.5.js", mode="r", encoding="utf-8") as f:
        exe = execjs.compile(f.read())
    params_data = exe.call("get_params")
    result = []
    for i in range(1, 6):
        params["page"] = f"{i}"
        params["m"] = params_data["params"]["m"]
        params["f"] = params_data["params"]["f"]
        cookies["RM4hZBv0dDon443M"] = params_data["cookies"]["RM4"]
        cookies["m"] = params_data["cookies"]["m"]
        response = requests.get(base_url, params=params, headers=headers, cookies=cookies)
        for each in response.json()["data"]:
            result.append(each["value"])
    result = sorted(result)
    print(sum(result[-5:]))

