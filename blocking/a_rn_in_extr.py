import asyncio
from concurrent.futures import ProcessPoolExecutor

def blocker():
    from time import sleep
    sleep(3)
    print('slept for 3 seconds')


async def main(loop, exctr):
    loop.run_in_executor(exctr, blocker, None)

loop = asyncio.get_event_loop()
exctr = ProcessPoolExecutor(3)
loop.set_default_executor(exctr)
task = [asyncio.ensure_future(main(loop, exctr))]
wt = asyncio.wait(task)
loop.run_until_complete(wt)
exctr.shutdown(wait=True)
loop.close()


