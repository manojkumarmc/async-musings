from aiohttp import web

async def index(request):
    return web.Response(text='Hello there...!!!')

async def index_param(request):
    name = request.match_info.get('name', 'Anonymous')
    return web.Response(text='Hello {0}'.format(name))


