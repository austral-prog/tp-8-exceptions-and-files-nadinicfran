import os
import unittest

from exercise_06_grades_stats import grades_stats


class TestGradesStats(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_06_tmp.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def test_ejemplo_basico(self):
        self._write("Ana:8,9,7\nBeto:5,5,10\nCami:10\n")
        result = grades_stats(self.filename)
        self.assertAlmostEqual(8.0, result["Ana"][0])
        self.assertEqual(9.0, result["Ana"][1])
        self.assertEqual(7.0, result["Ana"][2])
        self.assertAlmostEqual(6.666666666666667, result["Beto"][0])
        self.assertEqual(10.0, result["Beto"][1])
        self.assertEqual(5.0, result["Beto"][2])
        self.assertEqual((10.0, 10.0, 10.0), result["Cami"])

    def test_retorna_tupla(self):
        self._write("Ana:8,9,7\n")
        result = grades_stats(self.filename)
        self.assertIsInstance(result["Ana"], tuple)
        self.assertEqual(3, len(result["Ana"]))

    def test_ignora_lineas_vacias(self):
        self._write("Ana:8,9,7\n\n\nBeto:6\n")
        result = grades_stats(self.filename)
        self.assertIn("Ana", result)
        self.assertIn("Beto", result)
        self.assertEqual(2, len(result))

    def test_valores_son_float(self):
        self._write("Ana:5\n")
        result = grades_stats(self.filename)
        self.assertIsInstance(result["Ana"][0], float)
        self.assertIsInstance(result["Ana"][1], float)
        self.assertIsInstance(result["Ana"][2], float)

    def test_archivo_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            grades_stats("archivo_que_no_existe_tp8_06.txt")


if __name__ == "__main__":
    unittest.main()
