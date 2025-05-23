from shop_module import desserts, flavors, dessert_image, display_stock

sales_record = {}

def take_order(stock):
    print("\nWhat dessert would you like to order today?")
    dessert = input("dessert: ").strip().lower()
    if dessert == "2":
        return "EXIT", "", "exit"
    if not dessert:
        return "", "", "empty"

    if dessert not in desserts:
        return dessert, "", "not offered"

    if stock.get(dessert, 0) == 0:
        print("❌ Sorry, that dessert is sold out.")
        return dessert, "", "sold out"

    print("Which flavor would you like? (chocolate / strawberry / cream)")
    flavor = input("flavor: ").strip().lower()

    if not flavor:
        print("No flavor entered. We'll prepare cream flavor.")
        flavor = "cream"
    elif flavor not in flavors:
        print("❌ We don't have that flavor. We'll prepare cream flavor.")
        flavor = "cream"

    return dessert, flavor, "ok"


def order_process(dessert, flavor, status, stock, unknown_desserts_count, manager):
    if status == "not offered":
        print("❌ We are not offering that kind of dessert.")
        unknown_desserts_count[dessert] = unknown_desserts_count.get(dessert, 0) + 1
        if unknown_desserts_count[dessert] >= 3:
            print(f"\n🤔 Customers have repeatedly requested '{dessert}'. Would you like to add it to the menu? (yes/no)")
            while True:
                reply = input("Staff: ").strip().lower()
                if reply == 'yes':
                    print(f"✨ '{dessert}' has been added as a new dessert! (2 servings available by default)")
                    desserts.append(dessert)
                    stock[dessert] = 2
                    manager.save_stock_to_file(stock)
                    break
                elif reply == 'no':
                    print(f"❌ '{dessert}' doesn't seem like a dessert and cannot be added to the menu.")
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
            unknown_desserts_count[dessert] = 0
        return

    if status == "sold out":
        return

    if status == "ok":
        stock[dessert] -= 1
        sales_record[dessert] = sales_record.get(dessert, 0) + 1
        print(f"\nOne {flavor} {dessert} coming right up!")
        dessert_image(dessert)
        display_stock(stock)
        manager.save_stock_to_file(stock)


def get_sales_record():
    return sales_record


def sales_report(sales_record):
    print("\n📊 Today's Sales Report:")
    if not sales_record:
        print("No sales recorded.")
    else:
        for dessert, count in sales_record.items():
            print(f"{dessert}: {count} sold")

