from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout1_correct(self):
        assert CheckoutSolution().checkout("A,3A,B")==210

    def test_checkout1_correct(self):
        assert CheckoutSolution().checkout("A,E")==-1