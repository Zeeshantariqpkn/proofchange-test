"""Pricing rules for the test repository."""


def calculate_discount(price, customer_type):
    if customer_type == "premium":
        return price * 0.80

    return price