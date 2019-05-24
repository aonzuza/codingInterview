


# prices = [9,13,16,11,8,9,20]
#
#
# buy  = prices[0];
# should_sell = 0;
# should_buy = 0;
# max_profit = 0;
#
#
# for price in prices:
#
#     profit = price - buy;
#
#     if profit > max_profit:
#         max_profit = profit;
#         should_sell = price;
#         should_buy  = buy;
#     if  price < buy:
#         buy = price;
#
# print(should_buy)
# print(should_sell)




# solutions

prices = [9,13,16,11,8,9,20];

max_sell = 0;
min_buy  = 0;
max_profit = 0;
for price in reversed(prices):

    max_sell = max(max_sell,price);
    potential_profit = max_sell - price;
    max_profit =  max(max_profit,potential_profit);

print(max_profit);
