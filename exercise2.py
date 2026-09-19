"""Exercise 2: A Cart class.

Implement Cart so the example at the bottom of this file behaves correctly.

  add_item(item, qty=1)  add an item; if it is already in the cart,
                         increase the quantity instead of adding a second line
  remove_item(item_id)   remove that item entirely
  clear()                empty the cart
  total()                sum of price * qty across all lines, rounded to 2dp
  __repr__()             something readable, e.g. <Cart 3 items, $27.75>

Store each line as a dictionary:
    {"item_id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "qty": 2}
"""

from exercise1 import load_menu # what are we importing here? Food for thought.


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
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
        self.lines = [line for line in self.lines if line["item_id"] != item_id]

    def clear(self) -> None:
        self.lines.clear()

    def total(self) -> float:
        raw_total = sum(line["price"] * line["qty"] for line in self.lines)
        return round(raw_total, 2)

    def __repr__(self) -> str:
        count = len(self.lines)
        item_word = "item" if count == 1 else "items"
        return f"<Cart {count} {item_word}, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]
    ramen = menu[0]

    cart = Cart()
    cart.add_item(gyoza, 2)
    cart.add_item(gyoza, 1)      # should become qty 3, NOT a second line
    cart.add_item(ramen, 1)

    print(cart)                  # <Cart 2 items, $40.50>
    print(len(cart.lines))       # 2
    print(cart.total())          # 40.5
