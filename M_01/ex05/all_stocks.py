import sys


def all_stocks(company):
    ls_names = []
    for s in company.split(','):
        if not s.strip():
            return
        else:
            ls_names += [s.strip()]
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
    for i in ls_names:
        flag = 0
        for k, v in COMPANIES.items():
            if i.upper() == v:
                print(i.upper() + " is a ticker symbol for " + k)
                flag = 1
            elif i.upper() == k.upper():
                print(k + " stock price is " + str(STOCKS[v]))
                flag = 1
        if not flag:
            print(i + " is an unknown company or an unknown ticker symbol")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_stocks(sys.argv[1])
