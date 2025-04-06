
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
                 "K" : 70,
                 "L" : 90,
                 "M" : 15,
                 "N" : 40,
                 "O" : 10,
                 "P" : 50,
                 "Q" : 30,
                 "R" : 50,
                 "S" : 20,
                 "T" : 20,
                 "U" : 40,
                 "V" : 50,
                 "W" : 20,
                 "X" : 17,
                 "Y" : 20,
                 "Z" : 21
                 }
        
        # (quantity, price offer)
        special_offers = {"A" : [(5, 200), (3, 130)],
                          "B" : [(2, 45)],
                          "F" : [(3, 20)],
                          "H" : [(10, 80), (5, 45)],
                          "K" : [(2, 120)],
                          "P" : [(5, 200)],
                          "Q" : [(3, 80)],
                          "U" : [(4, 120)],
                          "V" : [(3, 130), (2, 90)]
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

        # check whether 3N offer applies
        # 3N get 1 M free 
        if checkout_items.get("N", 0) >= 3:
            triplets_of_N = checkout_items.get("N", 0)//3
            if triplets_of_N != 0:
                for n in range (0,triplets_of_N):
                    if checkout_items.get("M", 0) != 0:
                        checkout_items["M"] -= 1
                        if checkout_items["M"] == 0: # delete M from dictionary so that it wont cause an error later on
                            del checkout_items["M"]

        # check whether 3R offer applies
        # 3R get 1Q free
        if checkout_items.get("R", 0) >= 3:
            triplets_of_R = checkout_items.get("R", 0)//3
            if triplets_of_R != 0:
                for n in range (0,triplets_of_R):
                    if checkout_items.get("Q", 0) != 0:
                        checkout_items["Q"] -= 1
                        if checkout_items["Q"] == 0: # delete M from dictionary so that it wont cause an error later on
                            del checkout_items["Q"]


        

        
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
            else:
                total += count * items[item]
        

        return total