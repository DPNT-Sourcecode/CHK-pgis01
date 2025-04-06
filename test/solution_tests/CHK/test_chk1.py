from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout1_correct(self):
        assert CheckoutSolution().checkout("AAAB")==160

    def test_checkout2_correct(self):
        assert CheckoutSolution().checkout("EEEBBE")==160

    def test_checkout2_correct(self):
        assert CheckoutSolution().checkout("ABCDECBAABCABBAAAEEAA")==665
        

    def test_checkout1_incorrect(self):
        assert CheckoutSolution().checkout("a")==-1


