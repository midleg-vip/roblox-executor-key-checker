import requests
import time

def register_account(email, password, username, invite):
    response = requests.post(
        "https://api.volt.bz/auth/register",
        headers={
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "api.volt.bz",
            "Origin": "https://volt.bz",
            "Referer": "https://volt.bz/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0"
        },
        json={
            "email": email,
            "invite": invite,
            "password": password,
            "username": username
        }
    )
    return response.status_code, response.text
print("\nvolt.bz key checker/account creator with invite")

email = input("enter your email plz: ")
password = input("enter your password plz: ")
username = input("enter your username plz: ")
print("\nloading invite keys...")
with open("invites.txt") as f:
    invites = [line.strip() for line in f if line.strip()]
print(f"found {len(invites)} invite codes to check\n")
valid_count = 0
invalid_count = 0
for invite in invites:
    try:
        status, body = register_account(email, password, username, invite)
        if status == 400:
            print(f"invalid - {invite}")
            invalid_count += 1
        elif status in [200, 201]:
            print(f"valid - {invite} (account created)")
            valid_count += 1
            with open("valid_accounts.txt", "a") as f:
                f.write(f"invite Code: {invite}\n")
                f.write(f"email: {email}\n")
                f.write(f"username: {username}\n")
                f.write(f"password: {password}\n")
                f.write(f"response: {body}\n")
                f.write("-" * 40 + "\n\n")
        else:
            print(f"unknown status {status} - {invite}")
    except Exception as e:
        print(f"error checking {invite}")
    time.sleep(2)
print(f"results: {valid_count} valid, {invalid_count} invalid")
if valid_count > 0:
    print("valid accounts saved to valid_accounts.txt")
