class Paint:

    def __init__(self, buckets, color):  # Or get house area and height
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


class DiscountedPaint(Paint):
    def discounted_price(self, discount_percentage):
        price = self.total_price()
        discounted_price = price * discount_percentage
        return price - discounted_price


paints= DiscountedPaint(5, "red")
print(paints.total_price())
print(paints.discounted_price(discount_percentage=20))
