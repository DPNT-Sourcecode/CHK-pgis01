
class CheckoutSolution:

    # skus = unicode string
#     checkout(string) -> integer
#  - param[0] = a string containing the SKUs of all the products in the basket
#  - @return = an integer representing the total checkout value of the items
    def checkout(self, skus):
        # {SKU : price}
        items = {"A" : 50,
                 "B" : 30,
                 "C" : 20,
                 "D" : 15}
        
        checkout_items = {}
        skus = skus.upper()
        for i in range (len(skus)):
            if skus[i] in items:
                checkout_items[skus[i]] = 1 + checkout_items.get(skus[i], 0)
            else:
                return -1
        
        # check for any special offers

        total = 0
        for item, count in checkout_items.items():
            if item == "A" and count >= 3:
                # if 3 or more A's, apply special offer
                total += (count // 3) * 130 + (count % 3)  * items[item]
            elif item == "B" and count >= 2:
                total += (count // 2) * 45 + (count % 2)  * items[item]
            else:
                total += count * items[item]
                
        
        return total
