"""
Prpduct Model for IMS
"""

class Product():
    """
    class product describe product model
    """
    self.item_id = 0
    self.name = ''
    self.description = ''
    self.quantity = 0
    self.price = 0.0
    self.supplier = []

    def __init__(self, name, description, quantity, price, supplier):
        """
        """
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

