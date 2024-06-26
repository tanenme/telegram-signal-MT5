from pyrogram import Client
import MetaTrader5 as mt5
import time
import simple_colors

app = Client("my_account")

def order(data):
    symbol = data['symbol']
    sl = data['sl']
    tp = data['tp']

    if data['type'] == 'buy':
        mt5.initialize()
        mt5.login(login=311089796, password='Callista57!')
        point = mt5.symbol_info(symbol).point
        symbol_info = mt5.symbol_info(symbol)
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": 0.01,
            "type": mt5.ORDER_TYPE_BUY,
            "price": symbol_info.ask,
            "comment": 'Python Script Buy',
            "type_filling": mt5.ORDER_FILLING_IOC,
            "type_time": mt5.ORDER_TIME_GTC
        }
        order = mt5.order_send(request)
        mt5.shutdown()

    elif data['type'] == 'sell':
        mt5.initialize()
        mt5.login(login=311089796, password='Callista57!')
        point = mt5.symbol_info(symbol).point
        symbol_info = mt5.symbol_info(symbol)
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": 0.01,
            "type": mt5.ORDER_TYPE_SELL,
            "price": symbol_info.ask,
            "sl": sl,
            "tp": tp,
            "comment": 'Python Script Buy',
            "type_filling": mt5.ORDER_FILLING_IOC,
            "type_time": mt5.ORDER_TIME_GTC
        }
        order = mt5.order_send(request)
        mt5.shutdown()
    return order

def handle(string):
    keywords = ["sell", "buy"]
    keywords2 = ['sl', 'tp1', 'tp2']
    keywords3 = ['xauusd', 'gbpjpy', 'audjpy', 'audusd', 'eurgbp', 'eurjpy', 'eurusd', 'gbpusd', 'nzdjpy', 'nzdusd', 'usdcad']
    data = {'order': False}
    for keyword in keywords:
        if keyword in string.lower():
            data['order'] = True
            if keyword == 'sell':
                data['type'] = 'sell'
            elif keyword == 'buy':
                data['type'] = 'buy'
            for keyword2 in keywords2:
                if keyword2 in string.lower():
                    if keyword2 == 'sl':
                        sl_index = string.lower().find(keyword2)
                        sl_value = string[sl_index + len(keyword2):].split()[0]
                        data['sl'] = float(sl_value)+0.00
                    elif keyword2 == 'tp1':
                        tp1_index = string.lower().find(keyword2)
                        tp1_value = string[tp1_index + len(keyword2):].split()[0]
                        data['tp'] = float(tp1_value)+0.00
                    elif keyword2 == 'tp2':
                        tp2_index = string.lower().find(keyword2)
                        tp2_value = string[tp2_index + len(keyword2):].split()[0]
                        data['tp2'] = float(tp2_value)+0.00
            data['symbol'] = 'GOLD'
            for keyword3 in keywords3:
                if keyword3 in string.lower():
                    if keyword3 == 'audjpy':
                        data['symbol'] = 'AUDJPY'
                    elif keyword3 == 'audusd':
                        data['symbol'] = 'AUDUSD'
                    elif keyword3 == 'eurgbp':
                        data['symbol'] = 'EURGBP'
                    elif keyword3 == 'eurjpy':
                        data['symbol'] = 'EURJPY'
                    elif keyword3 == 'eurusd':
                        data['symbol'] = 'EURUSD'              
                    elif keyword3 == 'gbpjpy':
                        data['symbol'] = 'GBPJPY'  
                    elif keyword3 == 'gbpusd':
                        data['symbol'] = 'GBPUSD' 
                    elif keyword3 == 'nzdjpy':
                        data['symbol'] = 'NZDJPY'  
                    elif keyword3 == 'nzdusd':
                        data['symbol'] = 'NZDUSD'  
                    elif keyword3 == 'usdcad':
                        data['symbol'] = 'USDCAD'
    return data

@app.on_message()
async def my_handler(client, message):
    if message.chat.username == "SoodLayer2024":
        if message.text:
            print("MESSAGE :", simple_colors.red(message.text))
            pesan = message.text
            handleMessage = handle(pesan)
            if handleMessage['order'] == True:
                print("ORDER:", simple_colors.blue(handleMessage['order']))
                orderHandle = order(handleMessage)
                print("ORDER RESULT: ", simple_colors.green(orderHandle))
                await app.send_message("me", orderHandle)
            print("")

app.run()
