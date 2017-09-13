import asyncio
import random

async def coro2(x):
    print('coro2: Starting operation on %s' % x)
    await asyncio.sleep(1)
    print('coro2: Completing operation on %s' % x)


async def coro1(x):
    print('coro1: Starting operation on %s' % x)
    await asyncio.sleep(1)
    await coro2(x)
    print('cor1: Completing operation on %s' % x)

async def coro(x):
    print('Starting operation on %s' % x)
    await asyncio.sleep(1)
    await coro1(x)
    print('Completing operation on %s' % x)

if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    if random.randint(1,10) % 2 == 0:
        tasks = [asyncio.ensure_future(coro(x))
                for x in range(1,11)]
        wait_tasks = asyncio.wait(tasks)
    else:
        wait_tasks = asyncio.gather(asyncio.ensure_future(coro(10)))
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
