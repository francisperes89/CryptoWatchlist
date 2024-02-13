from binance.client import Client

# Substitua 'sua_chave_publica' e 'sua_chave_secreta' pelas suas chaves da Binance
api_key = 'DLyNtolzkdAO4kdlMOcz0UdKvyCTSRDLPIYovEW4cVWjSuIJl6OVlXJXqAIGyN0x'
api_secret = 'q6iMbt9qCFfd2ONvVYUkn78O6nWzKFSDGs2u6O2I36oYnVxaYsLD2OSOeuxiSEYJ'

# Crie uma instância do cliente Binance
client = Client(api_key, api_secret)

# Obtenha informações da conta
account_info = client.get_account()

# Agora você pode processar as informações para obter as posições, cotações, etc.
for asset in account_info['balances']:
    symbol = asset['asset']
    free_quantity = float(asset['free'])
    locked_quantity = float(asset['locked'])

    # Faça o que precisar com essas informações, como imprimir ou armazenar em uma tabela.
    print(f"Moeda: {symbol}, Quantidade Disponível: {free_quantity}, Quantidade Bloqueada: {locked_quantity}")
