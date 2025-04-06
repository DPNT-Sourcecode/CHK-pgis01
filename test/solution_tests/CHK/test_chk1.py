from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout1_correct(self):
        assert CheckoutSolution().checkout("AAAB")==210

    def test_checkout1_incorrect(self):
        assert CheckoutSolution().checkout("a")==-1

