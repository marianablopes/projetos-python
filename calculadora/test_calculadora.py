import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_por_zero(self):
        self.assertIsNone(self.calc.dividir(10, 0))

    def test_e_logico(self):
        self.assertTrue(self.calc.e_logico(1, 1))
        self.assertFalse(self.calc.e_logico(1, 0))

    def test_ou_logico(self):
        self.assertTrue(self.calc.ou_logico(0, 1))
        self.assertFalse(self.calc.ou_logico(0, 0))

    def test_nao_logico(self):
        self.assertTrue(self.calc.nao_logico(0))
        self.assertFalse(self.calc.nao_logico(1))

    def test_historico_vazio(self):
        self.assertEqual(self.calc.historico, [])

    def test_salvar_historico(self):
        self.calc.salvar_historico("2 + 2", 4)
        self.assertEqual(self.calc.historico, ["2 + 2 = 4"])


if __name__ == "__main__":
    unittest.main()
