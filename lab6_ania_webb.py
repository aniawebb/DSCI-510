#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Item(object):
    stock_code = str()
    unit_price = float()
    
    def __init__(self, stock_code: str, unit_price: float) -> None:
        self.stock_code = stock_code
        self.unit_price = unit_price

    def __str__(self) -> str:
        return f'Item(stock_code={repr(self.stock_code)}, unit_price={"%.2f"%self.unit_price})'

    def __repr__(self) -> str:
        return f'Item(stock_code={repr(self.stock_code)}, unit_price={"%.2f"%self.unit_price})'


# In[2]:


class Customer(object):
    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        self.cart = dict()

    def add_to_cart(self, item: Item, quantity: int) -> None:
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity
            
    def remove_from_cart(self, item: Item, quantity: int) -> None:
        if item in self.cart:
            if quantity >= self.cart[item]:
                del self.cart[item] 
            else: 
                self.cart[item] -= quantity

    def cart_total(self) -> float:
        if len(list(self.cart.keys()))==1:
            item1_total = list(self.cart.values())[0] * list(self.cart.keys())[0].unit_price
            total = item1_total
        elif len(list(self.cart.keys()))==2:
            item1_total = list(self.cart.values())[0] * list(self.cart.keys())[0].unit_price
            item2_total = list(self.cart.values())[1] * list(self.cart.keys())[1].unit_price
            total = item1_total + item2_total
        elif len(list(self.cart.keys()))==3:
            item1_total = list(self.cart.values())[0] * list(self.cart.keys())[0].unit_price
            item2_total = list(self.cart.values())[1] * list(self.cart.keys())[1].unit_price
            item3_total = list(self.cart.values())[2] * list(self.cart.keys())[2].unit_price
            total = item1_total + item2_total + item3_total
        elif len(list(self.cart.keys()))==4:
            item1_total = list(self.cart.values())[0] * list(self.cart.keys())[0].unit_price
            item2_total = list(self.cart.values())[1] * list(self.cart.keys())[1].unit_price
            item3_total = list(self.cart.values())[2] * list(self.cart.keys())[2].unit_price
            item4_total = list(self.cart.values())[3] * list(self.cart.keys())[3].unit_price
            total = item1_total + item2_total + item3_total + item4_total
            
        return float(total)

    def __str__(self) -> str:
        return f'Customer(customer_id={repr(self.customer_id)}, cart_total={"%.2f"%self.cart_total()})'
    def __repr__(self) -> str:
        return f'Customer(customer_id={repr(self.customer_id)}, cart_total={"%.2f"%self.cart_total()})'
    


# In[3]:


class VIPCustomer(Customer):   
    def cart_total(self) -> float:
        if len(list(self.cart.keys()))==1:
            item1_total = list(self.cart.values())[0] * list(self.cart.keys())[0].unit_price
            total = item1_total
        elif len(list(self.cart.keys()))==2:
            item1_total = list(self.cart.values())[0] * list(self.cart.keys())[0].unit_price
            item2_total = list(self.cart.values())[1] * list(self.cart.keys())[1].unit_price
            total = item1_total + item2_total
        elif len(list(self.cart.keys()))==3:
            item1_total = list(self.cart.values())[0] * list(self.cart.keys())[0].unit_price
            item2_total = list(self.cart.values())[1] * list(self.cart.keys())[1].unit_price
            item3_total = list(self.cart.values())[2] * list(self.cart.keys())[2].unit_price
            total = item1_total + item2_total + item3_total
        elif len(list(self.cart.keys()))==4:
            item1_total = list(self.cart.values())[0] * list(self.cart.keys())[0].unit_price
            item2_total = list(self.cart.values())[1] * list(self.cart.keys())[1].unit_price
            item3_total = list(self.cart.values())[2] * list(self.cart.keys())[2].unit_price
            item4_total = list(self.cart.values())[3] * list(self.cart.keys())[3].unit_price
            total = item1_total + item2_total + item3_total + item4_total
            
        if total >= 50:
            benefit_total = total - (total*0.20)
            return float(benefit_total)
        else:
            return float(total) 
            
    def __str__(self) -> str:
        return f'VIPCustomer(customer_id={repr(self.customer_id)}, cart_total={"%.2f"%self.cart_total()})'
            


# In[4]:


# # Tesint Q1
# item1 = Item("milk", 10.5)
# item2 = Item("egg", 1.25)
# print(item1)
# print(item2)

# # Tesint Q2
# customer1 = Customer("Bob")
# customer1.add_to_cart(item1, 10)
# customer1.add_to_cart(item2, 5)
# item1.unit_price += 1.5
# customer1.remove_from_cart(item1, 2)
# print(customer1.cart_total())
# print(customer1)

# # Tesint Q3
# customer2 = VIPCustomer("John")
# customer2.add_to_cart(item1, 10)
# customer2.add_to_cart(item2, 5)
# customer2.remove_from_cart(item1, 1)
# customer2.add_to_cart(item2, 1)
# item2.unit_price += 0.5
# print(customer2.cart_total())
# print(customer2)


# In[ ]:




