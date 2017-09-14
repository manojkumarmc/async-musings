import asyncio


async def m1():
    print('Hello')
    await asyncio.sleep(3)
    print('World')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(m1())
         for x in range(10)]

wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()




