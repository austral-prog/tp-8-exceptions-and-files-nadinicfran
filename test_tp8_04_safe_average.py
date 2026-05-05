import os
import unittest

from exercise_04_safe_average import safe_average


class TestSafeAverage(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_04_tmp.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def test_promedio_simple(self):
        self._write("10\n20\n30\n")
        self.assertEqual(20.0, safe_average(self.filename))

    def test_ignora_lineas_invalidas(self):
        self._write("10\n20\nno_es_un_numero\n30\n")
        self.assertEqual(20.0, safe_average(self.filename))

    def test_ignora_lineas_vacias(self):
        self._write("10\n\n20\n\n")
        self.assertEqual(15.0, safe_average(self.filename))

    def test_flotantes(self):
        self._write("1.5\n2.5\n")
        self.assertAlmostEqual(2.0, safe_average(self.filename))

    def test_retorna_float(self):
        self._write("5\n")
        self.assertIsInstance(safe_average(self.filename), float)

    def test_archivo_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            safe_average("archivo_que_no_existe_tp8_04.txt")

    def test_archivo_sin_numeros_validos(self):
        self._write("hola\nmundo\n")
        with self.assertRaises(ValueError):
            safe_average(self.filename)

    def test_archivo_vacio_sin_numeros(self):
        self._write("")
        with self.assertRaises(ValueError):
            safe_average(self.filename)


if __name__ == "__main__":
    unittest.main()
