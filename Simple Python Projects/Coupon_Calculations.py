'''
Program: Coupon_Calculation.py
Author: Patrick Foy
Last date modified: 01/28/2024

The purpose of this program is to take an order dollar amount deduct coupons for dollar and percent. Add shipping and output a total.

'''

#input order price conversion 
print("Please Enter order price")
price = input()
order_price = float(price)

#dollar off coupon conversion
print("Please Enter Dollar off coupon")
dollar = input()
dollar_coupon = float(dollar)


#Percentage off coupon conversion
print("Please Enter any Percentage off coupon")
percent = input()
percent_coupon = float(percent)

#coupon calculation with catches for 0
if dollar_coupon > 0 :
    dollar_subtotal = order_price - dollar_coupon
    print ("Total after dollar off coupons is: ${a:.2f}" .format(a=dollar_subtotal))
else:
    dollar_subtotal = order_price
    print ("Total after dollar off coupons is: ${a:.2f}" .format(a=dollar_subtotal))

if percent_coupon > 0 :
    coupon_subtotal = dollar_subtotal - (dollar_subtotal * (percent_coupon/100))  
    print ("Your total after percentage off coupons is: ${a:.2f}" .format(a=coupon_subtotal))
else:
    coupon_subtotal = dollar_subtotal
    print ("Your total after percentage off coupons is: ${a:.2f}" .format(a=coupon_subtotal))
    
#Order total after tax Calculation Declare Tax Constant
TAX = .06

order_subtotal = coupon_subtotal + (coupon_subtotal * TAX)

#Display order with tax and discounts
print ("Your order subtotal after tax is: ${a:.2f}".format (a=order_subtotal))


#Shipping Calculation
if order_subtotal > 0:
    if 0 < order_subtotal < 10:
        shipping_price = 5.95
        print( "Shipping is $5.95")
    elif 10 < order_subtotal < 30:
        shipping_price = 7.95
        print( "Shipping is $7.95")
    elif 30 < order_subtotal <  50:
        shipping_price = 11.95
        print( "Shipping is $11.95")
    elif order_subtotal > 50:
        shipping_price = 0
        print( "Shipping is free")

else:
    shipping_price = 100
    print( "Your order appears to be in the negative.")



#Add shipping final calculation
if shipping_price != 100:
    final_total = order_subtotal + shipping_price
    print ("Your final total with shipping is ${a:.2f}".format (a=final_total))
else:
    final_total = order_subtotal
    print ("Your final total reflects a store credit of ${a:.2f}".format (a=final_total))