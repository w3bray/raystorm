# raystorm.py - Simple Raystorm in Python

## What is Raystorm?

Raystorm is a low-bandwidth HTTP stress testing tool.
It works like this:

1. It starts making lots of HTTP requests.
2. It sends headers periodically (every ~15 seconds) to keep connections open.
3. It never closes the connection unless the server does so.
4. If the server closes a connection, Raystorm creates a new one and continues.

This can exhaust a server’s available connection/thread pool and prevent it from responding to legitimate users.

## Credits

Made by:

w3bray

Repo: w3bray/raystorm


---

## Installation

Clone the repository:

git clone https://github.com/w3bray/raystorm.git

cd raystorm

Install dependencies:

apt update && apt install python3-socks

Install locally:

pip install .


---

## Usage

Run:

raystorm example.com

Or directly with Python:

python3 raystorm.py example.com


---

## Proxy Support

To use a SOCKS5 proxy:

raystorm example.com -x

Custom proxy:

raystorm example.com -x --proxy-host 127.0.0.1 --proxy-port 8080


---

## Configuration Options

Run:

raystorm -h

Available options:

-p, --port → Target port

-s, --sockets → Number of sockets

-v, --verbose → Verbose logging

-ua, --randuseragents → Random user agents

-x, --useproxy → SOCKS5 proxy support

--https → Use HTTPS

--sleeptime → Time between headers



---

## License

This project is licensed under the MIT License.
