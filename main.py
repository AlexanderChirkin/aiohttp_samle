from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/abc')
async def abc_handler(request: web.Request) -> web.Response:
    print('handle abc')
    return web.Response(text='abc response')

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8080)


