import coinmarketcapapi

import config

cmc = coinmarketcapapi.CoinMarketCapAPI(config.cmc_API_KEY)


def get_price(crypto: str) -> str:
    """Returns current btc price"""
    data_quote = cmc.cryptocurrency_quotes_latest(symbol=f"{crypto}", convert="USD")
    usd_metrics = data_quote.data[f"{crypto}"]["quote"]["USD"]
    return (
        f"{crypto} -> Price: ${usd_metrics['price']:.2f}\nChange (24h): {usd_metrics['percent_change_24h']:.2f}%"
        + f"\n#{crypto} #HardLuck #crypto"
    )


if __name__ == "__main__":
    print(get_price("BTC"))
