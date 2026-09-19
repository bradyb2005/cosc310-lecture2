"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError(f"Quantity must be at least 1 (got {qty})")
        if not item.get("available", False):
            raise OutOfStockError(f"'{item.get('name', 'Item')}' is out of stock.")

        item_id = item.get("id", item.get("item_id"))
        for line in self.lines:
            if line["item_id"] == item_id:
                line["qty"] += qty
                return

        self.lines.append({
            "item_id": item_id,
            "name": item["name"],
            "price": item["price"],
            "qty": qty,
        })

    def remove_item(self, item_id: int) -> None:
        for i, line in enumerate(self.lines):
            if line["item_id"] == item_id:
                del self.lines[i]
                return
        raise KeyError(f"Item ID {item_id} not found in cart.")

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

# 1. Demonstrate ValueError (qty < 1)
    try:
        cart.add_item(gyoza, 0)
    except ValueError as e:
        print(f"Rejected (ValueError): {e}")

    # 2. Demonstrate OutOfStockError (item unavailable)
    try:
        cart.add_item(miso, 1)
    except OutOfStockError as e:
        print(f"Rejected (OutOfStockError): {e}")

    # 3. Demonstrate KeyError (removing item that doesn't exist)
    try:
        cart.remove_item(999)
    except KeyError as e:
        print(f"Rejected (KeyError): {e}")
