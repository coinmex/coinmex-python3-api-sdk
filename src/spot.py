from client import Client
from consts import *

class Spot(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time)

    # query account
    def get_account(self):
        return self._request_without_params(GET, SPOT_ACCOUNT)

    # query ledger
    def get_ledger(self, currencyCode, before='', after='', limit=''):
        params = {'before': before, 'after': after, 'limit': limit}
        return self._request_with_params(GET, SPOT_LEDGER + str(currencyCode) + '/ledger', params, cursor=True)

    # withdraw
    def withdraw(self, currencyCode, amount, address):
        params = {'currencyCode': currencyCode, 'amount': amount, 'address': address}
        return self._request_with_params(POST, WITHDRAW, params)

    # order
    def order(self, atype, side, code, size, price='', funds=''):
        params = {'type': atype, 'side': side, 'code': code, 'size': size, 'price': price, 'funds': funds}
        return self._request_with_params(POST, SPOT_ORDER, params)

    # revoke order by ID
    def revoke_order(self, orderId, code):
        params = {'code': code}
        return self._request_with_params(DELETE, SPOT_REVOKE_ORDER + str(orderId), params)

    # revoke orders by code
    def revoke_orders(self, code):
        params = {'code': code}
        return self._request_with_params(DELETE, SPOT_REVOKE_ORDERS, params)

    # query order by ID
    def get_order_info(self, orderId, code):
        params = {'code': code}
        return self._request_with_params(GET, SPOT_ORDER_INFO + str(orderId), params)

    # query orders by code
    def get_orders_info(self, status, code, before='', after='', limit=''):
        params = {'status': status, 'code': code, 'before': before, 'after': after, 'limit': limit}
        return self._request_with_params(GET, SPOT_ORDERS_INFO, params, cursor=True)

    # query code
    def get_code(self):
        return self._request_without_params(GET, SPOT_CODE)

    # query ticker
    def get_ticker(self, code):
        return self._request_without_params(GET, SPOT_TICKER + str(code) + '/ticker')

    # query depth
    def get_depth(self, code):
        return self._request_without_params(GET, SPOT_DEPTH + str(code) + '/orderbook')

    # query deal
    def get_deal(self, code, before='', after='', limit=''):
        params = {'before': before, 'after': after, 'limit': limit}
        return self._request_with_params(GET, SPOT_DEAL + str(code) + '/fills', params, cursor=True)

    # query k-line
    def get_kline(self, code, atype, start, end):
        params = {'type': atype, 'start': start, 'end': end}
        return self._request_with_params(GET, SPOT_KLINE + str(code) + '/candles', params)

    # query server-time
    def get_time(self):
        return self._request_without_params(GET, SERVER_TIMESTAMP)




