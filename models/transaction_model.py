#!/usr/bin/python

class Transaction:
    user = None
    trans_date  = None
    stock = None
    price = None
    sold = None
    order_id = None
    profit = None
    
    def __init__(self, user, trans_date, stock, price, sold, order_id, profit):
        self.user = user
        self.trans_date  = trans_date
        self.stock = stock
        self.price = price
        self.sold = sold
        self.order_id = order_id
        self.profit = profit
        
    def get_user(self):
        return self.user

    def set_user(self,x):
        self.user = x
    
    def get_trans_date(self):
        return self.trans_date
        
    def set_trans_date(self,x):
        self.trans_date = x

    def get_stock(self):
        return self.stock
        
    def set_stock(self,x):
        self.stock = x

    def get_price(self):
        return self.price
        
    def set_price(self,x):
        self.price = x

    def get_sold(self):
        return self.sold
        
    def set_sold(self,x):
        self.sold = x

    def get_order_id(self):
        return self.order_id
        
    def set_order_id(self,x):
        self.order_id = x

    def get_profit(self):
        return self.profit
        
    def set_profit(self,x):
        self.profit = x
