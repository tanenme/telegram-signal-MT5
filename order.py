import MetaTrader5 as mt5
import time

mt5.initialize()
mt5.login(login=69658637, password='Toor2002**')
account_info = mt5.account_info()
print(f"Balance: {account_info.balance}")
print(f"Equity: {account_info.equity}")

def order(data):
    symbol = "XAUEUR"

    if data['type'] == 'buy':
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": 0.01,
            "type": mt5.ORDER_TYPE_BUY,
            "price": mt5.symbol_info_tick(symbol).ask,
            "comment": 'Python Script Buy',
            "type_filling": mt5.ORDER_FILLING_IOC,
            "type_time": mt5.ORDER_TIME_GTC
        }
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": 0.01,
            "type": mt5.ORDER_TYPE_SELL,
            "price": mt5.symbol_info_tick(symbol).ask,
            "comment": 'Python Script Buy',
            "type_filling": mt5.ORDER_FILLING_IOC,
            "type_time": mt5.ORDER_TIME_GTC
        }

    order = mt5.order_send(request)

    while order.comment in ['No prices', 'Requote']:
        time.sleep(1)
        order = mt5.order_send(request)
        print(order.comment)

    print(order.comment)

    mt5.shutdown()

def handle(string):
    keywords = ["sell", "buy", "sl", "tp1", "tp2"]
    data = {'order': False}

    for keyword in keywords:
        if keyword in string.lower():
            data['order'] = True

            if keyword == 'sell':
                data['type'] = 'sell'
            elif keyword == 'buy':
                data['type'] = 'buy'
            elif keyword == 'sl':
                sl_index = string.lower().find(keyword)
                sl_value = string[sl_index + len(keyword):].split()[0]
                data['sl'] = float(sl_value)
            elif keyword == 'tp1':
                tp1_index = string.lower().find(keyword)
                tp1_value = string[tp1_index + len(keyword):].split()[0]
                data['tp'] = float(tp1_value)

    print(data)
    order(data)


string = "Gold BUY Now 2083 - 2086\n\nsl 2089\n\ntp1 2080\ntp2 2075\n\njga mm guys test market"
handle(string)  # Output: order: true, type: 'sell'
