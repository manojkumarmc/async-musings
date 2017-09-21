import asyncio
import yaml


def get_yaml(yaml_file):
    result = {}
    try:
        with open(yaml_file) as f:
            result = yaml.load(f)
    except IOError:
        pass
    return result


async def main(loop):
    fr = loop.call_soon(get_yaml('test.yml'))
    await asyncio.sleep(0)

loop = asyncio.get_event_loop()
fr = loop.call_soon(get_yaml('test.yml'))
print(fr)

# task = [asyncio.ensure_future(
#     main(loop)
# )]
# wt = asyncio.wait(task)
# loop.run_until_complete(wt)
# loop.close()

