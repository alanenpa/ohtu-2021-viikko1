import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_tilavuus_luo_tilattoman_varaston(self):
        self.varasto = Varasto(-1)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_saldo_luo_tyhjan_varaston(self):
        self.varasto = Varasto(10,-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ylimaarainen_saldo_menee_hukkaan(self):
        self.varasto = Varasto(10,12)

        self.assertAlmostEqual(self.varasto.saldo, 12)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_lisays_ei_toimi(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_otto_ei_toimi(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_liikaa_ottaminen_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(7)
        self.assertAlmostEqual(self.varasto.ota_varastosta(11), 7)

    def test_liikaa_ei_voi_lisata(self):
        print('hei', self.varasto.paljonko_mahtuu())
        self.varasto.lisaa_varastoon(11)
        print(self.varasto)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
