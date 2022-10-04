import sys


def ticker_symbol(company):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    for k, v in COMPANIES.items():
        if v == company.upper():
            return print(k, STOCKS[company.upper()])
    else:
        print("Unknown company")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ticker_symbol(sys.argv[1])
