from async_ORM.bd_handler import bd_handler
from ourAPI.ourAPI import Handler
from Authorisation.auth_client import AuthRPC
from aiohttp import web

async def ap():
    bd_handler.set_connection()
    app = web.Application()
    handler = Handler(BD = bd_handler(), Auth = AuthRPC())
    app.add_routes([web.post('/signin', handler.auth),
                    web.get('/mywishlist', handler.my_wishlist),
                    web.post('/mywishlist', handler.adding_wish),
                    web.delete('/mywishlist', handler.cansel_wish),
                    web.get('/friendwishlist', handler.friend_wishlist),
                    web.post('/friendwishlist',handler.gift),
                    web.delete('/friendwishlist',handler.cancel_gift),
                    web.get('/giftlist',handler.giftlist),
                    web.get('/search',handler.search)])

    web.run_app(app)