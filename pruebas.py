import unittest
from funciones import calcular_monto_total, descontar_comision, calcular_monto_plazo_fijo

class TestFunciones(unittest.TestCase):

    def test_calcular_monto_total(self):
        # Pruebas para calcular_monto_total con los nuevos valores esperados
        self.assertAlmostEqual(calcular_monto_total(1000, 1000), 1.65 )
        self.assertAlmostEqual(calcular_monto_total(1000, 5600), 9.82 )

    def test_descontar_comision(self):
        # Pruebas para descontar_comision
        self.assertAlmostEqual(descontar_comision(1000, 10), 900.0)
        self.assertAlmostEqual(descontar_comision(1000, 5), 950.0)

    def test_calcular_monto_plazo_fijo(self):
        # Pruebas para calcular_monto_plazo_fijo
        self.assertAlmostEqual(calcular_monto_plazo_fijo(1000, 5), 1050.0)
        self.assertAlmostEqual(calcular_monto_plazo_fijo(1000, 10), 1100.0)

if __name__ == '__main__':
    unittest.main()
