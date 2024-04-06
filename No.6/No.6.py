import requests
import base64
from fontTools.ttLib import TTFont

#保存字体文件为No.6.ttf
def save_font(woff):
    with open("./No.6.ttf", "wb") as f:
        f.write(base64.b64decode(woff))

#将字体文件转换为xml文件并获取每个数字的flags，每次数字的flags不变
# def font_map():
#     font = TTFont("./No.6.ttf")
#     font.saveXML("./No.6.xml")
#     for val in font.getGlyphNames():
#         print(val)
#         res = font['glyf'][val].flags
#         print(res)
#         res = [i for i in res]
#         res = map(lambda x: str(x), res)
#         print("".join(res))

#将单个数字字体映射为具体的数字
def map_font(val: str):
    val = val.replace("&#x", "uni")
    font = TTFont("./No.6.ttf")
    font.saveXML("./No.6.xml")
    res = font['glyf'][val].flags
    res = [i for i in res]
    res = map(lambda x: str(x), res)
    return "".join(res)

# 获取每页的召唤师名字和rank_number，并返回rank_number最大的召唤师信息
def get_val(data, page):
    number_tags = {
        "10100100100101010010010010": 0,
        "1001101111": 1,
        "100110101001010101011110101000": 2,
        "10101100101000111100010101011010100101010100": 3,
        "111111111111111": 4,
        "1110101001001010110101010100101011111": 5,
        "10101010100001010111010101101010010101000": 6,
        "1111111": 7,
        "101010101101010001010101101010101010010010010101001000010": 8,
        "10010101001110101011010101010101000100100": 9
    }
    name = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你',
            '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀',
            '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城',
            '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度',
            '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨',
            '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦',
            '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风',
            '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次',
            '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵']
    yyq = 1
    img_num = 1
    img_num_arr = [1, 8, 3, 2, 4, 5, 7, 5, 15, 3, 9, 8, 5, 1, 3]
    level_arr = [1, 4, 3, 2, 9, 15]
    res = []
    for val in data:
        rank_number = val["value"].replace("/ /g", '').split()
        r = 0
        i = 3
        for rank in rank_number:
            rank_tag = map_font(rank)
            r += number_tags[rank_tag] * (10**i)
            i -= 1
        res.append({
            "name": name[yyq + (page - 1) * 10],
            "rank_number": r
        })
        yyq += 1
        img_num += 1
    res.sort(key=lambda x: x.get('rank_number'), reverse=True)
    return res[0]


if __name__ == "__main__":

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh,zh-CN;q=0.9",
        "referer": "https://match.yuanrenxue.cn/match/7",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                      "Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = {
        "qpfccr": "true",
        "no-alert3": "true",
        "tk": "-3880036669150664309",
        "sessionid": "prwz6maf3v22lm876nvrwbg5qh5zzwh1",
    }
    params = {}
    url = "https://match.yuanrenxue.cn/api/match/7"
    result = []
    for item in range(1, 6):
        params["page"] = item
        response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
        save_font(response["woff"])
        result.append(get_val(response["data"], item))
    # result.sort(key=lambda x: x.get("rank_number"), reverse=True)
    print(max(result, key=lambda x: x.get("rank_number")))
