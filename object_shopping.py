
from IPython.display import clear_output

class Cart:
    items = []
    total_price = []

    def add_item(self, cart_item):
        return self.items.append(cart_item)
        
    def add_price(self, item_price):
        return self.total_price.append(item_price)

    def remove_item(self, item_name):
        for i in self.items:
            if item_name in i[0]:
                self.items.remove(i)
                self.total_price.remove(i[1])

    def clear_items(self):
        self.items.clear()
    
    def show_cart(self):
        if len(self.items) == 0:
            print("=" * 40)
            print("Your cart is empty.")
            print ("-" * 40)
            print("Your total: $0.00")
            print("=" * 40)
        else:
            display_cart = [] 
            print("=" * 40)
            for i in self.items:
                if i not in display_cart:
                    display_cart.append({
                        'name': i[0],
                        'price': i[1]
                    })
                elif i in display_cart:
                    for i in self.items:
                        print(i.count())
            for i in range(len(display_cart)):
                print(f"{i+1}: {display_cart[i]['name'].title()}  ${display_cart[i]['price']:.2f}")
            print("-" * 40)
            total = float(sum(self.total_price))
            print(f"Your total:  ${total:.2f}")
            print("=" * 40)


class ShoppingCart:

    def starting_cart():
        print("\nWelcome to the store!")
        print("-" * 40)
        print("Type 'add' to add an item to your cart.")
        print("Type 'remove' to remove an item from your cart.")
        print("Type 'clear' to remove all items from your cart.")
        print("Type 'quit' to exit program and show your cart.")

    @classmethod
    def run(self):  
        cart = Cart()
        done = False
        while not done:
            clear_output()
            self.starting_cart()
            cart.show_cart()
            ask = input("What would you like to do?   ").lower()
            if ask == "quit":
                confirm = input("Are you sure you are done shopping? Y/N   ").lower()
                cart.show_cart()
                if confirm == "y":
                    print("Thank you for shoppping with us!\n")
                    done = True
            elif ask == 'add':
                item_name = input("What item would you like to add?   ").lower()
                item_price = float(input("How much does the item cost?   "))
                #print(item_price) this is for test purpose but it wouldn't print. why?
                cart_item = (item_name, float(item_price))
                cart.add_item(cart_item)
                cart.add_price(item_price)
            elif ask == "remove":
                item_name = input("What would you like to remove?   ").lower()
                cart.remove_item(item_name)
            elif ask == "clear":
                cart.clear_items()
            
ShoppingCart.run()   

