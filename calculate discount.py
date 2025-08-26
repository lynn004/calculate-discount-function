def calculate_discount(price, discount_percent):
    # check if discount is 20 or more
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # if discount is less than 20, no discount applied
        return price


# ask the user for the price and discount
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# call the function
final_price = calculate_discount(price, discount_percent)

# print the result
print("The final price is:", final_price)
