from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/abc')
async def abc_handler(request: web.Request) -> web.Response:
    print('handle abc')
    return web.Response(text='abc response')


@routes.get('/v1/user')
async def user_handler(request: web.Request) -> web.Response:
    print(request.query.get('id'))
    raise web.HTTPUnauthorized(text='user unauthorized')
    return web.Response(text='response')


@routes.post('/v1/user')
async def user_handler_post(request: web.Request) -> web.Response:
    print(await request.json())
    return web.json_response({
        'id': 35,
        'name': 'alex',
        'info': {
            'a': None,
            'b': 0
        }
    })


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8080)


