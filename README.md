# Roblox Executor Key / Invite Checker

This repository contains two small Python utilities that check or use keys/invite codes against remote services.

Projects

- `seliware` — reads `keys.txt`, checks each key by POSTing the key to `https://seliware.com/checkkey`, and writes valid keys to `valid_keys.txt`.
- `volt` — reads `invites.txt`, attempts to register accounts using `https://api.volt.bz/auth/register` with each invite code, and appends successful account records to `valid_accounts.txt`.

What these scripts do (technical summary)

- `seliware/main.py`:
	- Sends an HTTP POST to `https://seliware.com/checkkey` with the raw key in the request body and a cookie named `key` set to the key.
	- Interprets a response body of `false` as an invalid key; any other non-empty response is treated as used/valid.
	- Sleeps 2 seconds between requests and saves valid keys to `valid_keys.txt`.

- `volt/main.py`:
	- Sends an HTTP POST with JSON payload to `https://api.volt.bz/auth/register` containing `email`, `password`, `username`, and `invite` fields.
	- Treats HTTP 400 as an invalid invite; HTTP 200/201 indicate a successful registration (a created account) and the script logs the account into `valid_accounts.txt`.
	- Sleeps 2 seconds between requests.

Required Python packages

- `requests` (install with `pip install requests`).

Quick setup

1. Ensure Python 3.8+ is installed and on your PATH.
2. Install dependencies:

```bash
pip install requests
```

Running the scripts

- Run `seliware` (from the repository root):

```bash
python -m seliware.main
# or
python seliware/main.py
```

- Run `volt` (from the repository root):

```bash
python -m volt.main
# or
python volt/main.py
```

Input files

- `seliware/keys.txt` — one key per line to check.
- `volt/invites.txt` — one invite code per line to try.

Output files

- `seliware/valid_keys.txt` — valid/used keys discovered by `seliware`.
- `volt/valid_accounts.txt` — appended account details for invites that successfully created accounts.

Security, ethics, and safety

- Inspect the source in `seliware/main.py` and `volt/main.py` before running.
- These scripts make automated requests to third-party services and attempt account creation; ensure you have explicit permission to test against those endpoints.
- Avoid exposing real credentials. `volt/main.py` prompts for email/password/username and will save those credentials to `valid_accounts.txt` if an account is created — treat that file as sensitive.

Notes about behavior

- Both scripts include a 2-second `time.sleep(2)` between requests to throttle activity.
- The scripts use simple heuristics (status codes and response text) to decide validity; they do not perform retries or robust error handling.

Extending this README

If you want, I can:

- Add sample `keys.txt`/`invites.txt` templates.
- Add command-line flags for concurrency, rate limits, or dry-run mode.
- Add a small GUI/terminal widget (Tkinter or textual) to run checks interactively.


