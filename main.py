from shop_module import desserts, display_menu, StockManage
from sales_module import take_order, order_process, get_sales_record, sales_report


def main():
    print("🍰 Welcome to the Dessert Shop Management Game! 🍰")

    manager = StockManage()
    stock = manager.setup_stock(desserts)
    unknown_desserts_count = {}

    while True:
        if manager.all_sold_out(stock):
            print("❗️ All desserts are sold out. We're closing the shop now. Thank you!")
            sales_report(get_sales_record())
            manager.clear_stock_file(stock)
            break

        print("\nPlease select a mode: [1] Manual customer order [2] Close shop [3] View menu")
        mode = input("mode: ").strip()

        if mode == '2':
            print("🎉 We've finished serving for today. Thank you and see you next time!")
            sales_report(get_sales_record())
            manager.clear_stock_file(stock)
            break
        elif mode == '3':
            display_menu(desserts)
            continue
        elif mode != '1':
            print("Please enter a valid option (1, 2, or 3).")
            continue

        dessert, flavor, status = take_order(stock)

        if status == "exit":
            print("🎉 We've finished serving for today. Thank you and see you next time!")
            sales_report(get_sales_record())
            manager.clear_stock_file(stock)
            break

        if status == "empty":
            print("Invalid input, please order again.")
            continue

        order_process(dessert, flavor, status, stock, unknown_desserts_count, manager)


if __name__ == '__main__':
    main()

