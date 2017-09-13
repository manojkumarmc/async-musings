import asyncio


async def coro(x):
    print('Starting operation on %s' % x)
    await asyncio.sleep(2)
    print('Completing operation on %s' % x)


ioloop = asyncio.get_event_loop()
tasks = [coro(x)
         for x in range(1,11)]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()
