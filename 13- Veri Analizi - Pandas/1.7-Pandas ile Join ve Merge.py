import pandas as pd

customers = {
    "CustomerId" : [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName": ["Yılmaz", "Korkmaz","Çelik","Toprak"]
}

orders = {
    "OrderId": [10,11,12,13],
    "CustomerId": [1,2,5,7],
    'OrderDate': ["2010-08-04","2010-07-04","2010-07-07","2012-07-05"]
}

dfCustomers = pd.DataFrame(customers, columns=["CustomerId", "FirstName","LastName"])
dfOrders = pd.DataFrame(orders, columns=["OrderId","CustomerId","OrderDate"])

# print(dfCustomers)
# print(dfOrders)

# result = pd.merge(dfCustomers, dfOrders, how="inner")
# result = pd.merge(dfCustomers, dfOrders, how="left")                # müşteri listesi gelir, customerId tutmayan müşterilerin
                                                                    # ürünleri NaN olur

result = pd.concat([dfOrders, dfCustomers], axis=1)     # concat ile tabloları alt alta ekleyebiliyoruz. axis ile de alt alta yada yan yana ekleriz

print(result)