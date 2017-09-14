import asyncio

async def mtier(num):
    for x in range(1,11):
        await asyncio.sleep(0)
        print('%s * %s = %s' % (x,num, x*num))

loop = asyncio.get_event_loop()

tasks = [
    asyncio.ensure_future(mtier(x))
    for x in range(1,10)
]

wt = asyncio.wait(tasks)
loop.run_until_complete(wt)
loop.close()
