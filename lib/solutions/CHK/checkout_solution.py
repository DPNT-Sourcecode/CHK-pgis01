
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
                 "D" : 15,
                 "E" : 40}
        
        checkout_items = {}
        
        for i in range (len(skus)):
            if skus[i] in items:
                checkout_items[skus[i]] = 1 + checkout_items.get(skus[i], 0)
            else:
                return -1
        
        # check for any special offers

        total = 0
        for item, count in checkout_items.items():
            if item == "A":
                # if 5 or more A's, apply special offer
                total += 5 (count // 5) * 200
                remainder = (count % 5) 
                
                if remainder >= 3:
                    total += (remainder // 3) * 130 
                    remainder = remainder % 3
               
                total += remainder * 50

            elif item == "B" and count >= 2:
                total += (count // 2) * 45 + (count % 2)  * items[item]
            else:
                total += count * items[item]
                
        
        return total
