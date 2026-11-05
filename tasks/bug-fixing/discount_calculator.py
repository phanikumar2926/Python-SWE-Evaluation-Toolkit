def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
        price: Original product price.
        discount_percent: Discount percentage.

    Returns:
        Final price after discount.
    """
    discount = price * discount_percent
    return price - discount