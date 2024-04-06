import requests

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}
cookies = {
    "sessionid": "98m4ownu1kda60clcjdrfl015d76ttss",
    "RM4hZBv0dDon443M": "0r4DxBBxzWN0NVKr/RJlDL3UBOuH5O+2oVbeOvQX76QkFBExV2LtZQFKfJM48IvpWhcJP0rD8K2GMrEl7l3nx2VfnLFkSXr4oC4wpn6Mlt1TPLUz4uDhLmevIFKmdIa7NXSIu1BCAkU166FwK2gAPLiWmE2nO2qveks8k6solKxfkVV714JhDRWk1mLMVlvI9+GNhTkI9ZCXAje7VIakRd/l6jYVLqX+1fT2707LmQ8=",
}
url = "https://match.yuanrenxue.cn/api/match/5"
params = {
    "page": 1,
    "m": "1711893707215",
    "f": "1711893706000"
}
response = requests.get(url, headers=headers, params=params, cookies=cookies)

print(response.text)
print(response.url)
