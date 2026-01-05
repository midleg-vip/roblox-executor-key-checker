import requests
import time

def check_key(key):
    response = requests.post(
        "https://seliware.com/checkkey",
        headers={
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": str(len(key)),
            "Content-Type": "text/plain",
            "Cookie": f"key={key}",
            "Host": "seliware.com",
            "Origin": "https://seliware.com",
            "Referer": "https://seliware.com/",
            "sec-ch-ua": '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
        },
        data=key
    )
    return response.text.strip()
with open("keys.txt") as f:
    keys = [line.strip() for line in f if line.strip()]
valid_keys = []
invalid_keys = []
print("seliware key checker")
for key in keys:
    try:
        response = check_key(key)
        if response == "false":
            print(f"invalid - {key}")
            invalid_keys.append(key)
        else:
            print(f"used/valid - {key}")
            valid_keys.append(key)
            
    except Exception as e:
        print(f"error → {key}")
    time.sleep(2)
print(f"valid: {len(valid_keys)} | invalid: {len(invalid_keys)}")
if valid_keys:
    with open("valid_keys.txt", "w") as f:
        f.write("\n".join(valid_keys))
    print("valid keys saved to valid_keys.txt")
