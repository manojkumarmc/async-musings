import asyncio
import aiohttp
import async_timeout
import pprint
from datetime import datetime

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            pprint.pprint(await response.text())


async def main():
    conn = aiohttp.TCPConnector(verify_ssl=False)
    url = 'http://localhost:8888/'
    async with aiohttp.ClientSession(connector=conn) as session:
        wt = asyncio.wait([asyncio.ensure_future(fetch(session, url + str(x)))
                     for x in range(1,10001)
                     ])
        return await wt

loop = asyncio.get_event_loop()
start = datetime.now()
loop.run_until_complete(main())
end = datetime.now()
print(f'Start :{start}')
print(f'End   :{end}')
