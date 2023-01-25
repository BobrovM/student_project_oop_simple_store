import pandas as pd
from print_pdf import print_pdf


df = pd.read_csv("articles.csv")
print(df)


class ShopItem:
    def __init__(self, item_id):
        self.item_id = item_id
        self.name = df.loc[df["id"] == self.item_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.item_id, "price"].squeeze()

    def buy_operation(self):
        in_stock = df.loc[df["id"] == self.item_id, "in stock"].squeeze()
        if in_stock > 0:
            print_pdf(self.item_id, self.name, self.price)
            in_stock -= 1
            df.loc[df["id"] == self.item_id, "in stock"] = in_stock
            df.to_csv("articles.csv", index=False)
            return True
        return False


item_id = int(input("Choose an article to buy: "))
shop_item = ShopItem(item_id)
if shop_item.buy_operation():
    print("Successful transaction.")
else:
    print(f"Sorry, but the {str(shop_item.name).title()} is not available.")