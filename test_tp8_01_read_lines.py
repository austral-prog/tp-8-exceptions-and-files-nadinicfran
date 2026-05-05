import os
import unittest

from exercise_01_read_lines import read_lines


class TestReadLines(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_01_tmp.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def test_lineas_basicas(self):
        self._write("manzana\nbanana\npera\n")
        self.assertEqual(["manzana", "banana", "pera"], read_lines(self.filename))

    def test_strip_de_espacios(self):
        self._write("  hola  \nmundo\t\n")
        self.assertEqual(["hola", "mundo"], read_lines(self.filename))

    def test_ignora_lineas_vacias(self):
        self._write("a\n\nb\n   \nc\n")
        self.assertEqual(["a", "b", "c"], read_lines(self.filename))

    def test_archivo_vacio_retorna_lista_vacia(self):
        self._write("")
        self.assertEqual([], read_lines(self.filename))

    def test_archivo_no_existe_lanza_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_lines("archivo_que_no_existe_tp8_01.txt")

    def test_retorna_lista(self):
        self._write("uno\ndos\n")
        self.assertIsInstance(read_lines(self.filename), list)


if __name__ == "__main__":
    unittest.main()
