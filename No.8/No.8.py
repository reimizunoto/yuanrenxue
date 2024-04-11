import requests
import re
import cv2
import numpy as np
import base64
from cnradical import Radical, RunOption
from verify import Verify_code
import json

APP_ID = ''
API_Key = ''
Secret_Key = ''

all_word_ocr_result = []


def get_verify(session):
    url = 'http://match.yuanrenxue.com/api/match/8_verify'
    response = session.get(url=url)
    print(response.json())
    html_str = response.json()['html']
    code = re.findall(r"<p>(.*?)</p>", html_str)
    image_base64 = re.findall(r"base64,(.*?)\" alt=\"\">", html_str)[0]
    image_data = base64.b64decode(image_base64)  # 解码
    image_np = np.frombuffer(image_data, dtype=np.uint8)  # 转为numpy
    image = cv2.imdecode(image_np, cv2.COLOR_RGB2BGR)  # 转为cv2
    cv2.imwrite("./verify.jpg", image)
    return code


def get_captcha_result(images):
    url = "http://api.jfbym.com/api/YmServer/customApi"
    headers = {
        "Content-Type": "application/json",
    }
    params = {
        "token": "NUNCYkCrIPH7g6E760ZgVF2jJslb5jxfVXBGUmMvBAg",
        "type": "10114"
    }
    result = []
    for image in images:
        image = cv2.imencode(".jpg", image)[1]
        image_code = base64.b64encode(image).decode("utf-8")
        params["image"] = image_code
        response = requests.post(url, data=json.dumps(params), headers=headers).json()
        if response['code'] != 10000:
            continue
        if response["data"]["data"] is not None:
            result.append(response["data"]["data"])
    return result

def get_page(page_num, index_list, session):
    url = 'http://match.yuanrenxue.com/api/match/8'
    coordinate_dict = {
        1: 126,
        2: 136,
        3: 146,
        4: 426,
        5: 466,
        6: 477,
        7: 726,
        8: 737,
        9: 776
    }
    answer = '|'.join([str(coordinate_dict[__ + 1]) for __ in index_list]) + '|'
    params = {
        'page': page_num,
        # 'answer': '757|476|155|137|
        'answer': answer
    }
    response = session.get(url=url, params=params)
    print(response.text)


if __name__ == '__main__':
    session = requests.session()
    session.headers = {
        'Host': 'match.yuanrenxue.com',
        'Referer': 'http://match.yuanrenxue.com/match/8',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.183Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    words = get_verify(session)
    verify = Verify_code()
    verify_code = verify.process_captcha_picture()
    codes = get_captcha_result(verify_code)
    radical = Radical(RunOption.Radical)
    radical_codes = [radical.trans_ch(ele) for ele in codes]
    radical_words = [radical.trans_ch(ele) for ele in words]
    res = {}
    for i, word in enumerate(radical_words):
        if word in radical_codes:
            res[word] = i
    print(res)
