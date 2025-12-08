import os

from py_clob_client.client import ClobClient
from py_clob_client.clob_types import ApiCreds, MarketOrderArgs, OrderType
from dotenv import load_dotenv
from py_clob_client.constants import AMOY
from py_clob_client.order_builder.constants import BUY




def main():
    host = os.getenv("CLOB_API_URL", "https://clob.polymarket.com")
    key = "0x644dec691ec2cabe992ee0c10d1249e391492c83d340e49a2ae82de94b97f262"
    creds = ApiCreds(
        api_key='0f2eedfb-aad7-79cb-d00c-62317f40e214',
        api_secret='qVGmZoLWoyr0LrcVpym-tDOV6YSLDtbNY--Lc7thp6Y=',
        api_passphrase='be65f4284dbaf1d81f0af3e0e2f2ab19f66d1f7e89325726d8bad694ec3174b2',
    )
    chain_id = 137
    client = ClobClient(host, key=key, chain_id=chain_id, creds=creds)

    # create a market buy order for the equivalent of 100 USDC at the market price
    order_args = MarketOrderArgs(
        token_id="43346999573571279084829705550951657228560122189852907354399832194708460277206",
        amount=5,  # $$$
        side=BUY,
    )
    signed_order = client.create_market_order(order_args)
    resp = client.post_order(signed_order, orderType=OrderType.FOK)
    print(resp)
    print("Done!")


main()