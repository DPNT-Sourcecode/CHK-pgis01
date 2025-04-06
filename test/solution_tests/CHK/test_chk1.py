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
        assert CheckoutSolution().checkout("K")==70

    def test_checkout4_2K_correct(self):
        assert CheckoutSolution().checkout("KK")==120

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

    def test_checkout4_1O_correct(self):
        assert CheckoutSolution().checkout("O")==10

    def test_checkout4_2O_correct(self):
        assert CheckoutSolution().checkout("OO")==20

    def test_checkout4_1P_correct(self):
        assert CheckoutSolution().checkout("P")==50

    def test_checkout4_5P_correct(self):
        assert CheckoutSolution().checkout("PPPPP")==200

    def test_checkout4_1Q_correct(self):
        assert CheckoutSolution().checkout("Q")==30

    def test_checkout4_3Q_correct(self):
        assert CheckoutSolution().checkout("QQQ")==80

    def test_checkout4_1R_correct(self):
        assert CheckoutSolution().checkout("R")==50

    def test_checkout4_3R_correct(self):
        assert CheckoutSolution().checkout("RRR")==150

    def test_checkout4_3R1Q_correct(self):
        assert CheckoutSolution().checkout("RRRQ")==150

    def test_checkout4_1S_correct(self):
        assert CheckoutSolution().checkout("S")==20

    def test_checkout4_2S_correct(self):
        assert CheckoutSolution().checkout("SS")==40

    def test_checkout4_1T_correct(self):
        assert CheckoutSolution().checkout("T")==20

    def test_checkout4_2T_correct(self):
        assert CheckoutSolution().checkout("TT")==40

    def test_checkout4_1U_correct(self):
        assert CheckoutSolution().checkout("U")==40

    def test_checkout4_2U_correct(self):
        assert CheckoutSolution().checkout("UU")==80

    def test_checkout4_3U_correct(self):
        assert CheckoutSolution().checkout("UUU")==120

    def test_checkout4_4U_correct(self):
        assert CheckoutSolution().checkout("UUUU")==120

    def test_checkout4_1V_correct(self):
        assert CheckoutSolution().checkout("V")==50

    def test_checkout4_2V_correct(self):
        assert CheckoutSolution().checkout("VV")==90

    def test_checkout4_3V_correct(self):
        assert CheckoutSolution().checkout("VVV")==130

    def test_checkout4_1W_correct(self):
        assert CheckoutSolution().checkout("W")==20

    def test_checkout4_2W_correct(self):
        assert CheckoutSolution().checkout("WW")==40

    def test_checkout4_1X_correct(self):
        assert CheckoutSolution().checkout("X")==17

    def test_checkout4_2X_correct(self):
        assert CheckoutSolution().checkout("XX")==34

    def test_checkout4_1Y_correct(self):
        assert CheckoutSolution().checkout("Y")==20

    def test_checkout4_2Y_correct(self):
        assert CheckoutSolution().checkout("YY")==40

    def test_checkout4_1Z_correct(self):
        assert CheckoutSolution().checkout("Z")==21

    def test_checkout4_2Z_correct(self):
        assert CheckoutSolution().checkout("ZZ")==42

    def test_checkout4_whole_alphabet_correct(self):
        assert CheckoutSolution().checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")==1646

    def test_checkout4_long_string_correct(self):
        assert CheckoutSolution().checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH")==1646

    def test_checkout5_STX_correct(self):
        assert CheckoutSolution().checkout("STX")==45
 
    def test_checkout5_STY_correct(self):
        assert CheckoutSolution().checkout("STY")==45

    def test_checkout5_STZ_correct(self):
        assert CheckoutSolution().checkout("STZ")==45

    def test_checkout5_SXY_correct(self):
        assert CheckoutSolution().checkout("SXY")==45


    def test_checkout5_SXZ_correct(self):
        assert CheckoutSolution().checkout("SXZ")==45
 
    def test_checkout5_SYZ_correct(self):
        assert CheckoutSolution().checkout("SYZ")==45

    def test_checkout5_TXY_correct(self):
        assert CheckoutSolution().checkout("TXY")==45

    def test_checkout5_TXZ_correct(self):
        assert CheckoutSolution().checkout("TXZ")==45

    def test_checkout5_TYZ_correct(self):
        assert CheckoutSolution().checkout("TYZ")==45
 
    def test_checkout5_XYZ_correct(self):
        assert CheckoutSolution().checkout("XYZ")==45

    def test_checkout5_ASTX_correct(self):
        assert CheckoutSolution().checkout("ASTX")==95


    def test_checkout5_SSTX_correct(self):
        assert CheckoutSolution().checkout("SSTX")==65
 
    def test_checkout5_STXXYZ_correct(self):
        assert CheckoutSolution().checkout("STXXYZ")==90

    def test_checkout5_STXZ_correct(self):
        assert CheckoutSolution().checkout("STXZ")==62

    def test_checkout5_STXYZ_correct(self):
        assert CheckoutSolution().checkout("STXYZ")==82

    def test_checkout5_STYTXYXYZ_correct(self):
        assert CheckoutSolution().checkout("STYTXYXYZ")==135


    def test_checkout5_SXY_correct(self):
        assert CheckoutSolution().checkout("SXY")==45
    def test_checkout1_incorrect(self):
        assert CheckoutSolution().checkout("a")==-1
