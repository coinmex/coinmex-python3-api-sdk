# API接口说明

---
## PRIVATE API
- 币币账户信息
```python
get_account(self)
```
- 币币账单流水
```python
get_ledger(self, currencyCode, before='', after='', limit='')
```
- 提币
```python
withdraw(self, currencyCode, amount, address)
```
- 下单
```python
order(self, atype, side, code, size, price='', funds='')
```
- 撤销指定订单
```python
revoke_order(self, orderId)
```
- 批量撤销订单
```python
revoke_orders(self, code)
```
- 获取指定订单
```python
get_order_info(self, orderId)
```
- 批量获取订单
```python
get_orders_info(self, code, status, before='', after='', limit='')
```

## PUBLIC API
- 获取币对信息
```python
get_code(self)
```
- 获取Ticker信息
```python
get_ticker(self, code)
```
- 获取深度数据
```python
get_depth(self, code)
```
- 获取成交数据
```python
get_deal(self, code, before='', after='', limit='')
```
- 获取K线数据
```python
get_kline(self, code, start, end, atype)
```
- 获取服务器时间
```python
get_time(self)
```

