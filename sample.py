await api.market_order(
            isin="US0378331005",
            exchange="LSX",
            order_type="buy",
            # limit=1000.0,
            size=1.0,
            expiry="gtd",
            expiry_date="2023-11-14",
            sell_fractions= False
        )


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