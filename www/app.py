import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='utf-8')


async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    runner = web.AppRunner(app)
    # app.make_handler()这个方法用不了，改用APPrunner,虽然我没看懂，但是官方替换是这样得
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8000)  #当用8000接口，显示错误：OSError: [Errno 10048] error while attempting to bind on address ('127.0.0.1', 8000): 通常每个套接字地址(协议/网络地址/ 端口)只允许使用一次。那么换成8001或8002，这样一般就可以了
    await site.start()
    logging.info('server started at http://127.0.0.1:8000...')
    return site

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()