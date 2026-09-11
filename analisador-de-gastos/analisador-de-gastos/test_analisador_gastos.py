import unittest
from analisador_gastos import calcular_total, filtrar_por_categoria


class TestAnalisadorGastos(unittest.TestCase):

    def setUp(self):
        self.gastos = [
            {"descricao": "Mercado", "valor": 150.0, "categoria": "Alimentação"},
            {"descricao": "Uber", "valor": 30.0, "categoria": "Transporte"},
            {"descricao": "Cinema", "valor": 50.0, "categoria": "Lazer"},
            {"descricao": "Restaurante", "valor": 80.0, "categoria": "Alimentação"},
        ]

    def test_total_geral(self):
        total = sum(g["valor"] for g in self.gastos)
        self.assertEqual(total, 310.0)

    def test_total_por_categoria(self):
        categorias = {}
        for gasto in self.gastos:
            cat = gasto["categoria"]
            categorias[cat] = categorias.get(cat, 0) + gasto["valor"]
        self.assertEqual(categorias["Alimentação"], 230.0)
        self.assertEqual(categorias["Transporte"], 30.0)
        self.assertEqual(categorias["Lazer"], 50.0)

    def test_lista_vazia(self):
        self.assertEqual(sum(g["valor"] for g in []), 0)

    def test_filtro_categoria_existente(self):
        filtrados = [g for g in self.gastos if g["categoria"] == "Alimentação"]
        self.assertEqual(len(filtrados), 2)

    def test_filtro_categoria_inexistente(self):
        filtrados = [g for g in self.gastos if g["categoria"] == "Educação"]
        self.assertEqual(len(filtrados), 0)


if __name__ == "__main__":
    unittest.main()
