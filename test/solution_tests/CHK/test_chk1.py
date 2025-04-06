from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout1_correct(self):
        assert CheckoutSolution().checkout("AAAB")==160

    def test_checkout1_1_correct(self):
        assert CheckoutSolution().checkout("EEEBBE")==160

    def test_checkout2E_correct(self):
        assert CheckoutSolution().checkout("ABCDECBAABCABBAAAEEAA")==665
        
    def test_checkout3F_correct(self):
        assert CheckoutSolution().checkout("F")==10
        
    def test_checkout3_1F_correct(self):
        assert CheckoutSolution().checkout("FF")==20

    def test_checkout3_2F_correct(self):
        assert CheckoutSolution().checkout("FFF")==20

    def test_checkout3_3F_correct(self):
        assert CheckoutSolution().checkout("AFFF")==70
        
    def test_checkout3_4F_correct(self):
        assert CheckoutSolution().checkout("AFFFFF")==90

    def test_checkout3_5F_correct(self):
        assert CheckoutSolution().checkout("FFFF")==30

    def test_checkout4_1G_correct(self):
        assert CheckoutSolution().checkout("G")==20

    def test_checkout4_2G_correct(self):
        assert CheckoutSolution().checkout("GG")==40
        
    def test_checkout1_incorrect(self):
        assert CheckoutSolution().checkout("a")==-1


