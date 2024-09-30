class Order:
    def __init__(self, type, item, price):
        self.type = type  
        self.item = item  
        self.price = price
class Deal:
    def __init__(self, sell_index, prev_index):
        self.sell_index = sell_index
        self.prev_index = prev_index  
        
        
tes_data = lines_of_text = [
6,
"N", 1, 5,
"P", 1, 10,
"N", 2, 1,
"N",3, 10,
"P", 2, 20,
"P", 3, 20
]

profits = []
previous = []
order_count = tes_data [0]
orders = []


for a in range(order_count):
    data = tes_data [1:]
    type = data[a*3]
    item = data[a*3 + 1]
    price = data[a*3 + 2]
    orders.append(Order(type,item,price))


def find_compatible(o_index):
    helper_prof = profits.copy()
    while helper_prof:
        best_profit = max(helper_prof) # muzou byt dva TODO
        bp_index = profits.index(best_profit)
        best_deal = previous[bp_index]
        # checks if the current buy index is higher then the best offer sell index
        if (o_index > best_deal.sell_index):
            return bp_index # returns index of the best deal which is compatible
        else:
            helper_prof.remove(best_profit)
    return None # in case nothing is compatible

for sell_index in range (order_count):
    if (orders[sell_index].type == 'P'):
        for buy_index in range(sell_index):        
            if (orders[buy_index].type == 'N' and orders[buy_index].item == orders[sell_index].item):
                profit = orders[sell_index].price - orders[buy_index].price
                previous_best_deal = find_compatible(buy_index)
                if previous_best_deal != None:
                    previous.append(Deal(sell_index, previous_best_deal))
                    profits.append(profit + profits[previous_best_deal])
                else:
                    previous.append(Deal(sell_index, None))
                    profits.append(profit)

print(max(profits))