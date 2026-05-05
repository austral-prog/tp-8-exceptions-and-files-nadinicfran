import os
import unittest

from exercise_02_count_words import count_words


class TestCountWords(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_02_tmp.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def test_conteo_basico(self):
        self._write("hola mundo hola\nmundo python\n")
        self.assertEqual(
            {"hola": 2, "mundo": 2, "python": 1},
            count_words(self.filename),
        )

    def test_case_insensitive(self):
        self._write("Hola HOLA hola\n")
        self.assertEqual({"hola": 3}, count_words(self.filename))

    def test_archivo_vacio(self):
        self._write("")
        self.assertEqual({}, count_words(self.filename))

    def test_separadores_varios(self):
        self._write("a  b\tc\na\n")
        self.assertEqual({"a": 2, "b": 1, "c": 1}, count_words(self.filename))

    def test_archivo_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            count_words("archivo_que_no_existe_tp8_02.txt")

    def test_retorna_dict(self):
        self._write("uno dos\n")
        self.assertIsInstance(count_words(self.filename), dict)


if __name__ == "__main__":
    unittest.main()
