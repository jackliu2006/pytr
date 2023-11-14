
from pytr.account import login
import asyncio


phoneNo = "+491602314407"
api = login(phone_no=phoneNo,pin="0816")




async def order_loop():
        recv = 0

        # await api.limit_order(
        #     isin="US0378331005",
        #     exchange="LSX",
        #     order_type="buy",
        #     limit=1.0,
        #     size=1.0,
        #     expiry="gtd",
        #     expiry_date="2023-11-14",
        #     # sell_fractions= False
        # )
        # recv += 1
        

        await api.cancel_order( '35e14c34-dd56-4445-ab75-86037b8cf84d')
        recv += 1

        await api.order_overview()
       
        recv += 1

        while recv > 0:
            subscription_id, subscription, response = await api.recv()
            print(subscription)
            print(response)
            recv -= 1

            await api.unsubscribe(subscription_id)


       
asyncio.get_event_loop().run_until_complete(order_loop())