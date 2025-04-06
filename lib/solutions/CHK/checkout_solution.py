
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
                 "E" : 40,
                 "F" : 10,
                 "G" : 20,
                 "H" : 10,
                 "I" : 35,
                 "J" : 60,
                 "K" : 80,
                 "L" : 90,
                 "M" : 15,
                 "N" : 40,
                 "O" : 10,
                 "P" : 50,
                 "Q" : 30,
                 "R" : 50,
                 "S" : 30,
                 "T" : 20,
                 "U" : 40,
                 "V" : 50,
                 "W" : 20,
                 "X" :90,
                 "Y" : 10,
                 "Z" : 50
                 }
        
        # (quantity, price offer)
        special_offers = {"A" : [(3, 130), (5, 200)],
                          "B" : [(2, 35)]
                         

        }

        checkout_items = {}
        
        for i in range (len(skus)):
            if skus[i] in items:
                checkout_items[skus[i]] = 1 + checkout_items.get(skus[i], 0)
            else:
                return -1
            
        # check whether 2E special offer applies
        if checkout_items.get("E", 0) >= 2:
            pairs_of_E = checkout_items.get("E", 0)//2
            print("pairs" + str(pairs_of_E))
            if pairs_of_E != 0:
                for e in range (0,pairs_of_E):
                    if checkout_items.get("B", 0) != 0:
                        checkout_items["B"] -= 1
                        if checkout_items["B"] == 0: # delete B from dictionary so that it wont cause an error later on
                            del checkout_items["B"]


            

        
        # check for any special offers

        total = 0
        for item, count in checkout_items.items():
            # if item is in the special_offer dictionary
            if item in special_offers:
                for offer_quantity, offer_price in special_offers[item]:
                    offer_count = count // offer_quantity
                    total += offer_count * offer_price
                    count %= offer_quantity
                total += count * items[item]
            # if item == "A":
            #     # if 5 or more A's, apply special offer
            #     total += (count // 5) * 200
            #     remainder = (count % 5) 

            #     if remainder >= 3:
            #         total += (remainder // 3) * 130 
            #         remainder = remainder % 3

            #     total += remainder * items[item]

            elif item == "B":
                total += (count // 2) * 45 + (count % 2)  * items[item]

            elif item == "F":
                free_f = count // 3
                total += (count-free_f) * items[item]
            
            elif item == "H":
                total += (count // 10) * 80
                remainder = (count % 10) 

                if remainder >= 5:
                    total += (remainder // 5) * 45 
                    remainder = remainder % 5

                total += remainder * items[item]

            else:
                total += count * items[item]

        return total
