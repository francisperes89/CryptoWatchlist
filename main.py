import requests
import os
import pandas as pd
import openpyxl

def get_watchlist_data(API_key, watchlist):
    API_domain = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_key
    }
    
    parameters = {
        'symbol': ','.join(watchlist),
        'convert':'USD'
    }

    response = requests.get(API_domain, headers=headers, params=parameters)
    data = response.json()
    coins_data = []
    for id, coin in data['data'].items():
        coin_data = {
            'Coin': coin['name'],
            'Price (USD)': coin['quote']['USD']['price'],
            '24h Change (%)': coin['quote']['USD']['percent_change_24h'],
            '7d Change (%)': coin['quote']['USD']['percent_change_7d'],
        }
        coins_data.append(coin_data)

    return coins_data




if __name__ == '__main__':
  
    API_key = os.environ['API_key']
  
    watchlist = ['BTC', 'ETH', 'XRP', 'SOL', 'AVAX', 'MATIC', 'IMX', 'ATOM', 'TAO', 'INJ', 'TIA', 'XLM', 'HBAR', 'ARB', 'SUI', 'SEI', 'BEAM', 'ALGO', 'HNT', 'PYTH', 'AKT', 'MANTA', 'FET', 'SUPER', 'ILV', 'PRIME', 'CTSI', 'FLUX', 'SFUND', 'AUCTION', 'BIGTIME', 'PYR', 'YGG', 'PAAL', 'MYRIA', 'PAID', 'SHRAP', 'SIDUS', 'ALU', 'CETUS', 'INSP', 'REEF', 'PNG', 'VPP', 'SAVM', 'XAVA', 'SEILOR', 'SUIP', 'TURBOS']
  
    coins_data = get_watchlist_data(API_key, watchlist)
  
    # Create a DataFrame from the data
    df = pd.DataFrame(coins_data)
  
    # Save the DataFrame to an Excel file
    excel_filename = 'coin_watchlist.xlsx'
    df.to_excel(excel_filename, index=False)
  
    print(f'Table saved to {excel_filename}')
    # print(coins_data)