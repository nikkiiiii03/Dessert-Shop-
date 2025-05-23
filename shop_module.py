desserts = ["croissant", "donut", "bagel", "cake"]
flavors = ["chocolate", "strawberry", "cream"]


class StockManage:
    def __init__(self):
        self.stock_file = "stock.txt"

    def setup_stock(self, desserts):
        print("Please set today's stock quantity for each dessert:")
        stock = {}
        for dessert in desserts:
            while True:
                try:
                    count = int(input(f"{dessert}: "))
                    if count < 0:
                        print("Please enter a non-negative integer.")
                        continue
                    stock[dessert] = count
                    break
                except ValueError:
                    print("Please enter a valid integer.")
        self.save_stock_to_file(stock)
        return stock

    def save_stock_to_file(self, stock):
        with open(self.stock_file, 'w') as f:
            for dessert, quantity in stock.items():
                f.write(f"{dessert}: {quantity}\n")

    def clear_stock_file(self, stock):
        with open(self.stock_file, 'w') as f:
            f.write("")
        for dessert in list(stock.keys()):
            stock[dessert] = 0

    def all_sold_out(self, stock):
        return all(quantity == 0 for quantity in stock.values())


def display_stock(stock):
    print("\n📦 Current Stock:")
    for dessert, quantity in stock.items():
        print(f"{dessert}: {quantity}")


def display_menu(desserts):
    print("\n🍰 Desserts:")
    for dessert in desserts:
        print(f"- {dessert}")
    print("\n🍯 Flavors:")
    for flavor in flavors:
        print(f"- {flavor}")

def dessert_image(dessert):
    image = {
        'croissant': r"""
          ___
(🥐)    /     \   (🥐)
    \ (  ^   ^  ) /
     |_____▽_____|
     |___________|
      (_________) 
        \     /
          ---
""",
        'donut': r"""

       ___
    .-"   "-.
  .'   . ;   `.
 /    : . ' :  \
|   `  .-. . '  |
|  :  (   ) ; ` |
|   :  `-'   :  |
 \   .` ;  :   /
  `.   . '   .'
    `-.___.-'

""",
        'bagel': r"""
       ___
    .-"   "-.
  .'   . ;   `.
 /    : . ' :  \
|   `  .-. .    |
|       🥯      |
|   :  `-'   :  |
 \   .` ;  :   /
  `.   . '   .'
    `-.___.-'
""",
        'cake': r"""
         (.)
         .|.
         l7J
     _.--| |--._
  .-';  ;`-'& ; `&.
 & &  ;  &   ; ;   \
 \      ;    &   &_/
  s---------------s
  | | | | | | | | |
  | | | | | | | | | 
   `---.|.|.|. ---' 
"""
    }
    default_image = r"""
   ==!!!NEW!!!==      
"""
    print(image.get(dessert, default_image))
  

