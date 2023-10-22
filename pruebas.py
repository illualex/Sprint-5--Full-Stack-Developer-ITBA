import unittest
from funciones import calcular_monto_total, descontar_comision, calcular_monto_plazo_fijo

class TestFunciones(unittest.TestCase):
    def test_calcular_monto_total_clienteClassic(self):
        resultado = calcular_monto_total(100, 1000, 0.5, 1, tipo_cliente="clienteClassic")
        self.assertAlmostEqual(round(resultado, 2), 1015.0)  # Resultado esperado redondeado

    def test_calcular_monto_total_clienteGold(self):
        resultado = calcular_monto_total(100, 1000, 0.1, 0.5, tipo_cliente="clienteGold")
        self.assertAlmostEqual(round(resultado, 2), 1006.0)  # Resultado esperado redondeado

    def test_calcular_monto_total_clienteBlack(self):
        resultado = calcular_monto_total(100, 1000, 0, 0, tipo_cliente="clienteBlack")
        self.assertAlmostEqual(round(resultado, 2), 1000.0)  # Resultado esperado redondeado

    def test_descontar_comision(self):
        monto_descontado = descontar_comision(1000, 5)
        self.assertAlmostEqual(round(monto_descontado, 2), 950.0)  # Resultado esperado redondeado

    def test_calcular_monto_plazo_fijo(self):
        monto_final = calcular_monto_plazo_fijo(1000, 2)
        self.assertAlmostEqual(round(monto_final, 2), 1020.0)  # Resultado esperado redondeado

if __name__ == '__main__':
    unittest.main()
