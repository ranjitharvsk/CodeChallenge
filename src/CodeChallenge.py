## function to get max profit from stock list
def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) == 0:
        return 0
    elif len(stock_prices_yesterday) == 1:
        return 0
    else:
        minStockPrice = min(stock_prices_yesterday)
        indexOfMinStock = stock_prices_yesterday.index(minStockPrice)

        newStockPricesList = stock_prices_yesterday[indexOfMinStock:]
        if len(newStockPricesList) > 0:
            maxStockPrice = max(newStockPricesList)
            if maxStockPrice > minStockPrice:
                print maxStockPrice - minStockPrice
                return maxStockPrice - minStockPrice
            else:
                return 0

import unittest

class TestCodeChallenge(unittest.TestCase):
    def test_get_max_profit(self):
        #list of one element
        stock_prices_yesterday = [1]
        self.assertEquals(get_max_profit(stock_prices_yesterday), 0)
        #list of same elements with same price
        stock_prices_yesterday = [1, 1]
        self.assertEquals(get_max_profit(stock_prices_yesterday), 0)
        #list of 0 elements
        stock_prices_yesterday = []
        self.assertEquals(get_max_profit(stock_prices_yesterday), 0)
        #list of elements from code challenge
        stock_prices_yesterday = [10, 7, 5, 8, 11, 9];
        self.assertEquals(get_max_profit(stock_prices_yesterday), 6)
        #list of 10 elements in asc order
        stock_prices_yesterday = [1,2,3,4,5,6,7,8,9,10];
        self.assertEquals(get_max_profit(stock_prices_yesterday), 9)
        #list of 10 elements in desc order - always loss
        stock_prices_yesterday.reverse()
        self.assertEquals(get_max_profit(stock_prices_yesterday), 0)

unittest.main()



