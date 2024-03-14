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
        data['symbol'] = 'XAUUSD.iux'
        for keyword3 in keywords3:
            if keyword3 in string.lower():
                if keyword3 == 'audjpy':
                    data['symbol'] = 'AUDJPY.iux'
                elif keyword3 == 'audusd':
                    data['symbol'] = 'AUDUSD.iux'
                elif keyword3 == 'eurgbp':
                    data['symbol'] = 'EURGBP.iux'
                elif keyword3 == 'eurjpy':
                    data['symbol'] = 'EURJPY.iux'
                elif keyword3 == 'eurusd':
                    data['symbol'] = 'EURUSD.iux'              
                elif keyword3 == 'gbpjpy':
                    data['symbol'] = 'GBPJPY.iux'  
                elif keyword3 == 'gbpusd':
                    data['symbol'] = 'GBPUSD.iux' 
                elif keyword3 == 'nzdjpy':
                    data['symbol'] = 'NZDJPY.iux'  
                elif keyword3 == 'nzdusd':
                    data['symbol'] = 'NZDUSD.iux'  
                elif keyword3 == 'usdcad':
                    data['symbol'] = 'USDCAD.iux' 
    
    print("ORDER:", simple_colors.blue(data['order']))

string1 = "gbpjpy Sell Now 2083 - 2086\n\nsl 2089\n\ntp1 2080\ntp2 2075\n\njga mm guys test market"
handle(string1)  # Output: order: true, type: 'sell'

string2 = "NZDUSD buy Now 2083 - 2086\n\nsl 2089\n\ntp1 2080\ntp2 2075\n\njga mm guys test market"
handle(string2)  # Output: order: true, type: 'sell'

string3 = "BUY"
handle(string3)  # Output: order: false, type: 'none'

string4 = "noptt "
handle(string4)  # Output: order: false, type: 'none'