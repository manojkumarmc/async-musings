import asyncio
from concurrent.futures import ProcessPoolExecutor

def blocker(x):
    from time import sleep
    sleep(x)
    print('slept for {0} seconds'.format(x))


async def main(exctr):
    loop = asyncio.get_event_loop()
    bt = [
        loop.run_in_executor(exctr, blocker, 5)
    ]
    c, p = await asyncio.wait(bt)
    rs = [t.result() for t in c]
    print(rs)

loop = asyncio.get_event_loop()
exctr = ProcessPoolExecutor(max_workers=3)
# task = [asyncio.ensure_future(main(exctr))]
# wt = asyncio.wait(task)
loop.run_until_complete(
    asyncio.ensure_future(main(exctr))
)
loop.close()


