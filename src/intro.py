def find_max(a, b):
    return a if a > b else b


def get_coupons():
    return [{"code": "SAVE20", "discount": 0.2}, {"code": "SAVE50", "discount": 0.5}]


def calculate_discount(code: str, price: int) -> float:
    if type(price) is not int or price <= 0:
        raise ValueError("Price must be a positive integer type")

    coupon = [coupon for coupon in get_coupons() if coupon["code"] == code]

    if not coupon:
        return price

    discount = coupon[0]["discount"]
    return price - discount * price
