import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus_nollataan(self):
        v = Varasto(-5)
        self.assertAlmostEqual(v.tilavuus, 0)
        self.assertAlmostEqual(v.saldo, 0)

    def test_alkusaldo_negatiivinen_nollataan(self):
        v = Varasto(5, -2)
        self.assertAlmostEqual(v.tilavuus, 5)
        self.assertAlmostEqual(v.saldo, 0)

    def test_alkusaldo_yli_tilavuuden_tayttuu_kattoon(self):
        v = Varasto(5, 100)
        self.assertAlmostEqual(v.tilavuus, 5)
        self.assertAlmostEqual(v.saldo, 5)

    def test_paljonko_mahtuu_laskee_oikein(self):
        self.varasto.lisaa_varastoon(7)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 3)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_muuta_mitaan(self):
        self.varasto.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_liika_lisays_tayttaa_kattoon(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_otto_palauttaa_nolla_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_liika_otto_palauttaa_kaiken_ja_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(6)
        saatu = self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(saatu, 6)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_muoto(self):
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")
