import asyncio
import aiohttp
import async_timeout
import pprint


proxy_url = 'http://proxy.com:8080'

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url, proxy=proxy_url) as response:
            pprint.pprint(await response.text())


async def main():
    conn = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        wt = asyncio.wait([asyncio.ensure_future(fetch(session, url))
                     for url in ['http://python.org', 'https://api.github.com/events']
                     ])
        return await wt

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
