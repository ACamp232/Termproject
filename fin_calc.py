
import urllib.request
import math

# 1. Takes the users’ monthly income and expenses based on input and calculates the surplus. 
#2. Finds the amount needed to save monthly based on cost of item (might split into separate functions)
#3. *Potential* use API to input taxes or costs of item




def surplus_calc():
    """Takes the users’ monthly income and expenses to give the surplus
    inc: monthly income of user
    exp: monthly expenses of user 
    surp: is the output"""
    # print ("Please input your monthly income:")
    inc = int(input())
    # print ("Please input the sum of your monthly expenses:")
    exp = int(input())
    surp = inc - exp
    # print("Your monthly surplus is: $", surp)
    
    

def mon_savings(product_name,product_price):
    """ based on user input calculates the
    number of months that it will take for the user to have enough money to purchase the product"
    mon_calc: is the output"""
    # print("What product are you looking to buy?")
    product_name = input()
    print (product_name)
    # print ("What is the price of the product?")
    product_price = int(input())
    surp = int(input())
    mon_calc = math.ceil(product_price/surp)
    return mon_calc
    # print('In', mon_calc, 'months you can buy a', product_name)
    


def main():
    surplus_calc(500,200)
   



# if __name__=="__main__":
#     main()