from aiohttp import web
import asyncio
import async_ORM.bd_handler
from Authorisation.auth_client import AuthRPC
from json_handler import jsoner
import sys
sys.path.append('../')



class Handler:

    auth_ = AuthRPC()

    # READY
    async def auth(self,request):
        try:
            data = await request.json()
            vk_id = data['vk_id']
            access_token = data['access_token']
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        token = self.auth_.register(user_id = vk_id, access_token = access_token)

        try: 
            await bd_handler.bd_handler.authorisation(vk_id=vk_id)
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        response = jsoner(status=200,token=token)
        return web.json_response(response)

    # TODO ELASTIC 
    async def my_wishlist(self,request):
        
        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        try: 
            result= await bd_handler.bd_handler.get_list_of_products(vk_id=vk_id)
        except:
            response = jsoner(status=400)
            return web.json_response(response)
        
        # TODO elasticsearch

        return web.Response(status=200,text=f"{vk_id}, {token == 'allowed'}")

    # TODO ELASTIC
    async def search(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
            search_querry = data['search'] 
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        return web.Response(status=200,text=f'OK')

    # READY
    async def adding_wish(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
            product_id = data['product'] 
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        try: 
            await bd_handler.bd_handler.add_wish_to_list(vk_id=vk_id, product_id=product_id)
        except:
            response = jsoner(status=400)
            return web.json_response(response)
            
        response = jsoner(status=200)
        return web.json_response(response)

    # TODO ELASTIC    
    async def friend_wishlist(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
            friend_id = data['friend_id'] 
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        try: 
            result= await bd_handler.bd_handler.get_list_of_products(vk_id=friend_id)
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        return web.Response(status=200,text=f'OK')

    # READY
    async def gift(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
            friend_id = data['friend_id']  
            product_id = data['product'] 
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        try: 
            await bd_handler.bd_handler.to_gift(my_id=vk_id,friend_id=friend_id,product_id=product_id)
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        response = jsoner(status=200)
        return web.json_response(response)

    # TODO ELASTIC 
    async def user_gftlist(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
            friend_id = data['friend_id']
            
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        try: 
            result= await bd_handler.bd_handler.watch_gift_list(my_id= vk_id,friend_id = friend_id)
        except:
            return web.Response(status=400,text='HTTP 400 Bad Request')
        return web.Response(status=200,text=f'OK')

    # TODO ELASTIC 
    async def giftlist(self, request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        try: 
            result= await bd_handler.bd_handler.watch_gift_list(my_id= vk_id,friend_id = None)
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        return web.Response(status=200,text=f'OK')

    # READY
    async def cancel_gift(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
            friend_id = data['friend_id']  
            product_id = data['product'] 
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        try: 
            await bd_handler.bd_handler.to_gift(my_id=None,friend_id=friend_id,product_id=product_id)
        except:
            response = jsoner(status=400)
            return web.json_response(response)
        
        response = jsoner(status=200)
        return web.json_response(response)

    # READY
    async def cansel_wish(self,request):

        try:
            data = await request.json()
            vk_id = data['vk_id']
            token = data['app_token']
            access_token = data['access_token']
            product_id = data['product'] 
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        if not self.auth_.authorize(user_id = vk_id, access_token = access_token,sign=token):
            response = jsoner(status=403)
            return web.json_response(response)

        try: 
            await bd_handler.bd_handler.delete_wish(my_id=vk_id,product_id=product_id)
        except:
            response = jsoner(status=400)
            return web.json_response(response)

        
        response = jsoner(status=200)
        return web.json_response(response)




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