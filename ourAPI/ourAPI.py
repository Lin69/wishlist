from aiohttp import web
import asyncio



class Handler:

    async def auth(self,request):
        try:
            data = await request.json()
            vk_id = data['vk_id']
            # TODO auth data
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

    async def my_wishlist(self,request):
        
        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['access_token']
            # TODO auth data
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

        try: 
            # TODO query validation 
            pass
        except:
            return web.Response(status=403,text='HTTP 403 Forbidden')

        # TODO rest
        return web.Response(status=200,text=f"{vk_id}, {token == 'allowed'}")
    
    async def search(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['access_token']
            # TODO auth data
            search_querry = data['search'] 
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

        try: 
            # TODO query validation 
            pass
        except:
            return web.Response(status=403,text='HTTP 403 Forbidden')

        # TODO rest
        return web.Response(status=200,text=f'OK')

    async def adding_wish(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['access_token']
            # TODO auth data
            product_id = data['product'] 
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

        try: 
            # TODO query validation 
            pass
        except:
            return web.Response(status=403,text='HTTP 403 Forbidden')

        # TODO rest
        return web.Response(status=200,text=f'OK')

    async def friend_wishlist(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['access_token']
            # TODO auth data
            friend_id = data['friend_id'] 
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

        try: 
            # TODO query validation 
            pass
        except:
            return web.Response(status=403,text='HTTP 403 Forbidden')

        # TODO rest
        return web.Response(status=200,text=f'OK')

    async def gift(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['access_token']
            # TODO auth data
            friend_id = data['friend_id']  
            product_id = data['product'] 
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

        try: 
            # TODO query validation 
            pass
        except:
            return web.Response(status=403,text='HTTP 403 Forbidden')

        # TODO rest
        return web.Response(status=200,text=f'OK')

    async def giftlist(self, request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['access_token']
            # TODO auth data
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

        try: 
            # TODO query validation 
            pass
        except:
            return web.Response(status=403,text='HTTP 403 Forbidden')

        # TODO rest
        return web.Response(status=200,text=f'OK')

    async def cancel_gift(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['access_token']
            # TODO auth data
            friend_id = data['friend_id']  
            product_id = data['product'] 
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

        try: 
            # TODO query validation 
            pass
        except:
            return web.Response(status=403,text='HTTP 403 Forbidden')

        # TODO rest
        return web.Response(status=200,text=f'OK')

    async def cansel_wish(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['access_token']
            # TODO auth data
            product_id = data['product'] 
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')

        try: 
            # TODO query validation 
            pass
        except:
            return web.Response(status=403,text='HTTP 403 Forbidden')

        # TODO rest
        return web.Response(status=200,text=f'OK')


app = web.Application()
handler = Handler()
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