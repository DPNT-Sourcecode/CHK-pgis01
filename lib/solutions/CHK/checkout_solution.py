
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
        
        special_offers = {"3A" : 130,
                          "2B" : 45}

        if " " in skus:
            skus_list = skus.split(" ")
        
        if "," in skus:
            skus_list = skus.split(",")

        total = 0

        for i in skus_list:
            if i in items:
                total += items.get(i)
            elif i in special_offers:
                total += special_offers.get(i)
            else:
                return -1
        
        return total
