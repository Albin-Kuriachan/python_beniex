"""Write a Python function called calculate_discounted_price that takes the original price of an item and a discount
percentage as input. The function should return the discounted price after applying the discount. Ensure that
the function handles the case where the discount percentage is negative and raises a custom exception called
 InvalidDiscountError with an appropriate error message. """


class InvalidDiscountError(Exception):
    pass

def calculate_discounted_price(price, discount):
    try:
        if discount < 1:
            raise InvalidDiscountError("Invalid input! Discount percentage cannot be negative")

        discount_amount = price * (discount / 100)
        final_price = price - discount_amount
        print(f'Discount amount is {discount_amount} % and amount to pay is {final_price}')


    except InvalidDiscountError as e:
        print(e)


price = float(input('Enter the price :'))
discount = float(input('Enter the discount percent :'))

calculate_discounted_price(price, discount)
