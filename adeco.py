import asyncio
from functools import wraps

def my_decorator(fn):
    @wraps(fn)
    async def wrapper(*args, **kwargs):
        print('Calling', fn.__name__)
        if asyncio.iscoroutinefunction(fn):
            return await fn(*args, **kwargs)
        else:
            return fn(*args, **kwargs)
    return wrapper

def something(fn):
    if asyncio.iscoroutinefunction(fn):
        print('it is')

@my_decorator
async def coro():
    await asyncio.sleep(0)
    print('in coro')

def main():
    ioloop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(coro())]
    wt = asyncio.wait(tasks)
    ioloop.run_until_complete(wt)
    ioloop.close()

if __name__ == "__main__":
    main()
