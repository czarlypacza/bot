import requests
import json

data = {
    "skinList": []
}


for i in range(1, 3):
    url = f"https://api.tradeupspy.com/api/skins/search/{i}?stattrak=false&rarity=5&condition=ft&collection=-1&skinname=%20&filter=0"
    headers = {
        "Host": "api.tradeupspy.com",
        "Sec-Ch-Ua-Platform": "Windows",
        "Accept-Language": "pl-PL,pl;q=0.9",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"99\", \"Chromium\";v=\"136\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://www.tradeupspy.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.tradeupspy.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)
    for skin in response.json()["skinList"]:
        data["skinList"].append(skin)

open("skins2.json", "w").write(json.dumps(data, indent=4))

