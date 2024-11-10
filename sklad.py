class Order:
    def __init__(self, type, item, price):
        self.type = type  
        self.item = item  
        self.price = price

class Deal:
    def __init__(self, sell_index, prev_index):
        self.sell_index = sell_index
        self.prev_index = prev_index  

# Read input from standard input
order_count = int(input())
orders = []

for _ in range(order_count):
    data = input().strip().split()  # Read and split input line like "N 1 5"
    type = data[0]  # 'N' or 'P'
    item = int(data[1])  # item number
    price = int(data[2])  # price
    orders.append(Order(type, item, price))

profits = []
previous = []

def find_compatible(o_index):
    helper_prof = profits.copy()
    while helper_prof:
        best_profit = max(helper_prof)
        bp_index = profits.index(best_profit)
        best_deal = previous[bp_index]
        if o_index > best_deal.sell_index:
            return bp_index
        else:
            helper_prof.remove(best_profit)
    return None

for sell_index in range(order_count):
    if orders[sell_index].type == 'P':
        for buy_index in range(sell_index):        
            if orders[buy_index].type == 'N' and orders[buy_index].item == orders[sell_index].item:
                profit = orders[sell_index].price - orders[buy_index].price
                previous_best_deal = find_compatible(buy_index)
                if previous_best_deal is not None:
                    previous.append(Deal(sell_index, previous_best_deal))
                    profits.append(profit + profits[previous_best_deal])
                else:
                    previous.append(Deal(sell_index, None))
                    profits.append(profit)
    
if profits:
    print(max(profits))
else:
    print(0)
