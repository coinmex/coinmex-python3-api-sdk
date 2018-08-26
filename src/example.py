# coding=utf-8
import spot as s

if __name__ == '__main__':

	# input your personal api info
    api_key = ''
    seceret_key = ''
    passphrase = ''

    # make a spot instance
    spot_instance = s.Spot(api_key, seceret_key, passphrase, True)

	# spot function

    # query account
    # example = spot_instance.get_account()

    # query ledger
    # example = spot_instance.get_ledger('ct', before='', after='', limit='')

    # withdraw
    # example = spot_instance.withdraw('usdt', 100, '')

    # order
    example = spot_instance.order('limit', 'sell', 'ct_usdt', '1', '10', funds='')

    # revoke order by ID
    # example = spot_instance.revoke_order(19885212780592, 'ct_usdt')

    # revoke orders by code
    # example = spot_instance.revoke_orders('ct_usdt')

    # query order by ID
    # example = spot_instance.get_order_info(19885212780592, 'ct_usdt')
 
    # query orders by code
    # example = spot_instance.get_orders_info('open', 'ct_usdt', before='', after='', limit='')

    # query code
    # example = spot_instance.get_code()

    # query ticker
    # example = spot_instance.get_ticker('ct_usdt')

    # query depth
    # example = spot_instance.get_depth('ct_usdt')

    # query deal
    # example = spot_instance.get_deal('ct_usdt', before='', after='', limit='')

    # query k-line
    # example = spot_instance.get_kline('ct_usdt', '1min', 1534132800000, 1534150800000)

    # query server-time
    # example = spot_instance.get_time()

    print(example)









