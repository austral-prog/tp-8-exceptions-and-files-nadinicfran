import os
import unittest

from exercise_08_find_longest_word import find_longest_word


class TestFindLongestWord(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_08_tmp.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def test_ejemplo_basico(self):
        self._write("el gato corre rapido\npor el jardin\n")
        self.assertEqual("rapido", find_longest_word(self.filename))

    def test_primera_aparicion_en_empate(self):
        self._write("uno dos tres cuatro cinco\n")
        # "cuatro" y "cinco" tienen 6 y 5 letras. cuatro gana.
        # Probemos con empate real:
        self._write("rojo azul gris\n")
        # Todos 4 letras -> gana "rojo"
        self.assertEqual("rojo", find_longest_word(self.filename))

    def test_archivo_con_una_palabra(self):
        self._write("unica\n")
        self.assertEqual("unica", find_longest_word(self.filename))

    def test_multilinea(self):
        self._write("a\nbb\nccc\ndddd\n")
        self.assertEqual("dddd", find_longest_word(self.filename))

    def test_archivo_vacio_lanza_value_error(self):
        self._write("")
        with self.assertRaises(ValueError):
            find_longest_word(self.filename)

    def test_archivo_solo_espacios_lanza_value_error(self):
        self._write("   \n\t\n  \n")
        with self.assertRaises(ValueError):
            find_longest_word(self.filename)

    def test_archivo_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            find_longest_word("archivo_que_no_existe_tp8_08.txt")


if __name__ == "__main__":
    unittest.main()
