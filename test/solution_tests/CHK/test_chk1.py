from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout1_1A_correct(self):
        assert CheckoutSolution().checkout("A")==50

    def test_checkout1_3A_correct(self):
        assert CheckoutSolution().checkout("AAA")==130

    def test_checkout1_1B_correct(self):
        assert CheckoutSolution().checkout("B")==30
    
    def test_checkout1_2B_correct(self):
        assert CheckoutSolution().checkout("BB")==45

    def test_checkout2_1C_correct(self):
        assert CheckoutSolution().checkout("C")==20

    def test_checkout2_2C_correct(self):
        assert CheckoutSolution().checkout("CC")==40

    def test_checkout2_1D_correct(self):
        assert CheckoutSolution().checkout("D")==15

    def test_checkout2_2D_correct(self):
        assert CheckoutSolution().checkout("DD")==30

    def test_checkout2_1E_correct(self):
        assert CheckoutSolution().checkout("E")==40

    def test_checkout2_2E_correct(self):
        assert CheckoutSolution().checkout("EE")==80

    def test_checkout2_2E1B_correct(self):
        assert CheckoutSolution().checkout("EEB")==80

    def test_checkout3_5A_correct(self):
        assert CheckoutSolution().checkout("A")==50

    def test_checkout3_1F_correct(self):
        assert CheckoutSolution().checkout("F")==10
        
    def test_checkout3_2F_correct(self):
        assert CheckoutSolution().checkout("FF")==20

    def test_checkout3_3F_correct(self):
        assert CheckoutSolution().checkout("FFF")==20

    def test_checkout3_1A3F_correct(self):
        assert CheckoutSolution().checkout("AFFF")==70
        
    def test_checkout3_1A5F_correct(self):
        assert CheckoutSolution().checkout("AFFFFF")==90

    def test_checkout3_4F_correct(self):
        assert CheckoutSolution().checkout("FFFF")==30

    def test_checkout4_1G_correct(self):
        assert CheckoutSolution().checkout("G")==20

    def test_checkout4_2G_correct(self):
        assert CheckoutSolution().checkout("GG")==40

    def test_checkout4_1H_correct(self):
        assert CheckoutSolution().checkout("H")==10
    
    def test_checkout4_2H_correct(self):
        assert CheckoutSolution().checkout("HH")==20
    
    def test_checkout4_5H_correct(self):
        assert CheckoutSolution().checkout("HHHHH")==45

    def test_checkout4_10H_correct(self):
        assert CheckoutSolution().checkout("HHHHHHHHHH")==80

    def test_checkout4_1A5H_correct(self):
        assert CheckoutSolution().checkout("AHHHHH")==95

    def test_checkout4_1I_correct(self):
        assert CheckoutSolution().checkout("I")==35

    def test_checkout4_2I_correct(self):
        assert CheckoutSolution().checkout("II")==70

    def test_checkout4_1J_correct(self):
        assert CheckoutSolution().checkout("J")==60

    def test_checkout4_2J_correct(self):
        assert CheckoutSolution().checkout("JJ")==120

    def test_checkout4_1K_correct(self):
        assert CheckoutSolution().checkout("K")==80

    def test_checkout4_2K_correct(self):
        assert CheckoutSolution().checkout("KK")==150

    def test_checkout4_1L_correct(self):
        assert CheckoutSolution().checkout("L")==90

    def test_checkout4_2L_correct(self):
        assert CheckoutSolution().checkout("LL")==180

    def test_checkout4_1M_correct(self):
        assert CheckoutSolution().checkout("M")==15

    def test_checkout4_2M_correct(self):
        assert CheckoutSolution().checkout("MM")==30

    def test_checkout4_1N_correct(self):
        assert CheckoutSolution().checkout("N")==40

    def test_checkout4_3N_correct(self):
        assert CheckoutSolution().checkout("NNN")==120

    def test_checkout4_3N1M_correct(self):
        assert CheckoutSolution().checkout("NNNM")==120

    # def test_checkout1_correct(self):
    #     assert CheckoutSolution().checkout("AAAB")==160

    # def test_checkout1_1_correct(self):
    #     assert CheckoutSolution().checkout("EEEBBE")==160

    # def test_checkout2E_correct(self):
    #     assert CheckoutSolution().checkout("ABCDECBAABCABBAAAEEAA")==665
        
   




    def test_checkout1_incorrect(self):
        assert CheckoutSolution().checkout("a")==-1
