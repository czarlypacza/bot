# 111799
# 111800
# import pyautogui
# import time

# # Move and click the input box
# pyautogui.moveTo(2000, 650)  # Update coordinates as needed


# n = 0
# while n <= 888889:
#     # Click the input box
#     pyautogui.click()
#     # Type the 6-digit code
#     pyautogui.typewrite(str(111780 + n))
#     # Press enter
#     pyautogui.press("enter")
#     # Wait for a short period to avoid overwhelming the system
#     print("checked "+ str(111780 + n))
#     n += 1
#     time.sleep(0.1)


import json
import itertools

with open("skins.json", "r") as f:
    data = json.load(f)

filtered_skins = []
for s in data["skinList"]:
    if s.get("minFloat", 0) <= 0.26 <= s.get("maxFloat", 1):
        filtered_skins.append({
            "name": s["name"],
            "collectionId": s["collection"]["idc"],
            "price": s.get("price", 0.0)
        })

tradeups = []
for combo in itertools.combinations(filtered_skins, 10):
    tradeups.append({"skins": list(combo)})

result = {"tradeUps": tradeups}

print(f"Generated {len(result['tradeUps'])} trade-ups.")

# with open("tradeups.json", "w") as out_f:
#     json.dump(result, out_f, indent=4)

import json
import time

# with open("tradeups.json", "r") as f:
#     result = json.load(f)

# After generating the tradeUps, we can calculate contract probabilities.
import requests
from collections import Counter

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

tradeup_calculations = []

seen_supports = {}

for t in result["tradeUps"]:
    collections = sorted(set(s["collectionId"] for s in t["skins"]))
    support_str = "-".join(str(cid) for cid in collections)

    if support_str not in seen_supports:
        print(f"Requesting endpoint for collections: {support_str}")
        resp = requests.get(
            f"https://api.tradeupspy.com/api/skins/outcomes?stattrak=false&inputrarity=5&collection={support_str}",
            headers=headers
        )
        if resp.status_code == 200:
            seen_supports[support_str] = resp.json()
        else:
            print(f"Endpoint failed with status {resp.status_code} for {support_str}")
            continue

    out_data = seen_supports[support_str]
    #time.sleep(1)  # Rate limit

    input_collections_count = Counter(s["collectionId"] for s in t["skins"])
    out_skins = out_data
    output_collections_count = Counter(s["collection"]["idc"] for s in out_skins)

    calculation = []
    for skin_out in out_skins:
        c_id = skin_out["collection"]["idc"]
        if c_id in input_collections_count and c_id in output_collections_count:
            prob = (input_collections_count[c_id] / 10) * (1 / output_collections_count[c_id])
            calculation.append({
                "name": skin_out["name"],
                "collectionId": c_id,
                "probability": prob
            })

    tradeup_calculations.append({
        "tradeUp": t["skins"],
        "outputs": calculation
    })

# Optionally, save results
with open("tradeup_calculations.json", "w") as outf:
    json.dump(tradeup_calculations, outf, indent=4)

# ...existing code...